# Generated by Django 4.0.3 on 2022-04-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_transections_show_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transections',
            name='account_no',
            field=models.BigIntegerField(),
        ),
    ]
