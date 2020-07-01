# Generated by Django 3.0.5 on 2020-06-17 18:27

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'User',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=20)),
                ('street_number', models.CharField(max_length=20)),
                ('town', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('birth_date', models.DateField()),
                ('contact_number', models.CharField(max_length=11)),
                ('address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'parent',
                'verbose_name_plural': 'parents',
                'db_table': 'Parent',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('birth_date', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('salary', models.FloatField(max_length=6)),
                ('contact_number', models.CharField(max_length=11)),
                ('address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('birth_date', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('roll_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('gaurdian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Parent')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('birth_date', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('salary', models.FloatField(max_length=6)),
                ('contact_number', models.CharField(max_length=11)),
                ('address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'principal',
                'verbose_name_plural': 'principals',
                'db_table': 'Principal',
            },
        ),
        migrations.CreateModel(
            name='HrStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('birth_date', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('salary', models.FloatField(max_length=6)),
                ('contact_number', models.CharField(max_length=11)),
                ('address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'hr staff',
                'verbose_name_plural': 'hr staff',
                'db_table': 'HrStaff',
            },
        ),
    ]
