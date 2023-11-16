from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import AbstractUser, UserManager



class Roles(models.Model):
    """Foydalanuvchi rollari"""
    name = models.CharField(max_length=50)
    guard_name = models.CharField(max_length=50)
    carmodels = models.JSONField()

    class Meta:
        db_table = "roles"


class CustomUserManager(UserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        username = email
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        username = email
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
    

class Users(AbstractUser):
    # school = models.ForeignKey("school.Schools", on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    # role = models.ManyToManyField(Roles, null=True)
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = "users"

    
    def __str__(self) -> str:
        return self.username
    

class LoginHistory(models.Model):
    """Userlarning shaxsiy kabinetga kirish tarixi"""
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='login_history')
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