from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models  import trainee
from .forms import Traineeform ,Courseform

def index(request):
    traine = trainee.objects.all()
    context={'trainee': traine}
    return render(request ,'trainee/form.html',context)


def Newstrainee(request):
    tr_form=Traineeform()
    context={'tr_form': tr_form}
    if request.method=='POST':
        tr_form=Traineeform(request.POST)
        if tr_form.is_valid():
            tr_form.save()
            return HttpResponseRedirect('/')

    return render(request,'trainee/new.html',context)


def deletestudent(request,tr_id):
    deleted_st=trainee.objects.get(id=tr_id)
    deleted_st.delete()
    traine = trainee.objects.all()
    context={'trainee': traine}
    return render(request ,'trainee/form.html',context)



def edittrainee(request,tr_id):
    edited_st=trainee.objects.get(id=tr_id)
    tr_form=Traineeform(instance=edited_st)
    if request.method=='POST':
        tr_form=Traineeform(request.POST, instance=edited_st)
        if tr_form.is_valid():
            tr_form.save()
            return HttpResponseRedirect('/')

    context={'tr_form': tr_form}
    return render(request ,'trainee/new.html',context)


