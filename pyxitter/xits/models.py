import django.contrib.postgres.fields as pg_field
from django.db import models

from pyxitter.users.models import User


class Xit(models.Model):
    xit = models.TextField()
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    media = pg_field.ArrayField(models.CharField(), size=8)
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="replies",
    )
    rexit = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="rexits",
    )
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} : {self.xit}"
