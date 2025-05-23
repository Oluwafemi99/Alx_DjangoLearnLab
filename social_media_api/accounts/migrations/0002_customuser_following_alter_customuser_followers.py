# Generated by Django 5.1.7 on 2025-03-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(related_name='user_following', to='accounts.customuser'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(related_name='user_followers', to='accounts.customuser'),
        ),
    ]
