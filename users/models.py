from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.apps import apps
from django.contrib.auth.models import User


# class Permissions(models.Model):
#     """Platformadan foydalanish ruxsatlari"""
#     name = models.CharField(max_length=50)
#     guard_name = models.CharField(max_length=50)

#     class Meta:
#         db_table = "permissions"


class Roles(models.Model):
    """Foydalanuvchi rollari"""
    name = models.CharField(max_length=50)
    guard_name = models.CharField(max_length=50)
    carmodels = models.JSONField()

    class Meta:
        db_table = "roles"


# class Users(AbstractUser):
#     school = models.ForeignKey("school.Schools", on_delete=models.CASCADE)
#     archived = models.BooleanField(default=False)
#     role = models.ManyToManyField(Roles)

#     class Meta:
#         db_table = "users"

    
#     def __str__(self) -> str:
#         return self.username
    

class LoginHistory(models.Model):
    """Userlarning shaxsiy kabinetga kirish tarixi"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    login_at = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(null=True)
    logout_at = models.DateTimeField(null=True, blank=True)
    ip = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

    class Meta:
        db_table = "login_history"

    def __str__(self) -> str:
        return self.user.username