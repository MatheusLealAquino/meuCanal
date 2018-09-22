from django.shortcuts import render

def pagina_login(request):
    return render(request, 'login/pagina_login.html')
