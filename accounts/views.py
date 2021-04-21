from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.filter import UserFilter




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userlogin(request):
    if request.session.has_key('logged_in'):
        return redirect("home")
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            request.session['logged_in'] = True
            return redirect('home')

        else:
            messages.info(request, '**Incorrect username or password!')
            return render(request, 'login.html')
            
    else:
         
         return render(request, 'login.html')

   

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def usersignup(request):
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:  
            if User.objects.filter(username = username).exists():
              messages.info(request,'**Username not available')
            else:   
                user = User.objects.create_user(username = username ,email= email, first_name = first_name, last_name = last_name, password = password1)
                user.save()
                
                return redirect('login')
                
        else:
            messages.info(request,'**Passwords are not same')
            return redirect('signup') 
    return render(request, 'signup.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.session.has_key('logged_in'):
        return render(request, 'home.html')

    else:
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    del request.session['logged_in']
    return redirect('login')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if request.session.has_key('logged'):
        return redirect("adminpage")

    elif request.method == "POST":
        name = 'shareef'
        pswd = '123456'
        username = request.POST['username']
        password = request.POST['password']
        if username == name and password == pswd:
            request.session['logged'] = True
            return redirect('adminpage')
        else:
            messages.info(request, '**Incorrect username or password!')
            return render(request, 'admin_login.html')
    else:
         return render(request, 'admin_login.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminpage(request):
    if request.session.has_key('logged'):
        # users = User.objects.all()
        users = User.objects.exclude(is_superuser = 1)
        user_filter = UserFilter(request.GET, queryset = users)
        return render(request, 'admin_page.html', {'users': user_filter})        
    else:
        return redirect( 'admin')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def useradd(request):
    if request.session.has_key('logged'):
        
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 == password2:  
                if User.objects.filter(username = username).exists():
                    messages.info(request,'**Username already exists')
                    return redirect('adduser')
                    
                else:   
                    user = User.objects.create_user(username = username ,email= email, first_name = first_name, last_name = last_name, password = password1)
                    user.save()            
                    return redirect('adminpage')
            else:
                messages.info(request,'**Passwords are not same')
                return redirect('adduser') 
        else:       
            return render (request, 'add_user.html')
    else:
         return render(request, 'admin_login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def adminlogout(request):
    del request.session['logged']
    return redirect('admin')

# def userlist(request):
#     users = User.objects.all()
#     return render(request, 'admin_page.html', {'users':users})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateuser(request, pk):
    
    user = User.objects.get(id = pk)   
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        newemail = request.POST['email']
        user.first_name = fname
        user.last_name = lname
        user.email = newemail
        user.save()
        return redirect('adminpage')    
    return render(request, 'user_update.html', {'user': user})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteuser(request, pk):
    user = User.objects.get(id = pk)
    user.delete()
    messages.error(request, 'User deleted successfully')
    return redirect('adminpage')   