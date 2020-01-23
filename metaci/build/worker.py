import errno
import os
import signal

from rq.worker import StopRequested, Worker, signal_name


class RequeueingWorker(Worker):
    """An extension of the base rq worker which handles requeueing the job
    if SIGTERM or SIGINT causes the worker to close.  This currently uses
    the delay method on the target function so the function must support that
    """

    def _install_signal_handlers(self):
        """Installs signal handlers for handling SIGINT and SIGTERM
        gracefully.
        """

        def request_force_stop(signum, frame):
            """Terminates the application (cold shutdown)."""
            self.log.warning("Cold shut down.")
            self.log.debug(f"Got signal: {signal_name(signum)}")

            # If shutdown is requested in the middle of a job,
            # requeue the job
            if self.get_current_job():
                job = self.get_current_job()
                self.log.debug(f"Attempting to delay job: {job}")
                job.func.delay(*job.args, **job.kwargs)

            # Take down the horse with the worker
            if self.horse_pid:
                self.log.debug(f"Taking down horse {self.horse_pid} with me.")
                try:
                    os.kill(self.horse_pid, signal.SIGKILL)
                except OSError as e:
                    # ESRCH ("No such process") is fine with us
                    if e.errno != errno.ESRCH:
                        self.log.debug("Horse already down.")
                        raise

            self.log.debug("raising SystemExit()")
            raise SystemExit()

        def request_stop(signum, frame):
            """Stops the current worker loop but waits for child processes to
            end gracefully (warm shutdown).
            """
            self.log.debug(f"Got signal: {signal_name(signum)}")

            signal.signal(signal.SIGINT, request_force_stop)
            signal.signal(signal.SIGTERM, request_force_stop)

            self.log.warning("Warm shut down requested.")

            # If shutdown is requested in the middle of a job, wait until
            # finish before shutting down
            if self.get_current_job():
                self._stopped = True
                self.log.debug(
                    "Stopping after current horse is finished. "
                    "Press Ctrl+C again for a cold shutdown."
                )
            else:
                self.log.debug("raising StopRequested()")
                raise StopRequested()

        signal.signal(signal.SIGINT, request_stop)
        signal.signal(signal.SIGTERM, request_stop)
