# Generated by Django 2.2.6 on 2019-10-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAppartmentModel',
            fields=[
                ('plotno', models.IntegerField(primary_key=True, serialize=False)),
                ('roadno', models.IntegerField()),
                ('surveyno', models.IntegerField()),
                ('cstpersqyd', models.IntegerField()),
                ('totalsqyd', models.IntegerField()),
                ('expenses', models.IntegerField()),
                ('boundaries', models.IntegerField()),
                ('facing', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('totalcost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CreateEmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employeename', models.CharField(max_length=30)),
                ('Employeeid', models.IntegerField()),
                ('Employeemail', models.EmailField(max_length=254)),
                ('Employlocation', models.CharField(max_length=20)),
                ('EmployeeDOJ', models.IntegerField()),
                ('EmployeeRole', models.CharField(max_length=20)),
                ('EmployeeQualification', models.CharField(max_length=20)),
                ('EmployeeRemarks', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CreatePlotModel',
            fields=[
                ('plotno', models.IntegerField(primary_key=True, serialize=False)),
                ('roadno', models.IntegerField()),
                ('surveyno', models.IntegerField()),
                ('cstpersqyd', models.IntegerField()),
                ('totalsqyd', models.IntegerField()),
                ('expenses', models.IntegerField()),
                ('boundaries', models.IntegerField()),
                ('facing', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('totalcost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginAdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('upwd', models.CharField(max_length=30)),
            ],
        ),
    ]
