# Generated by Django 4.1.7 on 2023-04-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_add_prompt_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='message',
            name='tokens',
            field=models.IntegerField(default=0),
        ),
    ]
