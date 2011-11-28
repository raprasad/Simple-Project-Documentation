from django.contrib import admin

from project.models import AuthSystem, Server, ProjectTag, Project, ProjectNote, ProjectStatus


class AuthSystemAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ['name', 'url', 'description']
    search_fields =  ['name', 'url', 'description']
admin.site.register(AuthSystem, AuthSystemAdmin)

class ServerAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ['name', 'url', 'short_description']
    search_fields =  ['name', 'url', 'short_description', 'description']
admin.site.register(Server, ServerAdmin)


class ProjectStatusAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ['name' ]
    search_fields =  ['name']
admin.site.register(ProjectStatus, ProjectStatusAdmin)

class ProjectTagAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ['name', 'url', 'description']
    search_fields =  ['name', 'url', 'description']
admin.site.register(ProjectTag, ProjectTagAdmin)


class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['last_update', 'date_added']
    list_filter = ['is_live', 'status']
    
    filter_horizontal = ['related_projects', 'tags', 'authentication', 'servers']
    list_display= ['name', 'purpose', 'is_live', 'status', 'last_update', 'date_added']
    search_fields =  ['name', 'purpose', 'description', 'contacts',  'last_update']
admin.site.register(Project, ProjectAdmin)
