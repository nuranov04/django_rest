# Generated by Django 3.2 on 2021-07-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210714_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
