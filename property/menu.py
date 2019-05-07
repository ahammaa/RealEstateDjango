# -*- coding: utf-8 -*-

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from .models import Property

class PropertyMenu(CMSAttachMenu):
    name = _("Property Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for prop in Property.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as first argument, a URL as
            # second argument and a (for this tree) unique id as third
            # argument.
            node = NavigationNode(
                prop.name,
                reverse('property.views.home', args=(prop.pk,)),
                prop.pk
            )
            nodes.append(node)
        return nodes
#menu_pool.register_menu(PropertyMenu) # register the menu.