# Generated by Django 3.0.7 on 2020-07-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_employee_emp_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_date', models.DateField()),
                ('income_description', models.TextField()),
                ('income_amount', models.IntegerField()),
            ],
        ),
    ]
