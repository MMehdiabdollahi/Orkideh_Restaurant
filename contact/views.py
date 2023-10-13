from django.shortcuts import render
from .forms import ContactForm

def contact_us(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()

    context = {
        "contactform":contact_form,
    }

    return render(request,"contact/contact.html",context)