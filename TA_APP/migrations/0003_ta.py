from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):

    dependencies = ['TA_APP','0001_Users.py']

    operations = [
        migrations.CreateModel(
            name='TA',
            fields=[
                ('user_id',models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_APP.Users')),
                ('ta_id',models.IntegerField(primary_key=True)),
            ],
        ),

    ]