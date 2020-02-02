# Generated by Django 3.0 on 2020-02-01 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_remove_personalinfo_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='department',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='bank_account_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='bank_ifsc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Bank IFSC Code'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
