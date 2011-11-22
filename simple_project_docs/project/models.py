from django.db import models


class AuthSystem(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name', )

class Server(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True)
 
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name', )
 
class ProjectTag(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name', )
    
        
class Project(models.Model):
    name = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    contacts = models.TextField()

    url = models.URLField(blank=True)
    codebase = models.TextField(blank=True)
    authentication = models.ManyToManyField(AuthSystem, blank=True, null=True)
    servers = models.ManyToManyField(Server, blank=True, null=True)
    
    related_projects = models.ManyToManyField('self', related_name='related projects', blank=True, null=True)
    tags = models.ManyToManyField(ProjectTag, blank=True, null=True)
    
    last_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
    
    
class ProjectNote(models.Model):
    project = models.ForeignKey(Project)
    note = models.TextField()
    
    last_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('last_update', 'project' )
