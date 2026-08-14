from django.shortcuts import render, redirect, get_object_or_404
from .models import save_info


# Create your views here.
def index(request):
    if request.method=="POST":
        save_info.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobileNo=request.POST.get('mobileNo'),
            gender=request.POST.get('gender'),
            city=request.POST.get('city')
        )
        return redirect('index')

    #data = save_info.objects.all()
    return render(request, 'db_practicals/simple_db1.html')

def show(request):
    
    data=save_info.objects.all()
    return render(request, 'db_practicals/simple_db1.html', {'save_info': data})    

def delete(request, id):
    data=save_info.objects.get(id=id)
    data.delete()
    return redirect('show')

def update(request,  id):
    data=get_object_or_404(save_info, id=id)
    if request.method=="POST":
        data.name= request.POST.get('name')
        data.email= request.POST.get('email')
        data.mobileNo= request.POST.get('mobileNo')
        data.gender= request.POST.get('gender')
        data.city= request.POST.get('city')
        data.save()

        return redirect('show')
    return render(request, 'db_practicals/edit.html', {'data': data})

def search(request):
    if request.method=="POST":
        search= request.POST.get('search')

        data=save_info.objects.filter(name__icontains= search)

        return render(request, 'db_practicals/simple_db1.html', {'save_info': data}) 
    return redirect('show')
   
def login(request):

    if request.method== "POST":
        name=request.POST.get('name')
        email= request.POST.get('email')

        request.session['name']= request.POST['name']
    
        user = save_info.objects.filter(name=name, email=email).first()

        if user:
            return render(request, 'db_practicals/home1.html', {'name':name})
        else:
            return render(request, 'db_practicals/login_page.html', {'error': 'invalid name or email' })
    return render(request, 'db_practicals/login_page.html')   

