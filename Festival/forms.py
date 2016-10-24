from django import forms

class NameForm(forms.Form):
    product = forms.CharField(label='product.name', max_length=100)