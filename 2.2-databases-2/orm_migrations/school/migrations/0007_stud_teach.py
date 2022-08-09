# Generated by Django 4.0.3 on 2022-08-09 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stud_Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud', to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud', to='school.teacher')),
            ],
        ),
    ]
