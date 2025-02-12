from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    if request.method== "POST":

        data = request.POST
        rimg = request.FILES.get('rimg')
        rname = data.get("rname")
        rdesc = data.get("rdesc")
        
        Recipe.objects.create(
            recipe_name = rname,
            recipe_desc = rdesc,
            recipe_image = rimg,
        )

        return redirect('/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset= queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'receipes': queryset}

    return render(request, 'index.html', context)

def delR(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect('/')

def updateR(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
       data = request.POST
       rimg = request.FILES.get('rimg')
       rname = data.get("rname")
       rdesc = data.get("rdesc")


       queryset.recipe_name = rname
       queryset.recipe_desc = rdesc

       if rimg:
           queryset.recipe_image = rimg

       queryset.save()
       return redirect('/')
        
    context = {'receipe':queryset}

    return render(request, 'update.html', context)




