# Generated by Django 5.1.2 on 2024-10-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccname', models.CharField(blank=True, max_length=100, null=True)),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='category_images')),
                ('cdesc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
