# Generated by Django 3.2 on 2021-09-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictApp', '0008_alter_menu_subject_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_subject',
            name='menu_id',
            field=models.IntegerField(max_length=4),
        ),
    ]