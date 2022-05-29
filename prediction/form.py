from email.policy import default
from django import forms


class BasicForm(forms.Form):
   
    first_name = forms.CharField()
    Age = forms.CharField(max_length=255)
    Sex = forms.CharField(max_length=255)
    Chestpaintype = forms.CharField(max_length=255)
    BP = forms.CharField(max_length=255)
    Cholesterol = forms.CharField(max_length=255)
    FBSover120 = forms.CharField(max_length=255)
    EKGresults = forms.CharField(max_length=255)
    MaxHR = forms.CharField(max_length=255)
    Exerciseangina = forms.CharField(max_length=255)
    STdepression = forms.CharField(max_length=255)
    SlopeofST = forms.CharField(max_length=255, )
    Numberofvesselsfluro = forms.CharField(max_length=255)
    Thallium = forms.CharField(max_length=255)
    Result = forms.CharField(max_length=255)
    message = forms.CharField(max_length=1000)
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)


  