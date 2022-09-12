from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')

def dc(request):
    return render(request, 'main/dc.html')

def prob(request):
    return render(request, 'main/prob.html')

def xman(request):
    return render(request, 'main/xman.html')

def fantastic(request):
    return render(request, 'main/fantastic.html')

def stgal(request):
    return render(request, 'main/stgal.html')

def iron(request):
    return render(request, 'main/iron.html')

def hulk(request):
    return render(request, 'main/hulk.html')

def com1(request):
    return render(request, 'main/comspider1/com1.html')

def com2(request):
    return render(request, 'main/comspider1/com2.html')

def com3(request):
    return render(request, 'main/comspider1/com3.html')

def com4(request):
    return render(request, 'main/comspider1/com4.html')

def com5(request):
    return render(request, 'main/comspider1/com5.html')

def com6(request):
    return render(request, 'main/comspider1/com6.html')

def com7(request):
    return render(request, 'main/comspider1/com7.html')

def com8(request):
    return render(request, 'main/comspider1/com8.html')

def com9(request):
    return render(request, 'main/comspider1/com9.html')

def com10(request):
    return render(request, 'main/comspider1/com10.html')

def com11(request):
    return render(request, 'main/comspider1/com11.html')

def com12(request):
    return render(request, 'main/comspider1/com12.html')

def com13(request):
    return render(request, 'main/comspider1/com13.html')

def com1a(request):
    return render(request, 'main/comspider2/com1a.html')

def com2a(request):
    return render(request, 'main/comspider2/com2a.html')

def com3a(request):
    return render(request, 'main/comspider2/com3a.html')

def com4a(request):
    return render(request, 'main/comspider2/com4a.html')

def com5a(request):
    return render(request, 'main/comspider2/com5a.html')

def com6a(request):
    return render(request, 'main/comspider2/com6a.html')

def com7a(request):
    return render(request, 'main/comspider2/com7a.html')

def com8a(request):
    return render(request, 'main/comspider2/com8a.html')

def com9a(request):
    return render(request, 'main/comspider2/com9a.html')

def com10a(request):
    return render(request, 'main/comspider2/com10a.html')

def com11a(request):
    return render(request, 'main/comspider2/com11a.html')

def com12a(request):
    return render(request, 'main/comspider2/com12a.html')

def com13a(request):
    return render(request, 'main/comspider2/com13a.html')

def com14a(request):
    return render(request, 'main/comspider2/com14a.html')

def com15a(request):
    return render(request, 'main/comspider2/com15a.html')

def cap(request):
    return render(request, 'main/cap.html')

def panter(request):
    return render(request, 'main/panter.html')

def tor(request):
    return render(request, 'main/tor.html')

def spider(request):
    return render(request, 'main/spider.html')

def friends(request):
    tasks = Task.objects.all()
    return render(request, 'main/friends.html', {'title': 'Главная страница сайта', 'text': tasks})

def ris(request):
    return render(request, 'main/ris.html')

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/friends')
        else:
            error = "Форма неверна"
    form = TaskForm()
    context = {
        "form" : form
    }
    return render(request, 'main/create.html', context)