# Generated by Django 2.1.3 on 2018-11-19 01:15

import django.db.models.deletion
import tagulous.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181118_1950'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Author'),
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='blog.SiteTags'),
        ),
    ]
