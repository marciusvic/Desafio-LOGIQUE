from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/homeAuthenticated  .html', {'usuario': request.user})
    else:
        return render(request, 'usuarios/home.html')