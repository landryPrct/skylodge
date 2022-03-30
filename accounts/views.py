from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from accounts.forms import CustomerSignUpForm, ManagerSignUpForm
from .models import User


class Customer_register(CreateView):
    model=User
    form_class = CustomerSignUpForm
    template_name = "../templates/customer_register.html"

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect("/")


class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = "../templates/manager_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :

                login(request,user)

                request.session['is_manager'] =True
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


