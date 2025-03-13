from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import django.contrib.messages as messages
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User created successfully! {form.cleaned_data.get("username")} can now log in.')
            return redirect('navigation')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

