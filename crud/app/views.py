from django.shortcuts import render,redirect
from .models import Student,Subject
from django.views import View
# Create your views here.

class index(View):
    def get(self,request):
        sub = Subject.objects.all()
        return render(request,'index.html',{'sub':sub})
    def post(self,request):
        if request.method =="POST":
            name = request.POST['name']
            subject = request.POST['subject']
            subject = Subject.objects.get(id=subject)
            address = request.POST['address']
            mobile = request.POST['mobile']
            image = request.FILES['image']
            Student.objects.create(name=name,address=address,mobile=mobile,image=image,subject=subject)
            return redirect('/table/')


def table(request):
    data = Student.objects.all()
    return render(request,'table.html',{'data':data})

def delete(request,uid):
    Student.objects.filter(id=uid).delete()
    return redirect('/table/')

def update(request,uid):
        sub = Subject.objects.all()
        return render(request,'update.html',{'uid':uid,'sub':sub})

def upd(request):
        if request.method =="POST":
            hide = request.POST['hide']
            name = request.POST['name']
            subject = request.POST['subject']
            subject = Subject.objects.get(id=subject)
            address = request.POST['address']
            mobile = request.POST['mobile']
            image = request.FILES['image']
            Student.objects.filter(id=hide).update(name=name,address=address,mobile=mobile,image=image,subject=subject)
            return redirect('/table/')
