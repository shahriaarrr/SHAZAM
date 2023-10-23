from django import forms
from .models import Thunder

from django import forms
from .models import Thunder

class ThunderForm(forms.ModelForm):
    class Meta:
        model = Thunder
        fields = ('text',)  # Connect the 'text' field in the model to the form

    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': "Strike your thunder here...",
                "class": "form-control",
            }
        ),
        label="",
    )
