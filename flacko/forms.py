from django import forms
from .models import Lord, Jordy


class LordForm(forms.ModelForm):
    class Meta:
        model = Lord
        fields = ["name", "surname", "personal_thoughts"]


class JordyForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Jordy
        fields = ['title', 'description', 'lord', 'genre', 'releaste_date', 'personal_thoughts']