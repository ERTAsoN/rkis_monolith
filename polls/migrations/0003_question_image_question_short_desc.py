# Generated by Django 5.1.2 on 2024-12-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_total_votes_question_voters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='question',
            name='short_desc',
            field=models.CharField(default='text', max_length=200, verbose_name='Краткое описание'),
        ),
    ]
