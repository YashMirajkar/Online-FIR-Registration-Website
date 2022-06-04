from django import forms
from .models import AttachmentModel

class ImageForm(forms.ModelForm):
    class Meta:
        model=AttachmentModel
        fields=("sign","aaddhar_copy")