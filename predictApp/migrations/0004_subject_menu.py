# Generated by Django 3.2 on 2021-09-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictApp', '0003_auto_20210813_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(max_length=4)),
                ('subjectID', models.CharField(max_length=20)),
            ],
        ),
    ]