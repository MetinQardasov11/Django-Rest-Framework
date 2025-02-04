from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile, ProfileStatus

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance)
        
        
@receiver(post_save, sender=Profile)
def create_profile_status(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(
            user_profile = instance,
            status_content = f'{instance.user.username} joined the network.'
        )