from django.shortcuts import render
from django.views.generic import ListView
from core.models import Musician

# Create your views here.

# -- FBV --
def index(request):
    # conjunto de variaveis disponíveis no request
    context = {
        'hello' : 'hello world',
    }
    #            (metodo de chamada da funcao, arquivo renderizado no request, conjunto de dados passados)
    return render(request, 'core/index.html', context)

def teste(request):
    context = {
        'hello' : 'hello world',
    }

    return render(request, 'core/teste.html', context)


# -- CBV --
# READ

# views para renderizar models
class MusicianListView(ListView):   # fazendo requisição GET (postagem de dados)
    # modelo
    model = Musician
    # conjunto de dados disponiveis para o template (por padrao, nome do model no plural)
    context_object_name = 'musicians'
    # qual arquivo sera renderizado
    template_name = 'core/musico.html'
