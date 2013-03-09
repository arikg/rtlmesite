from tastypie.resources import ModelResource
from rtlmesite.apps.main.models import Result


class ResultResource(ModelResource):
    class Meta:
        queryset = Result.objects.all()
        allowed_methods = ['get']