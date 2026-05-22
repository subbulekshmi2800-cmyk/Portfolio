from django.shortcuts import render, redirect
from django.contrib import messages
 
from .models import Skill
from .models import Project
from .forms import ContactForm
from .models import Contact

def home(request):
    projects = Project.objects.all()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Message Sent Successfully!")

            return redirect('/#contact')

    else:
        skills = Skill.objects.all()
        form = ContactForm()
        contacts = Contact.objects.all().order_by('-id')
        projects = Project.objects.all()
        
        context = {
        
        'form': form,
        'contacts': contacts,
        'skills': skills,

        'projects': projects,


    }

    return render(request, 'index.html', context)



   