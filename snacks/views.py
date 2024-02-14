from django.views.generic import ListView
from .models import Snack
from django.views.generic import DetailView

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    
class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html' 