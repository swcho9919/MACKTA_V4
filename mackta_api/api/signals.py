from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from mackta_api.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        User.objects.create(user=instance)