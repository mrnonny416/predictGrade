# Generated by Django 3.2 on 2021-09-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictApp', '0006_delete_subject_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu_subject',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False)),
                ('menu_id', models.IntegerField(max_length=4)),
                ('subjectID', models.CharField(max_length=20)),
            ],
        ),
    ]
