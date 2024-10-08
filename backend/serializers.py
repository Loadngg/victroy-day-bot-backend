from rest_framework import serializers

from .models import Region, Path, Place, Team, TeamPlaceAnswer


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamPlaceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlaceAnswer
        fields = "__all__"
