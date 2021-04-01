from django.shortcuts import render
from .models import News
from .parse import data
# Create your views here.



def intro(request):
    return render(request, 'schedules/intro.html')

def index(request):
    news = News.objects.all()
    
    context = {'news':news, 'data': data}
    return render(request, 'schedules/index.html',context)