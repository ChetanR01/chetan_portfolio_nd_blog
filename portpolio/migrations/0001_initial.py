# Generated by Django 4.0.6 on 2022-09-18 18:04

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='img')),
                ('degree', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('Mobile_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='doc')),
                ('other', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_percentage', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('project_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='project_img')),
                ('desc', models.CharField(max_length=100)),
                ('code_link', models.CharField(max_length=200)),
                ('view_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ico_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
