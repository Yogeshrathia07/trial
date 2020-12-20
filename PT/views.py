from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.messages.api import error
from django.forms.fields import DateField, DateTimeField
from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib import messages
from .forms import files
#from .models import NOTES
from.models import MONDAY, TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY, NOTIFICATION, WEDNESDAY,NOTE
# Create your views here.
from django.contrib.auth.decorators import login_required

 
def home(request):

           return render(request,'index.html') 
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')    
def timetable(request):

      #tt=TIMETABLE.objects.all()
      #mon=MONDAY.objects.all()
        mon=MONDAY.objects.order_by('starttime')#.filter(day__iexact='Monday')     
        #mon=TIMETABLE.objects.order_by('day')
        tue=TUESDAY.objects.order_by('starttime')#.filter(day__iexact='Tuesday')
        wed=WEDNESDAY.objects.order_by('starttime')#.filter(day__iexact='Wednesday')
        thu=THURSDAY.objects.order_by('starttime')#.filter(day__iexact='Thursday')
        fri=FRIDAY.objects.order_by('starttime')#.filter(day__iexact='Friday')
        sat=SATURDAY.objects.order_by('starttime')#.filter(day__iexact='SATURDAY')
        sun=SUNDAY.objects.order_by('starttime')#.all().filter(day__iexact='Sunday')
        return render(request,'timetable1.html',{'n1':mon,'n2':tue,'n3':wed,'n4':thu,'n5':fri,'n6':sat,'n7':sun})


@login_required(login_url='login') 
def notification(request):
    noti=NOTIFICATION.objects.all()
    return render(request, "notification.html",{'n8':noti})


@login_required(login_url='login') 
def notes(request):
    if request.method == "POST":
        form = files(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = files()
    fl=NOTE.objects.order_by('datetime')
    return render(request,'notes.html',{'fl':fl,'form':form}) 

#def delete(request, id):
 #   if request.method == "POST":
  #      pi = User.objects.get(pk=id)
   #     pi.delete()
    #    return HttpResponseRedirect('/')  

@login_required(login_url='login') 
def delete(request, pk):
    if request.method == 'POST':
        pi = NOTE.objects.get(pk=pk)
        pi.delete()
    return redirect('/notes')


def about(request):
    return render(request,'about.html')

def nhome(request):
    return render(request,'home.html')





def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.error(request,'User created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('/register')
        
        
    else:
        return render(request,'registration.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       



    



    