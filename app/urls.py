from django.urls import path
from .views import criar_personagem, adicionar_jogador, lista_jogadores, excluir_jogador, excluir_personagem

urlpatterns = [
    path('criar-personagem/', criar_personagem, name='adicionar_personagem'),
    path('criar-jogador/', adicionar_jogador, name='adicionar_jogador'),
    path('lista-jogadores/', lista_jogadores, name='lista_jogadores'),
    path('excluir-jogador/<int:pk>/', excluir_jogador, name='excluir_jogador'),
    path('excluir-personagem/<int:pk>/', excluir_personagem, name='excluir_personagem'),
]