# Generated by Django 4.0.3 on 2022-03-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_api', '0003_alter_flashcard_answer_alter_flashcard_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='answer',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='question',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='subject',
            field=models.TextField(max_length=255),
        ),
    ]
