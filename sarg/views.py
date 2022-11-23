from django.shortcuts import render
from . models import Catogory, Competition, Result, Unit
# Create your views here.
def welcome(request):
    cat = Catogory.objects.all() 
    return render(request,'home.html', {'cat':cat,})

def catsel(request):
    cat = request.POST.get('cat')
    catsel=cat
    cat = Catogory.objects.get(catogory_name=cat)
    res = Result.objects.all()
    com = Competition.objects.filter(catogory=cat)
    resul = []
    unit = Unit.objects.all()
    for r in res:
        if r.competition.catogory.catogory_name == cat:
            resul.append(r)
    print(resul)
    rc=[]
    for u in unit:
        for c in com:
            rc.append([r if r.competition==c and r.unit==u else 0 for r in resul])
    print(rc)
                    

    com = Competition.objects.filter(catogory=cat)
    cat =Catogory.objects.all()
    return render(request,'home.html', {'com':com, 'catsel':catsel, "cat":cat})

def result(request):
    com = request.POST.get('com')
    comsel = com
    com = Competition.objects.get(competition_name=com)
    res = Result.objects.filter(competition=com)
    cat =Catogory.objects.all()
    com = Competition.objects.all()
    return render(request,'home.html', {'comsel':comsel,'res':res, 'catsel':catsel, 'cat': cat, 'com':com})
