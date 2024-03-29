# Generated by Django 2.2.6 on 2019-10-30 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191030_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='plotno',
            new_name='APPART_NO',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='boundaries',
            new_name='BOUNDARIES',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='cstpersqyd',
            new_name='COST_PER_SQD',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='facing',
            new_name='FACING',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='expenses',
            new_name='Other_EXPENCES',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='roadno',
            new_name='ROAD_NO',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='status',
            new_name='STATUS',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='surveyno',
            new_name='SURVEY_NO',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='totalcost',
            new_name='TOTAL_COAST',
        ),
        migrations.RenameField(
            model_name='createappartmentmodel',
            old_name='totalsqyd',
            new_name='TOTAL_SQD',
        ),
    ]
