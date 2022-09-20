from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimeStampedModel


class StudentProfile(TimeStampedModel):
    user = models.OneToOneField(to="accounts.User", on_delete=models.CASCADE, primary_key=True)

    # interest field will be here

    def __str__(self):
        return self.user.email


class TeacherProfile(TimeStampedModel):
    user = models.OneToOneField(to="accounts.User", on_delete=models.CASCADE, primary_key=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=32, null=True, blank=True, unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": _("A user with that username already exists."),
                                },
                                )
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
