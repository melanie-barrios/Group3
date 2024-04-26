# Generated by Django 5.0.4 on 2024-04-25 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=120)),
                ('course_term', models.CharField(choices=[('F', 'Fall'), ('W', 'Winter'), ('Sp', 'Spring'), ('Su', 'Summer')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=75)),
                ('phone_number', models.CharField(max_length=11)),
                ('address', models.TextField()),
                ('email', models.TextField()),
                ('type', models.CharField(choices=[('S', 'Supervisor'), ('I', 'Instructor'), ('T', 'TA')], default='Supervisor', max_length=10)),
                ('skills', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('section_id', models.IntegerField(primary_key=True, serialize=False)),
                ('section_number', models.IntegerField()),
                ('Time', models.TextField()),
                ('Location', models.TextField()),
                ('credits', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TA_APP.course')),
                ('instructor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.user')),
            ],
        ),
        migrations.CreateModel(
            name='LabSection',
            fields=[
                ('section_id', models.IntegerField(primary_key=True, serialize=False)),
                ('section_number', models.IntegerField()),
                ('Time', models.TextField()),
                ('Location', models.TextField()),
                ('Type', models.CharField(choices=[('L', 'Lab'), ('D', 'Discussion'), ('G', 'Grader')], default='Lab', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TA_APP.course')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TA_APP.coursesection')),
                ('ta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='TA_APP.user'),
        ),
    ]
