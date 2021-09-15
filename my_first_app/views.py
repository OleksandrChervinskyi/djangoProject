from django.shortcuts import render

# Create your views here.
user_list = ['Max', 'Ira', 'Olex']


def home(request):
    return render(request, 'home.html', {'context': 'text in context'})


def users(request):
    return render(request, 'users.html', {'users': user_list})


def test(request, age, name):
    user_list.append(name)
    return render(request, 'test.html', {'age': age, 'name': name})
