# Generated by Django 3.1.3 on 2021-02-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210211_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.CharField(default='commenter', max_length=200),
        ),
    ]
