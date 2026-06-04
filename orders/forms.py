from django import forms


class CheckoutForm(forms.Form):
    delivery_address = forms.CharField(
        max_length=255,
        label="Delivery Address"
    )

    delivery_notes = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="Delivery Notes"
    )