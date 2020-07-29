from django.urls import path
from core.views import index, teste, MusicianListView

app_name = 'core'

urlpatterns = [
    # FBV
    # (nome do path na url, funcao da views.py que sera chamada, nome da path para outros arquivos)
    path("", index , name="index"),
    path("teste", teste, name="teste"),
    # CBV
    path("musico", MusicianListView.as_view(), name="musician"),
]