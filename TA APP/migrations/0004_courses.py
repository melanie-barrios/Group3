from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):

    dependencies = ['TA APP','0002_instructor.py']

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id',models.CharField(primary_key=True)),
                ('course_name',models.CharField(max_length=120)),
                ('course_code',models.IntegerField()),
                ('instructor_id',models.ForeignKey(null=True,on_delete=django.db.models.deletion.CASCADE,to='TA APP.Instructor')),
                ('lab_id',models.IntegerField()),
            ],
        ),

    ]