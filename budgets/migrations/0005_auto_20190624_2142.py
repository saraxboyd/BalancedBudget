# Generated by Django 2.1.7 on 2019-06-24 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_auto_20190624_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='limit',
            old_name='categroy',
            new_name='category',
        ),
    ]