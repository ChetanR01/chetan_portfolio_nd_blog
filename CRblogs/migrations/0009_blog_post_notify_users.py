# Generated by Django 4.0.6 on 2022-10-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRblogs', '0008_blog_post_keywords_alter_blog_post_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='notify_users',
            field=models.BooleanField(default=True),
        ),
    ]
