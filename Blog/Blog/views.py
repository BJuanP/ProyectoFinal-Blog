

from django.shortcuts import render

from apps.articulos.models import Articulo


from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm



def Home(request):
    # Artículo destacado (si no hay, cae al más reciente)
    articulo_destacado = (
        Articulo.objects.filter(destacado=True).order_by("-creado").first()
        or Articulo.objects.order_by("-creado").first()
    )

    # Últimos 3, excluyendo el destacado para no repetir
    ultimos_articulos = (
        Articulo.objects.exclude(pk=getattr(articulo_destacado, "pk", None))
        .order_by("-creado")[:4]
    )

    es_moderador = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Moderador").exists()
    )

    ctx = {
        "articulo_destacado": articulo_destacado,
        "ultimos_articulos": ultimos_articulos,
        "es_moderador": es_moderador,
    }
    return render(request, "home.html", ctx)


TEAM = [
    {"nombre": "Bravo Juan Pablo", "rol": "Desarrollo & Diseño", "email": "bravojuanpablo153@gmail.com"},
    {"nombre": "César Lautaro Obregón", "rol": "Desarrollo & Diseño"},
    {"nombre": "Massad Lucas Yael", "rol": "Desarrollo & Diseño", "email": "massadlucas@gmail.com"},
    {"nombre": "Lazarczuk Carlos Agustin", "rol": "Desarrollo & Diseño"},
]


def acerca(request):
    
    return render(request, "acerca.html", {})




def contacto(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        subject = data["asunto"] or "Nuevo mensaje de contacto"
        body = f"Nombre: {data['nombre']}\nEmail: {data['email']}\n\n{data['mensaje']}"
        to_email = getattr(settings, "CONTACT_RECIPIENT_EMAIL",
                           getattr(settings, "DEFAULT_FROM_EMAIL", None))
        try:
            send_mail(subject, body,
                      getattr(settings, "DEFAULT_FROM_EMAIL", data["email"]),
                      [to_email] if to_email else [])
            messages.success(request, "¡Gracias! Tu mensaje fue enviado.")
            return redirect("contacto")
        except BadHeaderError:
            messages.error(request, "Error en el encabezado del correo.")
    return render(request, "contacto.html", {"form": form, "team": TEAM})