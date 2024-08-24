import requests
from django.shortcuts import render, redirect
from .models import Jogador, Personagem
from .forms import PersonagemForm, JogadorFormSet
from django.shortcuts import get_object_or_404


def criar_personagem(request):
    response_classes = requests.get("https://www.dnd5eapi.co/api/classes/")
    classes = response_classes.json().get('results', [])

    response_racas = requests.get("https://www.dnd5eapi.co/api/races/")
    racas = response_racas.json().get('results', [])

    jogadores = Jogador.objects.all()  

    if request.method == 'POST':
        form = PersonagemForm(request.POST, classes=classes, racas=racas, jogadores=jogadores)
        if form.is_valid():
            form.save()
            return redirect('lista_personagens')
    else:
        form = PersonagemForm(classes=classes, racas=racas, jogadores=jogadores)

    return render(request, 'adicionar_personagem.html', {'form': form})

def adicionar_jogador(request):
    if request.method == 'POST':
        formset = JogadorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('lista_jogadores')  
    else:
        formset = JogadorFormSet(queryset=Jogador.objects.none())

    return render(request, 'adicionar_jogador.html', {'formset': formset})

def lista_jogadores(request):
    jogadores = Jogador.objects.prefetch_related('personagens').all()
    return render(request, 'lista_jogador.html', {'jogadores': jogadores})

def excluir_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)

    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores') 

    return render(request, 'confirmar_exclusao.html', {'jogador': jogador})

def excluir_personagem(request, pk):
    personagem = get_object_or_404(Personagem, pk=pk)
    if request.method == 'POST':
        personagem.delete()
        return redirect('lista_jogadores')
    return render(request, 'confirmar_exclusao.html', {'objeto': personagem, 'tipo': 'Personagem'})


