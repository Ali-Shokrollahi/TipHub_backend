import os
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimeStampedModel

from .managers import StaffManager, StudentManager, TeacherManager, UserManager


def rename_profile(instance, filename):
    upload_to = "profiles"
    ext = filename.split(".")[-1]
    # get filename
    if instance:
        filename = "{}.{}".format(instance.email, ext)
    else:
        # set filename as random string
        filename = "{}.{}".format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    A custom user model that uses email for authentication instead of username.
    """

    class Role(models.TextChoices):
        STAFF = "STA", "staff"
        TEACHER = "TEA", "teacher"
        STUDENT = "STU", "student"

    base_type = Role.STUDENT

    role = models.CharField(_("Role"), max_length=3, choices=Role.choices, default=Role.STUDENT)
    # authentication field
    email = models.EmailField(_("email address"), unique=True)
    # fields
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=32, unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": _("A user with that username already exists."),
                                },
                                )

    first_name = models.CharField(_("first name"), max_length=32, blank=True)
    last_name = models.CharField(_("last name"), max_length=32, blank=True)
    phone_number = models.CharField(_("phone number"), max_length=11, blank=True)
    image = models.ImageField(_("image"), upload_to=rename_profile, default="default_user.png", null=True, blank=True)
    # authorization fields
    is_active = models.BooleanField(_("active"), default=False)
    email_verified = models.BooleanField(_("email_verified"), default=False)

    # config
    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def is_staff(self):
        if self.role == self.Role.STAFF:
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class Student(User):
    # This sets the user type to STUDENT during record creation
    base_type = User.Role.STUDENT
    # Ensure queries on the Student model return only Student
    objects = StudentManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.staffprofile


class Teacher(User):
    # This sets the user type to TEACHER during record creation
    base_type = User.Role.TEACHER
    # Ensure queries on the Teacher model return only Teachers
    objects = TeacherManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.teacherprofile


class Staff(User):
    # This sets the user type to TEACHER during record creation
    base_type = User.Role.STAFF
    # Ensure queries on the Teacher model return only Teachers
    objects = StaffManager()

    class Meta:
        proxy = True

    @property
    def extra(self):
        return self.staffprofile
