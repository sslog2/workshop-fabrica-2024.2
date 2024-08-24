from django import forms
from .models import Personagem, Jogador
from django.forms import modelformset_factory

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'email']

JogadorFormSet = modelformset_factory(Jogador, form=JogadorForm)

class PersonagemForm(forms.ModelForm):
    classe = forms.ChoiceField(choices=[])  
    raca = forms.ChoiceField(choices=[])
    nivel = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 21)])
    class Meta:
        model = Personagem
        fields = ['nome', 'classe', 'raca', 'nivel', 'jogador']

    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes', [])  
        racas = kwargs.pop('racas', [])
        jogadores = kwargs.pop('jogadores', [])  
        super().__init__(*args, **kwargs)
        self.fields['classe'].choices = [(c['index'], c['name']) for c in classes]
        self.fields['raca'].choices = [(r['index'], r['name']) for r in racas]
        self.fields['jogador'].queryset = Jogador.objects.filter(id__in=[j.id for j in jogadores])

