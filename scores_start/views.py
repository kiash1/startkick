from django.shortcuts import render


def home(self,*args, **kwargs):
    return render('base.html',{})

