from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentForm

# Create your views here.
class Home(View):
    def get(self,request):
        #getting the data from database and sending to the template with name 'Studata'
        data=Student.objects.all()
        return render(request,'core/home.html',{'Studata':data})

#view for adding Student
class Add_Student(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core/add-student.html',{'form':fm})
    
    def post(self,request):
        #getting data from addstudent.html with post method
        fm=AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add-student.html',{'form':fm})

#view for deleting the student
class Delete_Student(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata=Student.objects.get(id=id)
        studata.delete()
        return redirect('/')

class Edit_Student(View):
    def get(self,request,id):
        stu=Student.objects.get(id=id)
        fm=AddStudentForm(instance=stu)
        return render(request,'core/edit-student.html',{'form':fm})

    def post(self,request,id):
        stu=Student.objects.get(id=id)
        fm=AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
