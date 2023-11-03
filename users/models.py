from django.db import models
from school.models import Schools
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class Permissions(models.Model):
    """Platformadan foydalanish ruxsatlari"""
    name = models.CharField(max_length=50)
    guard_name = models.CharField(max_length=50)

    class Meta:
        db_table = "permissions"


class Roles(models.Model):
    """Foydalanuvchi rollari"""
    name = models.CharField(max_length=50)
    guard_name = models.CharField(max_length=50)
    carmodels = models.JSONField()

    class Meta:
        db_table = "roles"


class Users(AbstractUser):
    # username_validator = UnicodeUsernameValidator()
    # username = models.CharField(
    #     _("username"),
    #     max_length=150,
    #     unique=True,
    #     help_text=_(
    #         "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #     ),
    #     validators=[username_validator],
    #     error_messages={
    #         "unique": _("A user with that username already exists."),
    #     },
    # )

    # email = models.EmailField(max_length=254)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    role = models.ManyToManyField(Roles)

    class Meta:
        db_table = "users"

    
    def __str__(self) -> str:
        return self.username
    

class LoginHistory(models.Model):
    """Userlarning shaxsiy kabinetga kirish tarixi"""
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE, related_name='login_history')
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