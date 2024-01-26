from .. import app_settings as app_sett
from django import template

register = template.Library()


@register.simple_tag
def invoice_app_name():
    return app_sett.INVOICES_APP_NAME
