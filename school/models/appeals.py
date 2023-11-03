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
    ("Reception", "Reception")
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