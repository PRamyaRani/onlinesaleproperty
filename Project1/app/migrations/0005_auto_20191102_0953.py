# Generated by Django 2.2.6 on 2019-11-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191030_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='APPART_NO',
            new_name='APPARTMENT_NO',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='EmployeeDOJ',
            new_name='EMPLOYEE_DOJ',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='Employeemail',
            new_name='EMPLOYEE_EMAIL',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='EmployeeQualification',
            new_name='EMPLOYEE_LOCATION',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='Employeename',
            new_name='EMPLOYEE_NAME',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='EmployeeRemarks',
            new_name='EMPLOYEE_QUAL',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='EmployeeRole',
            new_name='EMPLOYEE_REMARKS',
        ),
        migrations.RenameField(
            model_name='createemployeemodel',
            old_name='Employlocation',
            new_name='EMPLOYEE_ROLE',
        ),
        migrations.RemoveField(
            model_name='createemployeemodel',
            name='Employeeid',
        ),
        migrations.RemoveField(
            model_name='createemployeemodel',
            name='id',
        ),
        migrations.AddField(
            model_name='createemployeemodel',
            name='EMPLOYEE_ID',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
