# Generated by Django 3.2.4 on 2021-06-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examaltersys', '0004_grievances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answers_text',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='freqquestions',
            name='question_text',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
