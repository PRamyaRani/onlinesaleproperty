from django.db import models


# Create your models here.

class CreatePlotModel(models.Model):
    PLOT_NO = models.IntegerField(primary_key=True)
    ROAD_NO = models.IntegerField()
    SURVEY_NO = models.IntegerField()
    COST_PER_SQD = models.IntegerField()
    TOTAL_SQD = models.IntegerField()
    Other_EXPENCES = models.IntegerField()
    BOUNDARIES = models.IntegerField()
    FACING = models.CharField(max_length=20)
    STATUS = models.CharField(max_length=20)
    TOTAL_COAST = models.IntegerField()

class CreateEmployeeModel(models.Model):
    EMPLOYEE_NAME = models.CharField(max_length=30)
    EMPLOYEE_ID = models.IntegerField(primary_key=True)
    EMPLOYEE_EMAIL = models.EmailField()
    EMPLOYEE_LOCATION = models.CharField(max_length=20)
    EMPLOYEE_DOJ = models.IntegerField()
    EMPLOYEE_ROLE = models.CharField(max_length=20)
    EMPLOYEE_QUAL = models.CharField(max_length=20)
    EMPLOYEE_REMARKS = models.CharField(max_length=20)

class CreateAppartmentModel(models.Model):
    APPARTMENT_NO = models.IntegerField(primary_key=True)
    ROAD_NO = models.IntegerField()
    SURVEY_NO = models.IntegerField()
    COST_PER_SQD = models.IntegerField()
    TOTAL_SQD = models.IntegerField()
    Other_EXPENCES = models.IntegerField()
    BOUNDARIES = models.IntegerField()
    FACING = models.CharField(max_length=20)
    STATUS = models.CharField(max_length=20)
    TOTAL_COAST = models.IntegerField()


