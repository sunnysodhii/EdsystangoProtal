# Generated by Django 3.0.7 on 2020-08-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_attendance_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeeDate', models.DateField()),
                ('RegistrtionId', models.IntegerField()),
                ('StudentName', models.CharField(max_length=255)),
                ('StudentClass', models.CharField(max_length=255)),
                ('MonthlyFee', models.IntegerField()),
                ('AdmissionFee', models.IntegerField()),
                ('RegistrtionFee', models.IntegerField()),
                ('PreviousBalance', models.IntegerField()),
                ('DiscountFee', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('Deposit', models.IntegerField()),
                ('DueBalance', models.IntegerField()),
            ],
        ),
    ]
