from django.db import models


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

class Students(models.Model):
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
    
    # debt bigint,
    # start_date date,
    # test_status character varying(255),
    # sale_manager_id integer,
    # personal_manager_id integer

