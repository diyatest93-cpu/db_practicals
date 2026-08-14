from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from django.contrib import messages

# Create your views here.


def home(request):

    peoples=[
        {"name": "Diya", "age":20},
        {"name": "Ravina", "age":10},
        {"name": "tanvi", "age":20},
        {"name": "dharmi", "age":17}
    ]


    vegetables=["potato", "Tomato", "chilli"]
    return render(request, "index.html", context= {'peoples': peoples , 'vegetables': vegetables} )



def about(request):
    
    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")

def success_page(request):
    
    return HttpResponse("<h1> This is a success Page </h1>")

def view_sum(request):
    result=None
    Grade=None 
    avg=None
    if request.method=="POST":
        num1= request.POST.get("num1")
        num2= request.POST.get("num2")
        num3= request.POST.get("num3")
        num4= request.POST.get("num4")
        num5= request.POST.get("num5")

        if num1 and num2  and num3 and num4 and num5:
            result=int(num1)+ int(num2)+ int(num3)+ int(num4)+ int(num5)

        avg=result / 5

        if avg >= 90:
            Grade="A++" 
        elif avg >=80  :
            Grade= "A"

        elif avg >=70:
            Grade="B"
        elif avg >=55:
            Grade="C"
        elif avg >=35:
            Grade="D"
        else:
            Grade="None"    
    return render(request, "sum.html", {'result':result, 'Grade':Grade,  'avg':avg})

def agecal(request):
    result=None
    
    
    if request.method=="POST":
        age=request.POST.get("age")
    
        if age:
            age= int(age)
            result={
                "year": age,
                "monts":age*12,
                "weeks":age*52,
                "days":age*365,
                "hours":age*365*24,
                "minutes": age*365*24*60,
                "seconds":age*365*24*60*60,
            }
    return render(request, 'agecal.html', {"result":result})    

def shopping(request):
    result=None
    dis= None

    if request.method=="POST":
        name=request.POST.get("name")
        pname=request.POST.get("pname")
        price=request.POST.get("price")
        qty=request.POST.get("qty")

        if name and pname and price and qty:
            price=int(price)
            qty=int(qty)

            total= price*qty
            if total > 1500:
                dis= total*15/100
            elif total >1000:
                dis= total*10/100
            elif total >500:
                dis= total*5/100
            else:
                dis=total*0/100   

            net=total-dis

            result={
                "name":name,
                "total":total,
                "dis":dis,
                "net":net
            }
    return render(request, 'shopping.html', {'result': result})    

def radiobutton(request):
    result=None

    if request.method=="POST":
        result=None
        gender=request.POST.get("gender")

        result={
            "gender":gender
        }

    return render(request, 'radio.html',{'result': result})    

def checkbox(request):

    select=[]
    if request.method== "POST":
        if request.POST.get("python"):
            select.append("python")

        if request.POST.get("java"):
            select.append("java") 
        if request.POST.get("C++"):
            select.append("C++")       
            

    return render(request, 'checkbox.html', {'select':select})

def dropdown(request):
    city = ""
    if request.method == "POST":
        city = request.POST.get("city")

    return render(request, 'select.html', {'city':city})


def image(request):
    uploaded_image = None  # Initialize it first
    name=""

    if request.method == "POST":
        file = request.FILES.get("image")

        if file:
            if file.name.endswith(("jpeg", "jpg", "png")):
                    exist_image=Image.objects.filter(name=file.name, size=file.size).exists()
                    if exist_image:
                        messages.error(request, "Already uploaded Image !")
                    else:    
                        uploaded_image = Image.objects.create(image=file, name=file.name, size=file.size)

            

    return render(request, "image.html", {
        "uploaded_image": uploaded_image,


      
    })
    
def table(request):
    result=[]
    num=None
    num1=None
    
    if request.method == "POST":
        num=int(request.POST.get("val"))
        num1=int(request.POST.get("val1"))
        
        for i in range(num,num1+1):
            for j in range(1,11):
                result.append((i,j, i*j ))
                
                
    return render(request, 'tables.html', {'result':result, 'num':num , 'num1':num1})

def wh_loop(request):
    
    result=None
    if request.method=="POST":
        num=int(request.POST.get("value"))
        rev=0
        

        while num >0:
            digit= num % 10
            rev= rev*10 + digit
            num = num //10
        result= rev    
        

    return render(request, 'while.html',{'result': result})  

def rev_array(request):
    result=[]
    if request.method=="POST":
        arr= request.POST.get('arr')
        arr=arr.split()
        i=len(arr)-1
        while i>=0:
            result.append(arr[i])
            i -=1
    return render(request, 'array.html', {'result':result})              

def reg_page(request):
    if request.method =="POST":
        request.session['name']= request.POST['name']
        request.session['email']= request.POST['email']
        request.session['password']= request.POST['password']
        request.session['gender']= request.POST['gender']

        return redirect('login')
    return render(request, 'registration_page.html')

def login(request):
    if request.method== "POST":
        lo_email=request.POST['lo_email']
        lo_pass=request.POST['lo_password']

        if (lo_email == request.session.get('email') and lo_pass == request.session.get('password')):
            return redirect('home')
        else:

            return render(request, 'login_page.html',{'msg':'Invalid email or pssword'})
    return render(request,'login_page.html')   


def home(request):
    name=request.session.get('name')
    gender=request.session.get('gender')

    return render(request, 'homme.html', {'name':name, 'gender': gender})


def index(request):
    return render(request, 'querystring_1.html')

def hello(request):
    name=request.GET.get('name')

    return HttpResponse(f"hello {name}")

def cookie(request):
    name=""
    if request.method=="POST":
        email= request.POST['email']
        password=request.POST['password']
        remember= request.POST.get('remember')

        response = render(request, "cookies.html", {"email": email, 'password': password, "remember": remember})

        if remember:
           
            response.set_cookie("email", email, max_age=31536000)
            response.set_cookie("password", password, max_age=31536000)
            response.set_cookie("remember", "on", max_age=31536000)
        else:
            
            response.set_cookie("email", email)
            response.set_cookie("password", password)
            response.delete_cookie("remember")

        return response
    
    email = request.COOKIES.get("email", "")
    password = request.COOKIES.get("password", "")
    remember=request.COOKIES.get("remember", "")

    return render(request, "cookies.html", {"email": email, "password": password, "remember": remember})

