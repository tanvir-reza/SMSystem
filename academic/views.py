from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib import messages
from django.views.generic import UpdateView,DeleteView,RedirectView
from .forms import StudentForm,ClassForm,SubjectForm
from .models import Student,Class

class index(View):
    def get(self,request):
        students = Student.objects.all()
        context = {
            'students':students,
        }
        return render(request,'students.html',context)
    
class addStudent(View):
    def get(self,request):
        form = StudentForm()
        context = {
            'form':form,
        }
        return render(request,'addStudent.html',context)
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        else:
            return HttpResponse("Error in Adding Student")

class addClass(View):
    def get(self,request):
        form  = ClassForm()
        context = {
            'form':form,
        }
        return render(request,'addClass.html',context)
    def post(self,request):
        name = request.POST.get('name')
        Class.objects.create(name=name)
        return redirect('index')

class addSubject(View):
    def get(self,request):
        form = SubjectForm()
        context = {
            'form':form,
        }
        return render(request,'addSubject.html',context)


class editStudent(View):
    def get(self,request,pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(instance=student)
        context = {
            'form':form,
        }
        return render(request,'editStudent.html',context)
    def post(self,request,pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('index')

class DeleteStudent(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

        



    
   
        
