from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    nivel = models.IntegerField()
    jogador = models.ForeignKey(Jogador, related_name='personagens', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Classe: {self.classe}, Nível: {self.nivel}"