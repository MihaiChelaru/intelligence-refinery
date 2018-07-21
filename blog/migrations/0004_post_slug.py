# Generated by Django 2.0.7 on 2018-07-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_blurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='new-beginning', help_text='Hyphen-separated string of keywords for SEO', max_length=40),
            preserve_default=False,
        ),
    ]
