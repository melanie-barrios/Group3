from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id',models.UUIDField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('password',models.CharField()),
                ('name',models.CharField()),
                ('phone_number',models.CharField(max_length=11)),
                ('address',models.TextField()),
                ('email',models.TextField()),
            ],
        ),

    ]