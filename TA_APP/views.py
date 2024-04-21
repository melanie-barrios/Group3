from django.shortcuts import render, redirect
from django.views import View
from .models import User, Instructor, TA, Course, LabSection, Supervisor
import TA_APP.functions as functions

class Login(View):
    def get(self, request):
        return render(request, 'login.html',{})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        verify = functions.Login.authenticate(self,str(username),str(password))

        if verify:
            request.session['username'] = username
            return redirect('/')
        else:
            return render(request, "login.html", {"message": "Username or password is incorrect"})


