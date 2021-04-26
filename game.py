#aplicaçãoPOO
#jogo da forca

# -*- coding: UTF-8 -*-

import random

#cada erro significa cada parte do boneco a aparecer
#cada visualização do corpo pode ser um elemento de uma lista, sendo assim:
corpo = ['''
  -----+
 |	|
	|
	|
	|
	|
 ============
''','''
  -----+
 |	|
 O	|
	|
	|
	|
 ============
''','''
  -----+
 |	|
 O	|
 |	|
	|
	|
 ============
''','''
  -----+
 |	|
 O	|
/|	|
	|
	|
 ============
''','''
  -----+
 |	|
 O	|
/|\	|
	|
	|
 ============
''','''
  -----+
 |	|
 O	|
/|\	|
/	|
	|
 ============
''','''
  -----+
 |	|
 O	|
/|\	|
/ \	|
	|
 ============
'''
]

class Forca:
#	construtor
	def __init__(self, palavra):
		self.palavra= palavra
		self.erradas = []
		self.adivinhadas = []

#	para adivinhar letra
	def adivinhar(self, letra):
		self.letra = self.palavra.split()
		if letra in self.palavra and letra not in self.adivinhadas:
			self.adivinhadas.append(letra)
		elif letra not in self.palavra and letra not in self.erradas:
			self.erradas.append(letra)
		else:
			return False
		return True

#	quando perder
	def perdeu(self):
		return self.venceu() or (len(self.erradas) == 6)

#	quando vencer
	def venceu(self):
		if '_' not in self.esconderP():
			return True
		return False

	# Método para não mostrar a letra
	def esconderP(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.adivinhadas:
				rtn += '_'
			else:
				rtn += letra
		return rtn
#	situacao do boneco
	def status(self):
		print (corpo[len(self.erradas)])
		print ('\nPalavra: ' + self.esconderP())
		print ('\nLetras erradas: ',) 
		for letra in self.erradas:
			print (letra,) 
		print ()
		print ('Letras corretas: ',)
		for letra in self.adivinhadas:
			print (letra,)
		print ()


#escolher uma palavra aleatoriamente
def escolhaP():
	with open('palavras.txt','r') as f:
		bancoPalavras = f.readlines()
#		seleciona aleatoriamente uma palavra do banco
		return bancoPalavras[random.randint(0,len(bancoPalavras))].strip()
#executor principal
def main():
#	objeto
	jogo = Forca(escolhaP())

	# Enquanto o jogo não tiver terminado, mostra o status, solicita uma letra e faz a leitura do caracter
	while not jogo.perdeu():
		jogo.status()
		tentativa = input('\nDigite uma letra: ')
		jogo.adivinhar(tentativa)

	# Verifica o status do jogo
	jogo.status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.venceu():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu. A palavra era ' + jogo.palavra)

# Executa o programa		
if __name__ == "__main__":
	main()
