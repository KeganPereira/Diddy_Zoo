# Generated by Django 5.0.2 on 2024-11-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_enroll1_courses_zoo_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_card', models.CharField(blank=True, max_length=200)),
                ('card_number', models.CharField(max_length=200)),
                ('cvv_number', models.CharField(max_length=200)),
                ('expiry_date', models.CharField(max_length=200)),
            ],
        ),
    ]
