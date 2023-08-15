from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    auction = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
