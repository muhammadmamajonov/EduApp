from django.db import models


LESSON_TIME_CHOICES = (
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Evening", "Evening")
)

COMPUTER_KNOWLEDGE_CHOICES = (
    ("0", "Umuman bilmayman"),
    ("1", "O'rtacha bilaman"),
    ("2", "Yaxshi bilaman")
)

PROGRAMMING_KNOWLEDGE_CHOICES = (
    ("0", "Umuman tushuncha yo'q"),
    ("1", "Ozroq xabari bor"),
    ("2", "Kod yoza oladi")
)

DIRECTION_CHOICES = (
    ("Programming", "Programming"),
    ("Design", "Design")
)

FILLER_CHOICES = (
    ("Reception", "Reception"),
    ("Self", "Self")
)


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

class Appeals(models.Model):
    full_name = models.CharField("Arizachining ism-familyasi", max_length=50)
    phone = models.CharField("Telefon raqami", max_length=17)
    address = models.CharField("Manzili", max_length=100)
    study_or_work_place = models.CharField("Ish yoki o'qish joyi", max_length=50) # ?
    lesson_time = models.CharField(choices=LESSON_TIME_CHOICES, max_length=15)
    computer_knowledge = models.CharField("Komputerdan bilimi", max_length=1, choices=COMPUTER_KNOWLEDGE_CHOICES)
    programming_knowledge = models.CharField("Dasturlash tushunchasi", max_length=1, choices=PROGRAMMING_KNOWLEDGE_CHOICES)
    has_computer = models.BooleanField("Shaxsiy kompyuteri bormi", default=False)
    direction = models.CharField("Yo'nalish", max_length=15, choices=DIRECTION_CHOICES)
    filler = models.CharField("Anketani to'ldiruvchi", max_length=20, choices=FILLER_CHOICES)



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
    """O'quv markaz O'qituvchilari"""
    staff = models.ForeignKey("hr.Staffs", on_delete=models.CASCADE)
    specialty = models.ManyToManyField("administration.Specializations", verbose_name="Mutaxassisliklari", related_name="teachers")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name="teachers")

    class Meta:
        db_table = "teachers"



class Groups(models.Model):
    """O'quv markazdagi guruhlar"""
    name = models.CharField(max_length=50)
    course = models.ForeignKey("administration.Courses", on_delete=models.CASCADE, related_name="groups")
    teacher = models.ForeignKey(Teachers, verbose_name="Guruh o'qituvchisi", on_delete=models.CASCADE, related_name="groups")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=GROUP_STATUS_CHOICES)
    room = models.ForeignKey("administration.Rooms", verbose_name="Dars o'tiladigan xona", on_delete=models.CASCADE, related_name="groups")
    lesson_time = models.TimeField("Dars vaqti")
    lesson_days = models.CharField(choices=LESSON_DAYS)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name="groups")

    class Meta:
        db_table = "groups"




class Students(models.Model):
    STUDY_PLACE_CHOICES = (
        ('school', 'school'),
        ('college', 'college'),
        ('university', 'university'),
        ('worker', 'worker')
    )

    GENDER_CHOICES = (
        ('M', 'Erkak'),
        ("F", "Ayol")
    )

    STUDENT_STATUS_CHOICES = (
        ('Studying', 'Studying'),
        ("Graduated", "Graduated"),
        ("Stopped", "Stopped")
    )
    full_name = models.CharField("ism-familya", max_length=100)
    phone = models.CharField(max_length=17)
    birthdate = models.DateField("Tug'gilgan sana")
    district = models.ForeignKey("administration.Districts", verbose_name="Tuman", on_delete=models.CASCADE, related_name="students")
    group = models.ForeignKey("school.Groups", verbose_name="Guruhi", on_delete=models.CASCADE, related_name='students')
    address = models.CharField("Manzili", max_length=100)
    study_place = models.CharField(choices=STUDY_PLACE_CHOICES, max_length=15)
    gender = models.CharField("Jinsi", max_length=1, choices=GENDER_CHOICES)
    passport = models.CharField("Pasport seria va raqami", max_length=20)
    leaved_at = models.DateField(null=True, blank=True)
    graduated_at = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STUDENT_STATUS_CHOICES, max_length=20)
    first_month_price = models.PositiveIntegerField()
    workplace_after_graduation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="students")
    qr_code = models.ImageField(upload_to="students/qr_codes")
    
    class Meta:
        db_table = "students"

    def __str__(self) -> str:
        return self.full_name