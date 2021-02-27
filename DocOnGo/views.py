from django import forms
from django.shortcuts import render, redirect
from .forms import DetailForm
from datetime import datetime
import string
import csv

# Create your views here.

def index(request):
    print("HELLO")
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            str = form.cleaned_data['str']
            data = detailsfunc(name, email, str)
            return render(request, 'cards.html', {'data' : data})
        else:
            print("ERROR")
    else:
        form = DetailForm(request.POST)
        msg = "ERROR"
        return render(request, 'index.html', {'data' : msg})

def detailsfunc(name, email, str):
    #main extractor
    problem = str
    data=dict()
    txts = problem.split(" ")
    duration = ""

    try:
        for i in range(len(txts)):
            if txts[i].lower() == "since" or txts[i].lower() == "from":
                duration = txts[i+1]+" "+txts[i+2]
                break
    except:
        duration=""
   
    data['duration'] = duration.translate(str.maketrans('', '', string.punctuation))

    symptom = ""

    try:
        z=0
        txts = problem.split(" ")
        for i in range(len(txts)):
            if txts[i].lower() in ("have","having","feel","feeling"):
                si = i
            if txts[i] == "since":
                sii = i
                z=1
                break 
        if z == 1:
            for x in txts[si:sii]:
                symptom += x+" "
            z=0

    except:
        z=0
        symptom = problem

    data['symptom'] = symptom.translate(str.maketrans('', '', string.punctuation))

    aggrv=""
    txt = problem.lower()
    for i in ("during","while","when","increases","decreases"):
        k=-1;s=''
        try:
            k = txt.find(i)
            if k >= 0:
                s = txt[k:txt.index('.',k)]
                aggrv=s
                break
        except:
            aggrv=""
            pass
    data['name'] = name
    dt = datetime.now()
    strg = dt.strftime('%d %B %Y')
    data['date']=strg
    problem = problem.replace('\n','')
    data['aggrv']=aggrv.translate(str.maketrans('', '', string.punctuation))
    data['story']=problem.translate(str.maketrans('', '', string.punctuation))
    print(data['symptom'])
    with open("doctor.csv",'a') as f:
        f.write("\n"+data['name'] + "," +data['story'] + "," +data['duration'] + "," +data['symptom'] + "," +data['aggrv'] + "," +data['date'] )

    return data   

def datatable(request):
    n,st,dr,sp,dt,af = [],[],[],[],[],[]
    with open('E:\hackathon\doctor.csv', 'r') as file:
        reader = csv.reader(file)
        k = 0
        print("-")
        for row in reader:
            if k != 0:
                print(row[0])
                print(row[0]+"-")
                n.append(row[0])
                st.append(row[1])
                dr.append(row[2])
                sp.append(row[3])
                af.append(row[4])
                dt.append(row[5])
            else:
                k+=1
    data = zip(n,st,dr,sp,af,dt)
    print(dt)
    return render(request, 'table.html',{'data':data})