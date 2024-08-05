from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin

from pyxitter.xits import models

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]


class XitAdmin(models.Xit):
    pass
