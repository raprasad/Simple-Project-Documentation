from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import direct_to_template

from django.views.generic import list_detail
from project.views import project_detail
from project.models import Project


project_info = {
    "queryset" : Project.objects.all(),
        "template_object_name" : "project",
}

urlpatterns = patterns('',
    url(r'^list/$', list_detail.object_list, project_info, name='project_list'),#, {'template_name':'project/project_list.html'}),
    url(r'^detail/(?P<project_id>\d+)/$', project_detail, name='project_detail'),
    #, {'template': 'onesheet.html'}),
)

"""
urlpatterns = patterns('',
    (r'^list/$',             direct_to_template, {'template': 'project_index.html'}),
    (r'^detail/(?P<id>\d+)/$', direct_to_template, {'template': 'onesheet.html'}),
)
"""