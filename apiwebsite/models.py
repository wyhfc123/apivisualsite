from django.db import models

# Create your models here.
class DataNumber(models.Model):
    number=models.CharField(max_length=20,verbose_name="图表数据")
    class Meta:
        db_table='data_number'
        verbose_name="动态数据表"
        verbose_name_plural=verbose_name
class CurrentNumber(models.Model):
    currentNumber=models.CharField(max_length=20,verbose_name="当前数据")

    class Meta:
        db_table = 'current_number'
        verbose_name = "当前数据表"
        verbose_name_plural = verbose_name