from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 caracteres máximo")
    url = forms.URLField(label = "Tu sitio web", required=False, initial='https://')
    comment = forms.CharField()


