from django import forms
from assign_db.models import Destination


class destForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields = ('name','doc','desc')
