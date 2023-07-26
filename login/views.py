from django.shortcuts import render


def fo_oldal(request):
    return render(request, 'login/index.html')