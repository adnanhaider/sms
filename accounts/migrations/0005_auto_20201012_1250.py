# Generated by Django 3.0.4 on 2020-10-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201012_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrstaff',
            name='photo',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='C:\\Users\\Adnan\\OneDrive\\Projects\\Python\\sms\\media%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='photo',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='C:\\Users\\Adnan\\OneDrive\\Projects\\Python\\sms\\media%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='photo',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='C:\\Users\\Adnan\\OneDrive\\Projects\\Python\\sms\\media%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='C:\\Users\\Adnan\\OneDrive\\Projects\\Python\\sms\\media%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='C:\\Users\\Adnan\\OneDrive\\Projects\\Python\\sms\\media%Y/%m/%d'),
        ),
    ]