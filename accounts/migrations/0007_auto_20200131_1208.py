# Generated by Django 3.0 on 2020-01-31 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0006_auto_20200131_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='profile_pic',
            field=models.ImageField(default='https://drive.google.com/open?id=16ZU24pGnhv3UUrdbb6vQSagFGiKHLMWX', upload_to=''),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
