from rest_framework import serializers

from pyxitter.xits.models import Xit


class XitSerializer(serializers.ModelSerializer[Xit]):
    class Meta:
        model = Xit
        fields = [
            "xit",
            "user",
            "media",
            "parent",
            "rexit",
            "views",
            "created_at",
            "updated_at",
        ]
