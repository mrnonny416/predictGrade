# Generated by Django 3.2 on 2021-09-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictApp', '0010_menu_subject_img_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False)),
                ('department_id', models.CharField(max_length=20)),
                ('department_name', models.CharField(max_length=124)),
                ('start_CharField', models.IntegerField(max_length=4)),
                ('end_CharField', models.IntegerField(max_length=4)),
            ],
        ),
    ]
