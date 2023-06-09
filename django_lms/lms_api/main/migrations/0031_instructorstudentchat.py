# Generated by Django 4.1.7 on 2023-04-21 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_delete_instructorstudentchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorStudentChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_text', models.TextField()),
                ('msg_from', models.CharField(max_length=100)),
                ('msg_time', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name_plural': '7. Instructor Student Messages',
            },
        ),
    ]
