from django.urls import path
from .views import SumaView, RestaView, MultiplicarView, DividirView

urlpatterns = [
    path ('sumar', SumaView.as_view()),
    path ('restar', RestaView.as_view()),
    path ('multiplicar', MultiplicarView.as_view()),
    path ('dividir', DividirView.as_view())
]