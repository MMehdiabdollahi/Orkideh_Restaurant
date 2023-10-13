

from django.shortcuts import render
from .models import Food , HomePics , SliderPics
# Create your views here.

def food_list(request):
    food_list = Food.objects.all()
    homepics = HomePics.objects.all()
    sliderpics = SliderPics.objects.all()
    context = {
        "foods":food_list,
        "pics":homepics,
        "sliderpic":sliderpics,
    }

    return render(request,"foods/list.html",context)

def food_detail(request,id):
    food = Food.objects.get(id = id)
    context = {
        "food":food,
    }
    return render(request,"foods/detail.html",context)


    
