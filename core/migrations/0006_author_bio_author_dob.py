# Generated by Django 4.1.7 on 2023-03-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
