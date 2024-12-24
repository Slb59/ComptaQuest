from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):

    class UserTypes(models.TextChoices):
        ACCOUTANT = 'accountant', 'Accountant'
        MEMBER = 'member', 'Member'
        SUPERMEMBER = 'supermember', 'Supermember'

    trigram = models.CharField(max_length=10, blank=False)
    usertype = models.CharField(max_length=30, choices=UserTypes.choices,
    default = UserTypes.MEMBER, blank=True)

    def __str__(self):
        return f"{self.pseudo}"
    
    class Meta:
        verbose_name_plural = "users"
        verbose_name = "user"
        ordering = ["-trigram"]
        indexes = [
            models.Index(fields=["-trigram"]),
        ]

class BaseUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(blank=True)

    class Meta:
        abstract = True

class MemberProfile(BaseUserProfile):
    """ specific data to member """
    ...

class Member(User):

    class Meta:
        proxy = True

    @property
    def profile(self):
        return self.MemberProfile

class MemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filer(user_type=User.UserTypes.MEMBER)