from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse
from app.forms import Emailform
from app.models import Userform


# Create your views here.
def home(request):
    # return HttpResponse("Welcome")
    return render(request,'app/home.html')

def mailform(request):
    if request.method == 'GET':
        form = Emailform()

    else:
        usr = Userform()
        form = Emailform(request.POST)
        if form.is_valid():
            usr.From = form.cleaned_data['From']
            usr.To = form.cleaned_data['To']
            usr.subject = form.cleaned_data['subject']
            usr.message = form.cleaned_data['message']
            usr.save()

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER
            recepient_email = [form.cleaned_data['To']]
            send_mail(subject, message, email_from,recepient_email)
            return HttpResponse("Your details registered and mailed to your mail,Thanks")
    form_path='app/emailform.html'
    return render(request,form_path,{'form':form})