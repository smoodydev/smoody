from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from smoody.settings import DEFAULT_FROM_EMAIL
from projects.models import Project

# Index
def index(request):
    projects = Project.objects.filter(recommended=True)
    context = {
        "projects": projects
    }
    return render(request, "index.html", context)

# Contact
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
            data = form.cleaned_data
            sent = send_mail(
                data["subject"],
                f"{data['email']} - {data['message']}",
                DEFAULT_FROM_EMAIL,
                [DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            if sent:
                messages.success(request, "Thank you!  Hope to talk to you soon")
                return redirect("/")
            else:
                message.warning(request, "There is currently an issue with this contact form.  Please try again later")
        else:
            messages.info(request, "Looks like a field was incorrect!  Oops!")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"contact_form": form})
