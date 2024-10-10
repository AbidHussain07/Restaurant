from django.shortcuts import render , redirect
from django.http import HttpResponse
from Product.models import Itemlist , Items , About , Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def Home(request):
    review = Feedback.objects.all()
    return render(request, 'home.html',{'review' : review})

def Menu(request):
    items = Items.objects.all()
    category = Itemlist.objects.all()
    return render(request, 'menu.html' , {'items': items , 'category' : category})

def Abouts(request):
    return render(request, 'about.html')

def More_about(request):
    return render(request, 'about2.html')

# def Book_table(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         phone_no = request.POST.get('phone_no')
#         email = request.POST.get('email')
#         total_member = request.POST.get('members')
#         date = request.POST.get('booking_date')
        
#         if name!='' and phone_no!='' and email!='' and total_member!= 0 and date!='':
#             data = BookTable(
#                 name = name ,
#                 phone_no = phone_no ,
#                 email = email,
#                 total_member = total_member,
#                 date = date,
#             )
#             data.save()
#     return render(request, 'book_table.html')

def Feedbacks(request):
    review = Feedback.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        msg = request.POST.get('review')
        rating = request.POST.get('rating') 
        
        reviews = Feedback.objects.create(
            username = name,
            description = msg,
            rating = int(rating),
        )  
        reviews.save()
        return redirect('/feedback/')
    return render(request , 'Review.html',{'review' : review})

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request , "Username Already Taken Please Choose Another")
            return redirect('/register/')
        
        user = User.objects.filter(email = email)
        if user.exists():
            messages.info(request , "This Email-Id is already Registered.")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.success(request , "Account Created Successfully!!!")
        return redirect('/register/')
        
    return render(request , 'register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.warning(request , "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.warning(request , "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request , user)
            return redirect('/')
            
    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')