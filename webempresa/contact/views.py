from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print("Tipo de peticion: {}".format(request.method)) 
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Suponemos que todo esta bien
            #return redirect('/contact/?ok')
            #return redirect(reverse('contact')+"?ok")
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                    "La cafetiera nuevo mensaje de contacto",
                    "De {} <{}>\n\nEscribio\n\n{}".format(name,email,content),
                    "no-contestar@inbox.mailtrap.io",
                    ["davnax9@gmail.com"],
                    reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien bien resireccionamos a fail.
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no salio bien resireccionamos a fail.
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form':contact_form})