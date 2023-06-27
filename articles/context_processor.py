from .models import Currency

def currency_renderer(request):
    return {'currency': Currency.objects.first()}