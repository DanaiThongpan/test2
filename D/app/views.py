from django import forms
from django.shortcuts import render, redirect
from .models import db
# Create your views here.
class dbf(forms.ModelForm):
    class Meta():
        model = db
        fields = '__all__'

def home(req):
    f = dbf()
    if req.method == 'POST':
        f = dbf(req.POST)
        if f.is_valid():
            f.save()
    c = db.objects.all()
    return render(req,'home.html',{'f':f,'c':c})

def update(req, id):
    c = db.objects.get(pk=id)
    f = dbf(instance=c)
    if req.method == 'POST':
        f = dbf(req.POST, instance=c)
        if f.is_valid():
            f.save()
            return redirect('/')

    return render(req,'update.html',{'f':f,'c':c}) 