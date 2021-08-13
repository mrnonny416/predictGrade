# Generated by Django 3.2 on 2021-08-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_refer',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False)),
                ('subjectID', models.CharField(max_length=20)),
                ('ref_subjectID', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='ref_subject',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='subjectID',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_instructor',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_name_eng',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_name_th',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
