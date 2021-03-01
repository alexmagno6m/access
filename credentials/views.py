from django.shortcuts import render
from django.views.generic import ListView
from . models import usuarios

# Create your views here.
def prueba(request):
    return render(request, "test/inicio.html")

class Buscarusuario(ListView):
    template_name = "home/index.html"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        lista = usuarios.objects.filter(
            nip=palabra_clave,
        )
        return lista


