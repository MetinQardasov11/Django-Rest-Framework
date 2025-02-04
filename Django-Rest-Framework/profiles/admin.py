from django.contrib import admin
from .models import Profile, ProfileStatus
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'birth_date', 'profile_picture']
    
    
@admin.register(ProfileStatus)
class ProfileStatusAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'status_content', 'created_at', 'updated_at']