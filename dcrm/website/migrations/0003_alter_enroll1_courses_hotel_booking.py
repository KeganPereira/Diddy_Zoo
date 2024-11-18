# Generated by Django 5.0.2 on 2024-11-18 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_enroll1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll1',
            name='courses',
            field=models.CharField(choices=[('4-12', 'courses age 4-12'), ('4-12', 'courses age 4-12'), ('4-12', 'courses age 4-12')], max_length=200),
        ),
        migrations.CreateModel(
            name='Hotel_Booking',
            fields=[
                ('booking_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('hotel_booking_date_arrive', models.DateField()),
                ('hotel_booking_date_leave', models.DateField()),
                ('hotel_booking_adults', models.IntegerField(default=0)),
                ('hotel_booking_children', models.IntegerField(default=0)),
                ('hotel_booking_old_oap', models.IntegerField(default=0)),
                ('hotel_total_cost', models.FloatField(default=0)),
                ('hotel_points', models.IntegerField(default=0)),
                ('hotel_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
