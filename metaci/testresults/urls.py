from django.conf.urls import url

from metaci.testresults import views

urlpatterns = [
    url(
        r"^(?P<build_id>\d+)/(?P<flow>.*)/compare-to",
        views.build_flow_compare_to,
        name="build_flow_compare_to",
    ),
    url(
        r"^(?P<build_id>\d+)/(?P<flow>.*)/download-asset/(?P<category>.*)$",
        views.build_flow_download_asset,
        name="build_flow_download_asset",
    ),
    url(
        r"^(?P<build_id>\d+)/(?P<flow>.*)$",
        views.build_flow_tests,
        name="build_flow_tests",
    ),
    url(
        r"^trend/method/(?P<method_id>\d+)$",
        views.test_method_trend,
        name="test_method_trend",
    ),
    url(
        r"^method/(?P<method_id>\d+)$", views.test_method_peek, name="test_method_peek"
    ),
    url(
        r"^result/(?P<result_id>\d+)$",
        views.test_result_detail,
        name="test_result_detail",
    ),
    url(
        r"^result/(?P<result_id>\d+)/robot$",
        views.test_result_robot,
        name="test_result_robot",
    ),
    url(r"^compare/$", views.build_flow_compare, name="build_flow_compare"),
]
