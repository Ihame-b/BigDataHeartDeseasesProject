from email import message
from django.db import models

class Data(models.Model):
    Age = models.CharField(max_length=255, default='SOME STRING')
    Sex = models.CharField(max_length=255, default='SOME STRING')
    Chestpaintype = models.CharField(max_length=255, default='SOME STRING')
    BP = models.CharField(max_length=255, default='SOME STRING')
    Cholesterol = models.CharField(max_length=255, default='SOME STRING')
    FBSover120 = models.CharField(max_length=255, default='SOME STRING')
    EKGresults = models.CharField(max_length=255, default='SOME STRING')
    MaxHR = models.CharField(max_length=255, default='SOME STRING')
    Exerciseangina = models.CharField(max_length=255, default='SOME STRING')
    STdepression = models.CharField(max_length=255, default='SOME STRING')
    SlopeofST = models.CharField(max_length=255, default='SOME STRING')
    Numberofvesselsfluro = models.CharField(max_length=255, default='SOME STRING')
    Thallium = models.CharField(max_length=255, default='SOME STRING')
    Result = models.CharField(max_length=255, default='SOME STRING')
    message = models.TextField(default='SOME STRING')
    fname = models.CharField(max_length=255, default='SOME STRING')
    lname = models.CharField(max_length=255, default='SOME STRING')