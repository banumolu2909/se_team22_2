# Generated by Django 4.1.7 on 2023-04-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_instructor_otp_digit_instructor_verify_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='otp_digit',
        ),
        migrations.RemoveField(
            model_name='student',
            name='verify_status',
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
