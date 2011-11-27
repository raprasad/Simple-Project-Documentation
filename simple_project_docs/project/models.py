from django.db import models
from django.template.defaultfilters import slugify


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
    slug = models.SlugField(max_length=255, blank=True)
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
    
    def get_html_filename(self):
        if not self.slug:
            return None
        return '%s.html' % self.slug
        
    def save(self):
        if self.id is None:
            super(Project, self).save()
            
        self.slug = slugify(self.name)
        while 1:
            if Project.objects.exclude(id=self.id).filter(slug=self.slug).count() > 0:
                self.slug = self.slug + '_'
            else:
                break
                
        super(Project, self).save()
        
        
    class Meta:
        ordering = ('name', )
    
    
class ProjectNote(models.Model):
    project = models.ForeignKey(Project)
    note = models.TextField()
    
    last_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('last_update', 'project' )
