from django.shortcuts import render,redirect
from .models import Employee

def index(request):
    data=Employee.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)
def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Employee(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
        return render (request,"index.html")
def updateData(request,id):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        
        edit=Employee.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        return redirect("/")
        
        
        
    d=Employee.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)
    


def deleteData(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request,"delete.html")
    
    
    
    
    
    
    
    
    
    

    

# Create your views here.
