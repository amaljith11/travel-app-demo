from django.shortcuts import render

from . models import details 

# Create your views here.
def index(request):
    # obj = details()
    # obj.name = 'HOTEL PARADISE'
    # obj.desc = 'in vadakara'
    obj=details.objects.all()



    return render (request,'index.html',{'results':obj})

