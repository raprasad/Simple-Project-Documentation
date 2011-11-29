import os, sys

if __name__=='__main__':
    paths = ['/Users/rprasad/mcb-git/Simple-Project-Documentation/simple_project_docs'\
            , '/Users/rprasad/projects/mcb-git/Simple-Project-Documentation/simple_project_docs'\
            ]
    for p in paths:
        if os.path.isdir(p): sys.path.append(p)
    from django.core.management import setup_environ
    import settings
    setup_environ(settings)
    
from django.template.loader import render_to_string

from project.models import Project, ProjectDoc, PROJECT_UPLOAD_DIR
from settings import STATIC_SITE_DIRECTORY, MEDIA_ROOT
import shutil
import datetime

def dashes(): print '-' * 40
def msgt(m): dashes(); print m; dashes()

def write_page(fname, content, dirname=''):
    
    fname = os.path.join(dirname, fname)
    open(fname, 'w').write(content)
    print 'page written: %s' % fname
        
        
def make_pages():
    global STATIC_SITE_DIRECTORY
    
    dirname = 'docs_%s' % (datetime.datetime.now().strftime('%Y-%m%d_%I-%M-%p'))
    dirname = os.path.join(STATIC_SITE_DIRECTORY, dirname)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
        print 'directory created: %s' % dirname

    #-----------------------
    # Make detail pages
    #-----------------------
    cnt = 0
    for project in Project.objects.all():
        cnt +=1
        print '\n(%s) create project page for %s' % (cnt, project.name)
        content = render_to_string('static_site/static_project_detail.html', { 'p': project })
        write_page(project.get_html_filename(), content, dirname)

    #-----------------------
    # Make index page
    #-----------------------
    print '\n(%s) create project index page' % (cnt)
    content = render_to_string('static_site/static_project_list.html', { 'project_list': Project.objects.all() })
    write_page('index.html', content, dirname)

    #-----------------------
    # Copy over static media
    #-----------------------
    msgt('copy media files and project docs')
    for item in os.listdir(MEDIA_ROOT):
        fullname = os.path.join(MEDIA_ROOT, item)
        if os.path.isdir(fullname):
            print 'source', fullname
            print 'dest', os.path.join(dirname, item)
            shutil.copytree(fullname, os.path.join(dirname, item))
    
   
    
    
if __name__=='__main__':
    make_pages()
   