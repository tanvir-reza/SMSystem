from django.shortcuts import render
from .models import Result
from django.views import View

# Create your views here.
class index(View):
    def get(self,request):
        results = Result.objects.all()
        
        # print(results.student)
        context = {
            'results':results,
        }
        return render(request,'students.html',context)