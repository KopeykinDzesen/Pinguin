# Generated by Django 2.0.2 on 2018-02-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email_is_active',
            field=models.CharField(default=None, max_length=20),
        ),
    ]