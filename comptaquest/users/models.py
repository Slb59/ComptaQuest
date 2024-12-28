from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CQUser(auth_models.AbstractUser):

    class UserTypes(models.TextChoices):
        ACCOUTANT = 'accountant', 'Accountant'
        MEMBER = 'member', 'Member'
        SUPERMEMBER = 'supermember', 'Supermember'

    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_("email address"), unique=True)
    trigram = models.CharField(max_length=5, blank=False)
    usertype = models.CharField(max_length=30, choices=UserTypes.choices,
        default = UserTypes.MEMBER, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [trigram]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.trigram}"
    
    class Meta:
        verbose_name_plural = "users"
        verbose_name = "user"
        ordering = ["-trigram"]
        indexes = [
            models.Index(fields=["-trigram"]),
        ]

class BaseUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True, upload_to='profile_images')

    class Meta:
        abstract = True

class MemberProfile(BaseUserProfile):
    """ specific data to member """
    ...

class MemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=User.UserTypes.MEMBER)

class Member(CQUser):

    class Meta:
        proxy = True

    @property
    def profile(self):
        return self.memberprofile
    
    objects = MemberManager()

