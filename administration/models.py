from django.db import models

class Specializations(models.Model):
    """O'qitiladigan mutaxassislik yo'nalishlari"""
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'specializations'

    def __str__(self):
        return self.name


class Districts(models.Model):
    """Tuman va shaxarlar"""
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "districts"
    
    def __str__(self):
        return self.name


class Rooms(models.Model):
    """O'quv Xonalar"""
    number = models.CharField(max_length=10, db_column='room_number')
    capacity = models.PositiveSmallIntegerField(db_column='room_capacity')

    class Meta:
        db_table = "rooms"
    
    def __str__(self):
        return self.number


class Courses(models.Model):
    """O'qitiladigan yo'nalishlar"""
   
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    text_price = models.CharField("Kurs narxi(yozuv bilan)", max_length=100, db_column='price_as_text')
    status = models.BooleanField(default=True)
    for_bot = models.BooleanField(default=False, db_column='is_for_bot')
    description = models.CharField(max_length=200)
    about = models.TextField("Kurs xaqtida", db_column='body')
    code_for_certificate  = models.CharField("sartifikat uchun maxsus kod", max_length=50, db_column='code')
    image = models.ImageField(upload_to="courses", height_field=None, width_field=None, max_length=None)

    class Meta:
        db_table = "courses"
    
    def __str__(self):
        return self.name


class Organizations(models.Model):
    """Tashkilotlar"""
    name = models.CharField(max_length=100)
    # school = models.ForeignKey(Schools, on_delete=models.CASCADE) o'chirib tashlash kerak

    class Meta:
        db_table = 'organizations'
 
    def __str__(self) -> str:
        return self.name


# class DjangoMigrations(models.Model):
#     id = models.IntegerField()
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         db_table = "django_migrations"

