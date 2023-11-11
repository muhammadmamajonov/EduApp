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
    number = models.CharField(max_length=10, null=False)
    capacity = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = "rooms"
    
    def __str__(self):
        return self.number


class Courses(models.Model):
    """O'qitiladigan yo'nalishlar"""
   
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    text_price = models.CharField("Kurs narxi(yozuv bilan)", max_length=100)
    status = models.BooleanField(default=True)
    for_bot = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    about = models.TextField("Kurs xaqtida")
    code_for_certificate  = models.CharField("sartifikat uchun maxsus kod", max_length=50)
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


#     status character varying(255) NOT NULL,
#  

#     school_id integer DEFAULT 1 NOT NULL,


class KeldiKetdi(models.Model): #bunga mos inglizcha nom topilmadi. eng yaqini 'attendance' lekin to'liq qamrab ololmaydi nazdimda
    """Xodim va o'quvchilarning binoga kelish va ketishlari"""
    person_id = models.PositiveIntegerField(null=False)
    full_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=3, choices=(("in", "in"), ("out", "out")))
    event_datetime = models.TimeField(null=False, auto_now_add=True)
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, related_name='keldi_ketdi')

    class Meta:
        db_table = "keldi_ketdi"
    
    def __str__(self) -> str:
        return self.full_name + " | " + self.event_type



