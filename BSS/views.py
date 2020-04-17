from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from .models import Available_Books, Available_Stationary, Total_books
import urllib
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, "index.html")


def about(request):
     return render(request, "about.html")


def register(request):

    if request.method == 'POST':
        username = request.POST['firstname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        mo = request.POST['number']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Number Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=mo)
                user.save()
                print('user created')
            return redirect('login')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'Register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'Login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def donate(request):

    return render(request, 'donate.html')


def Add(request):

    if request.method == 'POST':
        Ownername = request.POST['Oname']
        BookName = request.POST['bname']
        Edition = request.POST['ed']
        AuthorName = request.POST['aname']
        Publication = request.POST['pub']
        BookCategory = request.POST['cat']
        img = request.POST['fileToUpload1']
        pdf = request.POST['fileToUpload2']
        Department = request.POST['dep']
        Semester = request.POST['sem']
        Return = request.POST['rt']

    Idata = Available_Books.objects.create(BookName=str(BookName), Edition=str(Edition), AuthorName=str(
        AuthorName), Publication=str(Publication), BookCategory=str(BookCategory), img=str(img), Ownername=str(Ownername), pdf=str(pdf), Semester=str(Semester), Department=str(Department), Return=str(Return))
    temp = Total_books.objects.create(User=str(Ownername), Number_Of_Books_Donate=str(
        (Available_Books.objects.filter(Ownername=Ownername).count())))

    return render(request, "donate.html")


def show(request):

    Book_dets = Available_Books.objects.all()
    return render(request, "books.html", {'Book_dets': Book_dets})


def search(request):

    if request.method == 'POST':
        Bname = request.POST['bn']
        Book_dets = Available_Books.objects.filter(BookName=Bname)
        # Book_del = Available_Books.objects.filter(BookName=Bname).delete()
    return render(request, "search.html", {'Book_dets': Book_dets})


def delete(request):

    Book_dets = Available_Books.objects.all()
    return render(request, "books.html", {'Book_dets': Book_dets})


def chat(request):
    return render(request, "inbox.html")


def cart(request):
    return render(request, "cart.html")


@login_required
def dlt(request, item_id):

    obj = Available_Books.objects.filter(pk=item_id)
    return render(request, "index.html", {'obj': obj})


def message(request):
    return redirect("home")