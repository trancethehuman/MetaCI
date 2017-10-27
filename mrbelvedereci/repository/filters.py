import rest_framework_filters as filters
from mrbelvedereci.repository.models import Branch
from mrbelvedereci.repository.models import Repository

class RepositoryRelatedFilter(filters.FilterSet):
    class Meta:
        model = Repository
        fields = [
            'id',
            'name',
            'owner',
            'url',
            'github_id',
        ]

class RepositoryFilter(RepositoryRelatedFilter):
    pass

class BranchRelatedFilter(filters.FilterSet):
    repo = filters.RelatedFilter(RepositoryRelatedFilter, name='repo', queryset=Repository.objects.all())
    class Meta:
        model = Branch
        fields = [
            'id',
            'name',
            'deleted',
        ]

class BranchFilter(BranchRelatedFilter):
    pass
