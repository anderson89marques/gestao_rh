# Generated by Django 3.1.7 on 2021-03-08 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0002_auto_20210308_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
