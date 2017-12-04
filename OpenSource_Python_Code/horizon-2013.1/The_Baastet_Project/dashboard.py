from django.utils.translation import ugettext_lazy as _

import horizon


class The_Baastet_Project(horizon.Dashboard):
    name = _("The_Baastet_Project")
    slug = "the_baastet_project"
    panels = ()  # Add your panels here.
    default_panel = ''  # Specify the slug of the dashboard's default panel.


horizon.register(The_Baastet_Project)
