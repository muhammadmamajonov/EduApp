from django.db import models

STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive")
    )

GROUP_STATUS_CHOICES = (
    ("Active", "Active"),
    ("Graduated", "Graduated")
)

LESSON_DAYS = (
    ("MWF", "Dushanba-Chorshanba-Juma"),
    ("TTS", "Seshanba-Payshanba-Shanba"),
    ("every", "Har kuni")
)


class SchoolTypes(models.IntegerChoices):
        EDUAPP = 1, "EduAPP"
        DIGITAL_SCHOOL = 2, "Digital School"

class Schools(models.Model):
    """O'quv markazlari"""
    company_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)
    domain = models.URLField(max_length=200)
    address = models.CharField(max_length=255)
    director = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    school_type = models.IntegerField(choices=SchoolTypes.choices, default=SchoolTypes.DIGITAL_SCHOOL)
    district = models.ForeignKey("administration.Districts", on_delete=models.CASCADE)
    computers_qty = models.PositiveSmallIntegerField("Informatika sinfi kompyuterlari soni", default=0)

    class Meta:
        db_table = "schools"
    
    def __str__(self) -> str:
        return self.company_name
    

class Teachers(models.Model):
    staff = models.ForeignKey("hr.Staffs", on_delete=models.CASCADE)
    specialty = models.ManyToManyField("administration.Specialty", verbose_name="Mutaxassisliklari", related_name="teachers")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name="teachers")

    class Meta:
        db_table = "teachers"



class Group(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey("administration.Courses", on_delete=models.CASCADE, related_name="groups")
    teacher = models.ForeignKey(Teachers, verbose_name="Guruh o'qituvchisi", on_delete=models.CASCADE, related_name="groups")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=GROUP_STATUS_CHOICES)
    room = models.ForeignKey("administration.Rooms", verbose_name="Dars o'tiladigan xona", on_delete=models.CASCADE, related_name="groups")
    lesson_time = models.TimeField("Dars vaqti", db_column='time')
    lesson_days = models.CharField(choices=LESSON_DAYS, db_column='course_days')
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name="groups")






    


