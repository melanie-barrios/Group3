from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):

    dependencies = ['TA_APP','0003_ta.py','0004_courses.py']

    operations = [
        migrations.CreateModel(
            name='LabSection',
            fields=[
                ('course_id',models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.Course')),
                ('course_code',models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.Course')),
                ('lab_id',models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.Course')),
                ('ta_id',models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.TA')),
            ],
        ),

    ]