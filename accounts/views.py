from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginFunction(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'utility/index.html')
        else:
            return render(request, 'accounts/login.html', {'msg': 'please check username and password'})
    else:
        return render(request, 'accounts/login.html')

def logoutFunction(request):
    logout(request)
    return render(request, 'utility/index.html')
