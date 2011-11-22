from django.contrib import admin

from project.models import AuthSystem, Server, ProjectTag, Project, ProjectNote


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


class ProjectTagAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ['name', 'url', 'description']
    search_fields =  ['name', 'url', 'description']
admin.site.register(ProjectTag, ProjectTagAdmin)


class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['last_update', 'date_added']
    list_display= ['name', 'purpose', 'last_update', 'date_added']
    search_fields =  ['name', 'purpose', 'description', 'contacts',  'last_update']
admin.site.register(Project, ProjectAdmin)
