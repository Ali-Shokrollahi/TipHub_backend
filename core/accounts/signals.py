from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import StaffProfile, StudentProfile, TeacherProfile

from .models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "STU":
            StudentProfile.objects.create(user=instance)

        elif instance.role == "TEA":
            TeacherProfile.objects.create(user=instance)

        elif instance.role == "STA":
            StaffProfile.objects.create(user=instance)
        else:
            pass
