from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user 



# Create your views here.

#This Function will add new data and show all data
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(Name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = user.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'stu':stud})

#This function will update.
def update_data(request, id):
    if request.method =='POST':
        pi=user.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi=user.objects.get(pk=id)
         fm= StudentRegistration(instance=pi)

    return render(request,'update.html',{'form':fm})
    



#This will delete the data.

def delete_data(request,id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    


  

    
    