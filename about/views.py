from django.shortcuts import render

# Create your views here.
def about_us(request):
    

    context = {
        
    }

    return render(request,"about/about.html",context)