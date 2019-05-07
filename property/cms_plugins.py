# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PropertyPlugin as PropertyPluginModel
from django.utils.translation import ugettext as _

class PropertyPlugin(CMSPluginBase):
    model = PropertyPluginModel # Model where data about this plugin is saved
    name = _("Property Plugin") # Name of the plugin
    render_template = "propertyhome.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(PropertyPlugin) # register the plugin