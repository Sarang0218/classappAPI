# Generated by Django 4.0.5 on 2022-08-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_groupchat_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
