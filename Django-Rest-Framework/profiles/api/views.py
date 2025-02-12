from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework import generics
from rest_framework.filters import SearchFilter

from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializers,\
    ProfileStatusSerializer, ProfilePhotoSerializer

from .permissions import IsOwnerOrReadOnly, StatusOwnerOrReadOnly

class ProfileViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        GenericViewSet
    ):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['location']
    
    
class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, StatusOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
        
        
class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user.profile