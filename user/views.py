from django.shortcuts import render

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')
