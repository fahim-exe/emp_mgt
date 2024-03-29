# Generated by Django 5.0.3 on 2024-03-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('Department_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Department_Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Employee_Name', models.CharField(max_length=100)),
                ('Employee_Dept', models.CharField(max_length=100)),
                ('Employee_DOJ', models.DateField()),
                ('Employee_PHOTO', models.CharField(max_length=100)),
            ],
        ),
    ]
