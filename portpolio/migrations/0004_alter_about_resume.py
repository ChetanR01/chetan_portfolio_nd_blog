# Generated by Django 4.0.6 on 2022-10-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portpolio', '0003_delete_review_delete_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='resume',
            field=models.CharField(max_length=300),
        ),
    ]