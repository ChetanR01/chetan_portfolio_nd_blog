# Generated by Django 4.0.6 on 2022-10-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRblogs', '0006_remove_blog_post_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='post_url',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
