# Generated by Django 3.2.15 on 2022-10-07 09:12

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='about project'),
        ),
    ]
