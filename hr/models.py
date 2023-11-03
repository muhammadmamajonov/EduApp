from django.db import models
from administration.models import Organizations


class Staffs(models.Model):
    full_name = models.CharField(max_length=100, db_column='name')
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    birthdate = models.DateField(db_column='year')
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
    