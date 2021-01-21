# Generated by Django 3.1.4 on 2021-01-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_delete_book'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ManyToManyField(related_name='books', to='community.Library'),
        ),
    ]