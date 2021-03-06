# Generated by Django 3.0.7 on 2020-06-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20200614_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('joining_date', models.DateField()),
                ('emp_type', models.CharField(choices=[('---Employee Type---', '---Employee Type---'), ('Teaching Staff', 'Teaching Staff'), ('Non-Teaching', 'Non-Teaching')], default='---Employee Type---', max_length=20)),
            ],
        ),
    ]
