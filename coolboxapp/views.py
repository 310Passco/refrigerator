from django.shortcuts import render, redirect
from django.views.generic import  DeleteView, CreateView
from .models import Food, CustomUser
from .forms import FoodForm, SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView


def foodCreate(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,'create.html')
    else:
        getuser = CustomUser.objects.get(pk=request.user.pk)
        form = FoodForm()
        context = {'user':getuser}
        return render(request,'create.html',context)
    

def top_view(request):
  return render(request, 'top.html')


@login_required
def list_view(request):
      getuser = CustomUser.objects.get(pk=request.user.pk)
      user_food = Food.objects.filter(owner=getuser)
      user_food = user_food.order_by('deadline').reverse
      context = {'foods': user_food}
      return render(request, 'list.html', context)

def count_minus(request,pk):
    object = Food.objects.get(pk=pk)
    if object.quantity >= 2:    
        object.quantity -= 1
        object.save()
        return redirect('list')
    else:
        return redirect('delete', object.pk)
    

class Food_Delete(DeleteView):
    model = Food
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class SignUpView(CreateView):
    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('list')
        return render(request, 'signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        return render(request, 'signup.html', {'form': form})

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect('list')


