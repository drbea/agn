from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)
    # Ajoutez d'autres champs selon vos besoins (numéro de téléphone, etc.)