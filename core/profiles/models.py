from utils.models import TimeStampedModel
from django.db import models


class StudentProfile(TimeStampedModel):
    user = models.OneToOneField(to="accounts.User", on_delete=models.CASCADE, primary_key=True)

    # interest field will be here

    def __str__(self):
        return self.user.email


class TeacherProfile(TimeStampedModel):
    user = models.OneToOneField(to="accounts.User", on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.email


class StaffProfile(TimeStampedModel):
    user = models.OneToOneField(to="accounts.User", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.email
