# Generated by Django 5.0.7 on 2024-07-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
                ('basic', models.CharField(max_length=50)),
                ('intermediate', models.CharField(max_length=50)),
                ('advance', models.CharField(max_length=50)),
            ],
        ),
    ]