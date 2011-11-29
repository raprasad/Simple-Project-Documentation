from django.contrib import admin

from project.models import *

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

class ProjectLinkAdminInline(admin.TabularInline):
    model = ProjectLink
    extra=0

class ProjectDocAdminInline(admin.TabularInline):
    model = ProjectDoc
    extra=0

class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['last_update', 'date_added']
    list_filter = ['is_live', 'status']
    inlines = [ProjectLinkAdminInline, ProjectDocAdminInline]
    
    filter_horizontal = ['related_projects', 'tags', 'authentication', 'servers']
    list_display= ['name', 'purpose', 'is_live', 'status', 'last_update', 'date_added']
    search_fields =  ['name', 'purpose', 'description', 'contacts',  'last_update']
admin.site.register(Project, ProjectAdmin)
