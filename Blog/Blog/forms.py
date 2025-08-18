
from django import forms

class ContactForm(forms.Form):
    nombre  = forms.CharField(label="Nombre", max_length=80)
    email   = forms.EmailField(label="Correo electrónico")
    asunto  = forms.CharField(label="Asunto (opcional)", max_length=120, required=False)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={"rows": 6}))

    # estética/UX
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.update({
                "class": "contact-input",
                "placeholder": f.label,
            })
