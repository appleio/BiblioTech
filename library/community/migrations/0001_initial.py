# Generated by Django 3.1.4 on 2021-01-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('privacy', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='private', max_length=64)),
            ],
        ),
    ]