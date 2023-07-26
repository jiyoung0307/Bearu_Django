from django.urls import path
from board.views import board
from user.views import signin, signup

# 아무것도 없는 경로로 들어왔을 때 board라는 함수를 실행시켜줘
urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name="signin"),
    path("user/signup", signup, name="signup")
]
