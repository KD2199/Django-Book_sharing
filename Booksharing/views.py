from django.shortcuts import render,HttpResponse


def index(request):
    # Book_dets = Book.objects.all()
    return render(request, "index.html")
    # return HttpResponse("<h1>Welcome</h1>")