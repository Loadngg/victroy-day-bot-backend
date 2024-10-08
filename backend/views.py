from rest_framework import generics

from backend.models import Region, Path, Place, TeamPlaceAnswer
from backend.serializers import RegionSerializer, PathSerializer, PlaceSerializer, TeamSerializer, \
    TeamPlaceAnswerSerializer


class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class PathList(generics.ListAPIView):
    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return Path.objects.filter(region_id=region_id)

    serializer_class = PathSerializer


class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class TeamCreate(generics.CreateAPIView):
    serializer_class = TeamSerializer


class TeamPlaceAnswerCreate(generics.CreateAPIView):
    serializer_class = TeamPlaceAnswerSerializer


class TeamPlaceAnswerUpdate(generics.UpdateAPIView):
    queryset = TeamPlaceAnswer.objects.all()
    serializer_class = TeamPlaceAnswerSerializer
