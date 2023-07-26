from django.shortcuts import render

def board(request):
    # 객체의 method가 GET방식이면 rendering 할 것인데 request 객체와 index.html에 rendering을 해줘
    if request.method == "GET":
        context = {
            "title":"안녕 베어유?"
        }

        return render(request, 'page/index.html', context=context)