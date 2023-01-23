from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    data = pd.read_csv('https://storagefrt123.blob.core.windows.net/static/dataset/diabetes.csv')
    X=data.drop("Outcome", axis=1) 
    Y=data['Outcome']

    scaler = MinMaxScaler()
    X[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']] = scaler.fit_transform(X)
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2, random_state = 32)
    
    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])  

    result1="" 
    if prediction==[0]:
        result1="Diabetic"
    else:
        result1="Not Diabetic" 

    return render(request,'result.html', {"result1":result1})

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        flag=0
        if password1!=password2:
            messages.info(request, "Passwords don't match")
            flag=1
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            flag=1
        if User.objects.filter(email=email).exists():
            messages.info(request, "This email is linked to an existing account")
            flag=1
        if flag == 1:
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password1, email=email)
            user.save()
            return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')