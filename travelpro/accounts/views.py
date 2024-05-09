from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        passw = request.POST['logpass']
        user = auth.authenticate(username=username,password=passw)
        if user is not None:
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            print('invalid')
            return redirect('login')
        
    else:
        print('logedin')
        return render(request,'login.html')
        
    
    
    
def account(request):
    if request.method=='POST':
        name = request.POST['firstname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1==password2:
            if User.objects.filter(username=name).exists():
                messages.info(request,('user name taken'))
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,('email taken'))
                return redirect('register')
            else: 
                user = User.objects.create_user(username=name,email=email,password=password1)
                user.save()
                print('user created')
                messages.info(request,('successfully registered'))                    
        else:
             messages.info(request,('password not match'))
             return redirect('register')
        return redirect('/')
    else:
        return render(request,'reg.html')
    



    

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
