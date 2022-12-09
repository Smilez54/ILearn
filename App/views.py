from django.shortcuts import render
from .models import Carousel, Courses


# Create your views here.
def index(request):
    
    carol = Carousel()
    carol.title = 'Best Paid Course Ever'
    carol.heading = 'Your number one online learning platform'
    carol.description = 'Learn from the best teachers and get your desired certification'
    
    
    cor1 = Courses()
    cor1.price = 357.00
    cor1.rate = 125
    cor1.title = 'Social Engineering Course for Beginners'
    cor1.name = 'Michael Tosin'
    cor1.time = '2 Hrs'
    cor1.num_stu = '35 Students'
    
    cor2 = Courses()
    cor2.price = 349.00
    cor2.rate = 127
    cor2.title = 'Backend Development Course for Beginners'
    cor2.name = 'Drey Yerin'
    cor2.time = '1.4 Hrs'
    cor2.num_stu = '50 Students'
    
    cor3 = Courses()
    cor3.price = 350.00
    cor3.rate = 129
    cor3.title = 'Frontend Development Course for Beginners'
    cor3.name = 'Whale Yodah'
    cor3.time = '3 Hrs'
    cor3.num_stu = '75 Students'
    
    cor = [cor1, cor2, cor3]
    
    return render(request, 'index.html', {'carol':carol, 'cor':cor})
    
