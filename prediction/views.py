from re import M
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.urls import reverse
from tkinter import *  
from tkinter import messagebox
from matplotlib.style import context  
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import auth
from .models import Data
from sklearn.preprocessing import LabelEncoder 
import mimetypes
import os
from contextlib import contextmanager
from django.template import *
from pprint import pprint
from googleapiclient import discovery
from sklearn import svm
import joblib
from datetime import datetime
from django.shortcuts import render
from prediction.form import BasicForm


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


  

# def signup(request):
#   template = loader.get_template('Home.html')
#   return HttpResponse(template.render())  

def signup(request):
    if request.method == 'POST':
      form = BasicForm(request.POST)
      if form.is_valid():
            pass
            
    else: 
      form = BasicForm()
    return render(request, 'signup.html', {'form': form})



def Report(request):
     mydata = Data.objects.order_by('-id')[0]
     
     template = loader.get_template('report.html')
     context = {
        'mydata': mydata,
     }
     return HttpResponse(template.render(context, request))


def data(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'indian_liver_patient.csv'
    # Define the full file path
    filepath = BASE_DIR + '/liverpredict/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

@csrf_exempt
def predict(request):
      a = request.POST['age']
      b = request.POST['sex']
      c = request.POST['che']
      d = request.POST['bp']
      e = request.POST['Cho']
      f = request.POST['fbs']
      g = request.POST['ekg']
      h = request.POST['max']
      i = request.POST['exer']
      j = request.POST['st']
      u = request.POST['slope']
      v = request.POST['num']
      z = request.POST['tha']
      m = request.POST['fname']
      n = request.POST['lname']
      model=joblib.load('/home/ihame/Documents/MyPython/IhamePython/heartproject/prediction/heartdataset.joblib')
      predictions = model.predict([[a,b,c,d,e,f,g,h,i,j,u,v,z]])
      k = predictions
      if k == 'Absence':
        if b == 1:
          note = """ Dear,""" + m +""" """+n + """ According to the result, We have found out that you are NEGATIVE against Heart disease """
          dat = Data(
          Age = a, Sex = 'Male', Chestpaintype = c, BP = d, Cholesterol = e, FBSover120 = f, EKGresults = g, MaxHR = h, Exerciseangina = i, STdepression = j, SlopeofST = u, Numberofvesselsfluro = v, Thallium = z, Result = k, message = note, fname = m, lname = n)
          dat.save()
        else:
          note = """ Dear,""" + m +""" """+n + """ According to the result, We have found out that you are NEGATIVE against Heart disease """
          dat = Data(
          Age = a, Sex = 'Female', Chestpaintype = c, BP = d, Cholesterol = e, FBSover120 = f, EKGresults = g, MaxHR = h, Exerciseangina = i, STdepression = j, SlopeofST = u, Numberofvesselsfluro = v, Thallium = z, Result = k, message = note, fname = m, lname = n)
          dat.save()
      else:
        if b == 1:
          note = """ Dear,""" + m +""" """+n + """ We have unfortunetly found that you are POSITIVE against Heart disease """
          dat = Data(
          Age = a, Sex = 'Male', Chestpaintype = c, BP = d, Cholesterol = e, FBSover120 = f, EKGresults = g, MaxHR = h, Exerciseangina = i, STdepression = j, SlopeofST = u, Numberofvesselsfluro = v, Thallium = z, Result = k, message = note, fname = m, lname = n)
          dat.save()
        else:
          note = """ Dear,""" + m +""" """+n + """ We have unfortunetly found that you are POSITIVE against Heart disease """
          dat = Data(
          Age = a, Sex = 'Female', Chestpaintype = c, BP = d, Cholesterol = e, FBSover120 = f, EKGresults = g, MaxHR = h, Exerciseangina = i, STdepression = j, SlopeofST = u, Numberofvesselsfluro = v, Thallium = z, Result = k, message = note, fname = m, lname = n)
          dat.save()
      return HttpResponseRedirect(reverse('report')) 