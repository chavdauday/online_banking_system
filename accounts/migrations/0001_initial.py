# Generated by Django 4.0.3 on 2022-03-31 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('mobile', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('address', models.TextField(default='Address not given')),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
