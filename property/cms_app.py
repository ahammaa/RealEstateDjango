# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_property import apphook_property
from property.menu import PropertyMenu
from django.utils.translation import ugettext_lazy as _

class PropertyApp(CMSApp):
    name = _("Property App") # give your app a name, this is required
    urls = ["property.urls"] # link your app to url configuration(s)
    menus = [PropertyMenu] # attach a CMSAttachMenu to this apphook.

apphook_property.register(PropertyApp) # register your app

