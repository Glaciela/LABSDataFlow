from django.shortcuts import render

def new_user(request):
    return render(request, 'core/new_user.html')