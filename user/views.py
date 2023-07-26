from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from user.models import User


# 요청 객체의 방식은 보편적으로 총 4가지가 있다.
# (물론 더 많이 존재한다.)

# Create your views here.
def signin(request):
    # 값을 읽고싶을 때 GET - URL PARAMETERN (http:zy_zero37?title=안녕하세요)
    # 값을 지우고 싶을 때 DELETE - url에 무언가 같이 보내는 것이 default

    # 값을 수정 PUT - body쪽에 값을 넣어서 전달 / 보통 로그인이나 회원가입을 할때는 노출이 되는 GET방식 보다 보편적으로 POST방식을 사용
    # 값을 생성 POST

    # 로그인
    if request.method == "GET":
        # request.GET['title'] # 안녕하세요
        # request.POST["hh"] # 키값을 넣으면 그 값을 받을 수 있음
        # print(request.GET['title']) #하이하이
        return render(request, 'page/signin.html')
    
    # user, password
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            messages.error(request, "입력값을 확인해주세요.")
            return redirect('signin')

    # 회원가입
def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')


