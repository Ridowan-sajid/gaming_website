from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render
from django.contrib import messages

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully created an account!")
            return redirect("/")
    return render(request,'user/user_reg_form.html',{'form':form})

