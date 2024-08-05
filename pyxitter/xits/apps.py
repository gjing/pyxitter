from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class XitsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pyxitter.xits"
    verbose_name = _("Xits")
