from django.shortcuts import render
from .forms import UserRegisterForm
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})