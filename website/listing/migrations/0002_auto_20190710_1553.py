# Generated by Django 2.2.3 on 2019-07-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='topic_text',
            field=models.TextField(),
        ),
    ]
