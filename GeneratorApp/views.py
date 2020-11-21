
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'GeneratorApp/home.html',{'Password':'Hui56hfgds'})

def About(request):
    return render(request, 'GeneratorApp/About.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uuppercaseletters"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("specialsymbols"):
        characters.extend(list("!@#$%^&*<>/|()"))

    lenght = int(request.GET.get('lenght',12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)


    return render(request, 'GeneratorApp/password.html', {"password":thepassword})
