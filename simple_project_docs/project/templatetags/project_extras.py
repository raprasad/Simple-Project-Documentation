from django.core.validators import email_re
from django import template

register = template.Library()

@register.filter(name='mail_links')
def mail_links(value, arg=None):
    replace_dict = {}
    for chunk in value.split():
        if email_re.match(chunk):
            replace_dict.update({chunk : '<a href="mailto:%s">%s</a>' % (chunk, chunk) })

    for k, v in replace_dict.iteritems():
        value = value.replace(k, v)
    return value