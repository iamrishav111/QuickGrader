from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from assign_db.models import Destination
# Create your views here.


def status(request):

        student_name=request.POST['name']
        description=request.POST['desc']
        # price=request.POST['price']
        file_name=request.POST['filename']


        # dest = Destination.objects.create_user(name=student_name,desc=description,price=price,filename=file_name)
        # dest.save()

        d=Destination(name=student_name,file_name=file_name,desc=description,price=500,offer=False)
        d.save()        

        return render(request,'status.html')

def loadhome(request):

    username = request.POST['username']
    password = request.POST['password']
    # student_radio=request.POST['student']
    # proff_radio=request.POST['professor']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        # return render(request,'home.html')
        if username == "navin":
            return render(request,'show_submissions.html')
        else:
            return render(request,'home.html')
    else:
        # messages.info(request,'invalid credentials')
        print('Invalid Details')
        return redirect('login')



def login(request):
    
    return render(request,'login.html')    


def loadcontent(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']

    if password1==password2:
        if User.objects.filter(username=username).exists():
            print('Username already used.')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            print("Email ID  Alrady Used")
            return redirect('/')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
            user.save()
            return render(request,'login.html')

        # if User.objects.filter(username=username).exists():
        #     messages.info(request,'Username Taken')
        #     return redirect('')
        # elif User.objects.filter(email=email).exists():
        #     messages.info(request,'Email Taken')
        #     return redirect('')
        # else:   
        #     user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
        #     user.save()
        #     print('user created')
        #     return redirect('')

    else:
        print('password not matching')
        return redirect('/')
        # messages.info(request,'password not matching..')    
        # return redirect('')
        # return redirect('/')

    # return render(request,'home.html')

def register(request):
    return render(request,'register.html')
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']

    #     if password1==password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,'Username Taken')
    #             return redirect('')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request,'Email Taken')
    #             return redirect('')
    #         else:   
    #             user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
    #             user.save()
    #             print('user created')
    #             return redirect('')

    #      else:
    #         messages.info(request,'password not matching..')    
    #         return redirect('')
    #         return redirect('/')
                        
    # else:
        # return render(request,'register.html')


                     



# def logout(request):
#     auth.logout(request)
#     return redirect('/')       