from django import template
from django.template import loader
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def responsive_table(context, table_id, url, refresh_interval=500, table_template='django_responsive_tables2/basic_table.html', *args, **kwargs):
    table_template = loader.get_template(table_template)
    context.push(table_url=reverse(url, args=args, kwargs=kwargs), table_id=table_id, refresh_interval=refresh_interval)
    return table_template.render(context.flatten())
