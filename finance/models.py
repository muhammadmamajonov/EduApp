from django.db import models



PAYMENT_METHOD_CHOICES = (
    ("Naqd", "Naqd"),
    ("Paynet", "Paynet"),
    ("Payme", "Payme"),
    ("Click", "Click"),
    ("Terminal", "Terminal"),
    ("Bank", "Bank")
)

class Months(models.IntegerChoices):
    JAN = 1, "Yanvar"
    FEB = 2, "Fevral"
    MAR = 3, "Mart"

class Payments(models.Model):
    student = models.ForeignKey("school.Students",  on_delete=models.CASCADE, related_name='payments')
    group = models.ForeignKey("school.Groups", on_delete=models.CASCADE, related_name="payments")
    amount = models.PositiveIntegerField(null=False)
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=10)
    description = models.TextField()
    purpose = models.IntegerField()
    month = models.IntegerField(choices=Months.choices)

    class Meta:
        db_table = "payments"

    def __str__(self) -> str:
        return self.student.full_name

