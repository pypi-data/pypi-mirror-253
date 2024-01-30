from django import template
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def include_static(file_path):
    # find the static file using django's finders
    if static_file := finders.find(file_path):
        # read the content of the static file
        with open(static_file, "r") as file:
            content = file.read()
        # return the content to be included in the template
        return mark_safe(content)
    # if the file was not found, return an empty string
    return ""
