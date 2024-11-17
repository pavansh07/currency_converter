# converter/forms.py
from django import forms

CURRENCY_CHOICES = [
    ('USD', 'USD - United States Dollar'),
    ('EUR', 'EUR - Euro'),
    ('INR', 'INR - Indian Rupee'),
    ('GBP', 'GBP - British Pound'),
    ('JPY', 'JPY - Japanese Yen'),
    # Add more currencies as needed
]

class CurrencyConverterForm(forms.Form):
    amount = forms.FloatField(label='Amount', widget=forms.NumberInput(attrs={'placeholder': 'Enter amount'}))
    from_currency = forms.ChoiceField(label='From Currency', choices=CURRENCY_CHOICES)
    to_currency = forms.ChoiceField(label='To Currency', choices=CURRENCY_CHOICES)
