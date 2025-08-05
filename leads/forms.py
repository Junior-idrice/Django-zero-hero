from django import forms


class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    age = forms.IntegerField()