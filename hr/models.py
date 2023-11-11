from django.db import models
from administration.models import Organizations


class Staffs(models.Model):
    full_name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    birthdate = models.DateField()
    image = models.ImageField(upload_to="staffs")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=17)
    passport = models.CharField(max_length=10)
    idcard = models.CharField(max_length=20)
    # school = models.ForeignKey(Schools, on_delete=models.CASCADE) #o'chirib tashlash kerak

    class Meta:
        db_table = "staffs"

    def __str__(self) -> str:
        return self.full_name
    