# Generated by Django 3.1.3 on 2020-11-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_todo_user_pk'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='likedUser',
            field=models.IntegerField(default=True),
        ),
    ]
