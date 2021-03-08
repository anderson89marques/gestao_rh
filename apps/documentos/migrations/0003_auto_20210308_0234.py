# Generated by Django 3.1.7 on 2021-03-08 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20210308_0230'),
        ('documentos', '0002_documento_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
