# Generated by Django 4.2.6 on 2023-10-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translateapp', '0002_alter_post_text_alter_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=250, verbose_name='text'),
        ),
    ]
