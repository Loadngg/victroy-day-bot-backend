from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from backend.views import RegionList, PathList, PlaceDetail, TeamCreate, TeamPlaceAnswerCreate, TeamPlaceAnswerUpdate

urlpatterns = [
    path('region/', RegionList.as_view(), name='get_regions'),
    path('path/<int:region_id>/', PathList.as_view(), name='get_path-by_region_id'),
    path('place/<int:pk>/', PlaceDetail.as_view(), name='get_place_by_id'),
    path('team/', TeamCreate.as_view(), name='create-team'),
    path('answer/', TeamPlaceAnswerCreate.as_view(), name='create-answer'),
    path('answer/<int:pk>', TeamPlaceAnswerUpdate.as_view(), name='update-answer'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
