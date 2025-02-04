from profiles.models import Profile, ProfileStatus
from rest_framework import serializers


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    profile_picture = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'location', 'birth_date', 'profile_picture']
        
class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        
        

class ProfileStatusSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user_profile.user.username', read_only=True)
    
    class Meta:
        model = ProfileStatus
        fields = ['id', 'user', 'status_content', 'created_at', 'updated_at']