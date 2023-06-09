# Generated by Django 4.0.3 on 2022-04-01 05:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(default='C:\\Users\\devoz\\PycharmProjects\\Online_Banking_System\\media\\default.jpg', upload_to='profile_images'),
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('CURRENT', 'Current'), ('SAVING', 'Saving'), ('SALARY', 'Salary'), ('FIXED_DEPOSITE', 'Fixed Deposite'), ('RECURRING_DEPOSITE', 'Recurring Deposite')], max_length=20)),
                ('account_no', models.PositiveIntegerField(unique=True)),
                ('IFSC_Code', models.CharField(max_length=10, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('Minimum_Balance', models.DecimalField(decimal_places=2, default=3000, max_digits=4)),
                ('created_on', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
