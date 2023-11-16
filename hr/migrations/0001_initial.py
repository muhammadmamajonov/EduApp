# Generated by Django 4.2.6 on 2023-11-14 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('image', models.ImageField(upload_to='staffs')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=17)),
                ('passport', models.CharField(max_length=10)),
                ('idcard', models.CharField(max_length=20)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.organizations')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
    ]
