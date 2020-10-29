from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def sign(request):
    return render(request,"Signup.html")

# def password_reset(request):
#     return render(request,"password_reset_form.html")