from django.shortcuts import render
from .models import Project
from .models import Skill
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from . import views
# Create your views here.
def home(request):
    projects = Project.objects.all()

    skills = Skill.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (you may need to configure email settings)
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'asikahamedstudy@gmail.com',  # Replace with your email address
                ['blackhatattackers@gmail.com'],  # Replace with the recipient's email address
                fail_silently=False,
            )

            # Redirect to a thank-you page after successful submission
            return HttpResponseRedirect(reverse('thankyou'))
    else:
        form = ContactForm()


# portfolio/views.py
from django.shortcuts import render

def skills(request):
    # You can add any context data you want to pass to the skills template here
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'skills':skills})


def thankyou(request):
    return render(request, 'portfolio/thankyou.html')
