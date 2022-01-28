from django.shortcuts import redirect, render
from CrudApp.forms import AddStudentForm
from .models import Student

def CrudHome(request):
    return render(request,'crud/crud_home.html')

def AddStudent(request):
    if request.method=='POST':
        frm=AddStudentForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('crudhome')
    else:
        fm=AddStudentForm()
        return render(request,'crud/add_student.html',{'form':fm})

def DisplayAll(request):
    stData=Student.objects.all()
    return render(request,'crud/display_all.html',{'alldata':stData})

def DeleteStudent(request):
    if request.method=='POST':
        stid=request.POST['hdStId']
        StudData=Student.objects.get(id=stid)
        StudData.delete()
        return redirect('crudhome')
    else:
        stData=Student.objects.all()
        return render(request,'crud/delete_student.html',{'alldata':stData})