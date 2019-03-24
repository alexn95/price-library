from django.views.generic import ListView

from .models import Store


class HomeView(ListView):
    """
    Home view
    """
    model = Store
    template_name = 'products/home.html'


