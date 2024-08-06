import random
import string

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ManyToManyField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for pyxitter.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    def generate_handle():
        return "".join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits  # noqa: COM812
            )
            for _ in range(32)
        )

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    handle = CharField(
        _("Handle of User"),
        blank=False,
        max_length=64,
        unique=True,
        default=generate_handle,
    )
    followers = ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
    )
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
