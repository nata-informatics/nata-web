# Generated by Django 2.1.1 on 2019-06-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='no_telp',
            field=models.CharField(max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tanggal_lahir',
            field=models.DateField(null=True),
        ),
    ]