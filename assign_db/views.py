
# from django.contrib.auth.models import User, auth
from assign_db.models import Destination
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from assign_db.forms import destForm
from django.core.files.storage import FileSystemStorage


def loadhome(request):
        form=destForm()

        return render(request,'home.html',{'form':form})

def showsubmissions(request):
    dests = Destination.objects.all()
    return render(request, 'show_submissions.html', {
        'dests': dests
    })

def submit(request):

        form=destForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                return render(request,'status.html')
        else:
                return redirect('/')
        # student_name=request.POST['name']
        # description=request.POST['desc']
        # price=request.POST['price']
        # file_=request.POST['filename']


        # # dest = Destination.objects.create_user(name=student_name,desc=description,price=price,filename=file_name)
        # # dest.save()
        # des=Destination(name=student_name,desc=description,price=price,offer=True)
        # des.save()

        # return render(request,'status.html')
        
