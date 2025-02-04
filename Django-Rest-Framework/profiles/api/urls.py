from django.urls import path
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, ProfilePhotoUpdateView
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'status', ProfileStatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('profile-photo/', ProfilePhotoUpdateView.as_view(), name='photo-update')
]