from django import forms
from .models import Thunder

class ThunderForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
            attrs={
                'placeholder': "Strike your thunder here...",
                "class": "form-control",
            }

        ),
        label="",
    )

    class Meta:
        model = Thunder
        exclude = ("user")
