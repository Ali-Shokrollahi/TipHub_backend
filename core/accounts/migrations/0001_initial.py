# Generated by Django 4.1.1 on 2022-09-19 10:42

import django.contrib.auth.validators
from django.db import migrations, models

import accounts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('STA', 'staff'), ('TEA', 'teacher'), ('STU', 'student')], default='STU', max_length=3, verbose_name='Role')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=32, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=32, verbose_name='last name')),
                ('phone_number', models.CharField(blank=True, max_length=11, verbose_name='phone number')),
                ('image', models.ImageField(blank=True, default='default_user.png', null=True, upload_to=accounts.models.rename_profile, verbose_name='image')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('email_verified', models.BooleanField(default=False, verbose_name='email_verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
    ]
