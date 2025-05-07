from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Tweek
from .forms import TweekForm
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
#Home Page
def home(request):
    if request.user.is_authenticated:
        return redirect('tweek_list')
    else:
        return redirect('tweek_list')



def tweek_list(request):
    tweeks = Tweek.objects.all().order_by('-created_at')
    return render(request,'componant/tweek_list.html',{'tweeks':tweeks})


@csrf_protect
@login_required
def tweek_create(request):
    if request.method == "POST":
        form = TweekForm(request.POST,request.FILES)
        if form.is_valid():
            tweek = form.save(commit=False)
            tweek.user = request.user
            tweek.save()
            return redirect("/tweeks")
    else:
        form = TweekForm()
    return render(request,'componant/add_tweek.html',{'form':form})
    
@csrf_protect
@login_required
def tweek_edit(request, tweek_id):
    tweek = get_object_or_404(Tweek, pk=tweek_id, user = request.user)
    if request.method == 'POST':
        form = TweekForm(request.POST, request.FILES, instance=tweek)
        if form.is_valid():
            tweek = form.save(commit=False)
            tweek.user = request.user
            tweek.save()
            return redirect('/tweeks')
    else:
        form = TweekForm(instance=tweek)
    return render(request,'componant/tweek_form.html',{'form':form})


@csrf_protect
@login_required
def tweek_delete(request,tweek_id):
    tweek_node = get_object_or_404(Tweek,pk=tweek_id,user=request.user)
    if request.method == 'POST':
        tweek_node.delete()
        return redirect('/tweeks')
    return render(request,'componant/tweek_confirm_delete.html',{'tweek':tweek_node})



@csrf_protect
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_photo = form.cleaned_data['user_photo']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('/tweeks')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})



@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual homepage name
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')  # Create this template



def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')