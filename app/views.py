from django.shortcuts import render
from .models import DoctorReg,predictions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
    
def slogin(request):
    if request.method=='POST':
        v=DoctorReg.objects.all()
        usn=request.POST['username']
        pwd=request.POST['passwd']
        check = False
        for i in v:
            if(i.pname==usn and i.password==pwd):
                check = True
                return render(request,'slogin.html',{'patient': usn})
        if check==False:
            return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
    
def ssignup(request):
    fname = request.POST['fname']
    email = request.POST['email']
    pwd = request.POST['passwd']
    cpwd = request.POST['cpasswd']
    try:
        doc = bool(request.POST['doc'])
    except MultiValueDictKeyError:
        doc = False
    phno = request.POST['phno']
    
    if (pwd==cpwd):
       user=DoctorReg(pname=fname,pemail=email,pphone=phno,password=pwd,doctor=doc) 
       user.save()
       
    return render(request,'slogin.html',{'patient': fname})

def predict(request):
    if(request.method == 'POST'):
        age = int(request.POST['age'])
        sex = int(request.POST['gender'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['tbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['rer'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['op'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])
        
        df = pd.read_csv(r"static/datasets/heart.csv")
        
        
        X = df.drop('target',axis=1)
        Y = df[['target']]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.10, random_state = 1)    
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        forest = RandomForestClassifier(n_estimators = 200, criterion = 'entropy', random_state = 1)
        forest.fit(X_train, Y_train)
        model = forest
        predict = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,
                             slope, ca, thal]])
        pred = model.predict(predict)
        
        target = pred[0]
                      
        hp = predictions(age=age,sex=sex,cp=cp,
                          trestbps=trestbps,chol=chol,fbs=fbs,restecg=restecg,
                          thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,
                          ca=ca,thal=thal,target=target)
        hp.save()
        
        if(target==1):
            r="Positive"
        else:
            r="Negative"
        if(sex==0):
            g="Female"
        else:
            g="Male"
        v=DoctorReg.objects.all()
        for i in v:
            return render(request,'predictions.html',{'predicted':r ,'age':age, 'gender':g ,'cp':cp, 'chol':chol, 'fbs':fbs, 'thalach':thalach})
    
    
    else:
        return render(request,'slogin.html')  
    
def consult(request):
    v=DoctorReg.objects.all()
    l=[]
    for i in v:
        if i.doctor==True:
            l.append(i)
    return render(request,"consult.html",{'lists':l})