# converter/views.py
from django.shortcuts import render
from .forms import CurrencyConverterForm
from .exchange_rate import get_exchange_rates

def convert_currency(request):
    result = None
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']

            rates = get_exchange_rates()
            if from_currency in rates and to_currency in rates:
                from_rate = rates[from_currency]
                to_rate = rates[to_currency]
                converted_amount = (amount / from_rate) * to_rate
                result = f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}."
    else:
        form = CurrencyConverterForm()

    return render(request, 'convert.html', {'form': form, 'result': result})
