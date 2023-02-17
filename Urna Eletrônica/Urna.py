# IMPORTANTO AS BIBLIOTECAS.

import graphics as gf
import funções as f
import pygame
from time import sleep

#------------------------------------------------------------------------------------------------------------------------------------------

# Abrindo a janela da graphics.

#------------------------------------------------------------------------------------------------------------------------------------------

win = gf.GraphWin("Urna eletrônica em Python - by: Vitor Freitas", 940, 450)
imgbase = gf.Image(gf.Point(470, 230), "baseurna.gif")
imgbase.draw(win)

#------------------------------------------------------------------------------------------------------------------------------------------

# Criando as estruturas da tela da urna.

#------------------------------------------------------------------------------------------------------------------------------------------

dicas= f.estrutura_dicas()

presidente= f.estrutura_presidente()

governador= f.estrutura_governador()

#------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------

# Abrindo os arquivos, com os dados dos candidatos. (nome/ número do partido)

#------------------------------------------------------------------------------------------------------------------------------------------

# PRESIDENTE

arq = open('candidatos_presidencia.csv', 'r')
lista1 = arq.readlines()
arq.close()
lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3 = []
for elem in lista2:
  x = elem.split(";")  #TIRA O SEPARADOR
  lista3.append(x)
candidatos_p = []
for elem in lista3:
  candidatos_p.append(elem[0]) #LISTA DE candidatos_p
n_partidos_p = []
for elem in lista3:
  n_partidos_p.append(elem[1]) #LISTA COM NUMEROS DOS PARTIDOS

print(n_partidos_p)
opcoes_votos_p=[]
for elem in n_partidos_p:
  opcoes_votos_p.append(elem)
opcoes_votos_p.append('branco') #Aqui adiciona branco e nulo nas opções de votos.
opcoes_votos_p.append('nulo')
print(opcoes_votos_p)

#------------------------------------------------------------------------------------------------------------------------------------------

# GOVERNADOR

arq = open('candidatos_governador.csv', 'r')
lista1 = arq.readlines()
arq.close()
lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3 = []
for elem in lista2:
  x = elem.split(";")  #TIRA O SEPARADOR
  lista3.append(x)
candidatos_g = []
for elem in lista3:
  candidatos_g.append(elem[0]) #LISTA DE NOMES = candidatos_g
n_partidos_g = []
for elem in lista3:
  n_partidos_g.append(elem[1]) #LISTA COM NUMEROS DOS PARTIDOS = n_partidos_g

print(n_partidos_g)
opcoes_votos_g=[]
for elem in n_partidos_g:
  opcoes_votos_g.append(elem)
opcoes_votos_g.append('branco') #Aqui adiciona branco e nulo nas opções de votos.
opcoes_votos_g.append('nulo')
print(opcoes_votos_g)

#------------------------------------------------------------------------------------------------------------------------------------------

# As listas são: 
# n_partidos_ é a lista que contém os NÚMEROS de cada partido.
# candidados_ é a lista com os NOMES de cada candidato. (ambas lista de NUMEROS e NOMES se baseiam no mesmo arquivo.)
# opcoes_votos_ é a lista no qual tem TODAS as opções de votos, que contém basicamente os numeros dos partidos, + as opções BRANCO e NULO.

#------------------------------------------------------------------------------------------------------------------------------------------

# RESULDADOS

arq=open('resultados_presidente.csv', 'r') # Presidente
lista1=arq.readlines()
arq.close()

lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3= []
for elem in lista2:
  lista3.append(elem[-1:])
listaFINAL_contP=[]
for elem in lista3:
  listaFINAL_contP.append(int(elem))
print(listaFINAL_contP)

arq=open('resultados_governador.csv', 'r') # Governador
lista1=arq.readlines()
arq.close()

lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3= []
for elem in lista2:
  lista3.append(elem[-1:])
listaFINAL_contG=[]
for elem in lista3:
  listaFINAL_contG.append(int(elem))
print(listaFINAL_contG)

#------------------------------------------------------------------------------------------------------------------------------------------

cont_votos_p= listaFINAL_contP #Contadores provisórios --> São contadores que contam os votos APENAS durante aquela sessão de votação.
print(cont_votos_p) #           Serve para salvar no arquivo final, os resultados daquela sessão eleitoral.

cont_votos_g= listaFINAL_contG
print(cont_votos_g)

#------------------------------------------------------------------------------------------------------------------------------------------

# Aqui começa o código da urna. 
# Temos um loop principal, e dentro dele as demais funções.

while True: # Loop principal
  #------------------------------------------------------------------------------------------------------------------------------------------

  # PRIMEIRO A VOTAÇÃO PARA PRESIDENTE.

  #------------------------------------------------------------------------------------------------------------------------------------------

  def vota_presidente(cont_p): #Função geral para realizar a votação para presidente.
          
    for elem in dicas: # Desenhando as estruturas.
      elem.draw(win)
    for elem in presidente:
      elem.draw(win)
    cont = 0
    list_img=[]
    list_img_branco=[] #Lista que leva a imagem de voto em branco.
    lista_obj_numpresidente = ['',''] #Lista de leva os numeros na tela.
    n=''

    andamento = True
    while andamento:
      novo = f.digitos(win)
      if novo=='encerra': 
        solicitaSenha=f.encerrar_eleição(list_img, list_img_branco, lista_obj_numpresidente, presidente, win)
        if solicitaSenha== False:
          return ('encerra')
      
      print(novo)
      if novo in ['0','1','2','3','4','5','6','7','8','9'] and cont < len(lista_obj_numpresidente): #Verifica se o que foi digitado no teclado é apenas um número.
        if n=='branco':
          aviso= gf.Text(gf.Point(250,300), "PARA DIGITAR ESTA OPÇÃO,\n CORRIJA A ANTERIOR!")
          aviso.draw(win)
          sleep(2)
          aviso.undraw()

        else:
          n += novo
          lista_obj_numpresidente[cont] = f.geraNumero(novo,cont) #Aqui a lista recebe o objeto do numero para desenhar, no exato indice. (Só há 2 indices na lista.)
          lista_obj_numpresidente[cont].draw(win) #Aqui desenha o numero digitado na tela!!!
          cont += 1
          if cont==len(lista_obj_numpresidente): #Aqui verifica se os espaços de digitos ja foram preenchidos, para enfim verificar se há um candidato com aquele número, e assim desenhar sua foto.
            list_img=f.desenha_cand(n, n_partidos_p, candidatos_p, 'presidente') #Usa a variavel -n- pois ela é a que armazena o número oficial.
            for elem in list_img:
              elem.draw(win)
          print(lista_obj_numpresidente) 

      elif novo == 'branco': #Verifica se o usuario digitou branco
        if len(n) == 0: #Aqui verifica se o usuario digitou algo ANTES de digitar branco.
          n=''
          n+=novo
          cont=0
          while cont < len(lista_obj_numpresidente): #Por aqui faz o procedimento de apagar o número que o usuario digitou anteriormente.
            num = lista_obj_numpresidente[cont] 
            if type(num) != str:  #Aqui ele verifica a lista de objetos dos numeros para serem desenhados, e vê se ela está preenchida, para dar UNDRAW e depois esvaziar a lista.
              num.undraw()
              lista_obj_numpresidente[cont] = '' #Coloca uma string vazia no indice do contador, basicamente esvaziando a lista.
            cont+=1
          cont=0
          for elem in list_img: #Apaga uma possível imagem do candidato, ou voto nulo, ou o proprio branco.
            elem.undraw()
          list_img_branco= f.desenha_cand(n, n_partidos_p, candidatos_p, 'presidente') #Essa lista chama a função que traz uma outra lista com objetos para desenhar, NESSE caso o objeto para desenha branco.
          for elem in list_img_branco:
            elem.draw(win)
          click= f.digitos(win) #Aqui se verifica se foi clicado confirma ou corrige, para que o voto branco seja desfeito ou confirmado
          if click == 'corrige': #Aqui começam os procedimentos de apagar tudo, da tela e das variáveis.
            n=''
            cont=0
            for elem in list_img_branco:
              elem.undraw()
              list_img_branco.remove(elem)
            while cont < len(lista_obj_numpresidente):
              num = lista_obj_numpresidente[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numpresidente[cont] = ''
              cont+=1
            cont=0
          elif click == 'confirma': #Verifica se clicou confirma, e inicia os procedimentos de salvar esse voto em branco.
            if n not in opcoes_votos_p: #Verifica se o que foi digitado (n) está na lista de opções, caso não esteja, (n) deve ser nulo.
              n='nulo'
              indice= opcoes_votos_p.index(n) #Verifica qual o indice do canditado que está sendo votado (nesse caso, o voto em branco)
              cont_p[indice]+=1 #Adiciona +1 no indice do determinado candidato
              print(cont_p)
              cont =0
              n=''
              for elem in list_img:
                elem.undraw()
              for elem in list_img_branco:
                elem.undraw()
              while cont < len(lista_obj_numpresidente): #Apaga as coisas
                num = lista_obj_numpresidente[cont]
                if type(num) != str:      
                  num.undraw()
                  lista_obj_numpresidente[cont] = ''
                cont += 1
              cont = 0
              for elem in presidente:
                elem.undraw()
              for elem in dicas:
                elem.undraw()
              andamento = False
            else:
              indice= opcoes_votos_p.index(n)
              cont_p[indice]+=1
              print(cont_p)
              cont =0
              n=''
              for elem in list_img:
                elem.undraw()
              for elem in list_img_branco:
                elem.undraw()
              while cont < len(lista_obj_numpresidente):
                num = lista_obj_numpresidente[cont]
                if type(num) != str:      
                  num.undraw()
                  lista_obj_numpresidente[cont] = ''
                cont += 1
              cont = 0
              for elem in presidente:
                elem.undraw()
              for elem in dicas:
                elem.undraw()
              andamento = False
        else:
          aviso= gf.Text(gf.Point(250,300), "PARA DIGITAR ESTA OPÇÃO,\n CORRIJA A ANTERIOR!")
          aviso.draw(win)
          sleep(2)
          aviso.undraw()
      elif novo == 'corrige': #Faz os procedimentos de apagar tudo caso o usuario clique corrige.
        cont =0
        n=''
        for elem in list_img:
          elem.undraw()
        for elem in list_img_branco:
          elem.undraw()
        while cont < len(lista_obj_numpresidente):
          num = lista_obj_numpresidente[cont]
          if type(num) != str:      
            num.undraw()
            lista_obj_numpresidente[cont] = ''
          cont += 1
        cont = 0
      
      elif novo == 'confirma':
        if len(n)==1:
          pega_malicia= gf.Text(gf.Point(300, 250),'Voto inválido. \nDigite corretamente ou aperte "BRANCO".') #Verifica se usuario digitou apenas um nmr, dps pede para digitar mais.
          pega_malicia.setSize(15)
          pega_malicia.draw(win)
          sleep(1)
          pega_malicia.undraw()
        elif len(n)>0: #Verifica se o usuario nao clicou confirma sem digitar nada.
          if n not in opcoes_votos_p:
            n='nulo'
            indice= opcoes_votos_p.index(n)
            cont_p[indice]+=1
            cont =0
            n=''
            for elem in list_img:
              elem.undraw()
            for elem in list_img_branco:
              elem.undraw()
            while cont < len(lista_obj_numpresidente):
              num = lista_obj_numpresidente[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numpresidente[cont] = ''
              cont += 1
            cont = 0
            for elem in presidente:
              elem.undraw()
            for elem in dicas:
              elem.undraw()
            andamento = False
          else:
            indice= opcoes_votos_p.index(n)
            cont_p[indice]+=1
            cont =0
            n=''
            for elem in list_img:
              elem.undraw()
            for elem in list_img_branco:
              elem.undraw()
            while cont < len(lista_obj_numpresidente):
              num = lista_obj_numpresidente[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numpresidente[cont] = ''
              cont += 1
            cont = 0
            for elem in presidente:
              elem.undraw()
            for elem in dicas:
              elem.undraw()
            andamento = False
        else:
          aviso= gf.Text(gf.Point(200,300), "Por favor, digite algo...")
          aviso.draw(win)
          sleep(1.4)
          aviso.undraw()
    return (cont_p)

  resultados_presidente=vota_presidente(cont_votos_p) # Armazena o resultado da votação em uma variável.
  if resultados_presidente== 'encerra': # Se o usuario clicar no botão encerra.
    break

  P=f.arqFinal_candidato(resultados_presidente, opcoes_votos_p) # Aqui escreve oficialmente em um arquivo.
  arq= open('resultados_presidente.csv', 'w')
  arq.write(P)
  arq.close()

  sleep(0.1)

  f.anima_grava(win)
  pygame.mixer.init()
  pygame.mixer.music.load('voto_do_meio.wav')
  pygame.mixer.music.play()

  sleep(0.5)

#------------------------------------------------------------------------------------------------------------------------------------------

# TUDO SE REPETE IGUAL PARA GOVERNADOR.

#------------------------------------------------------------------------------------------------------------------------------------------

  def vota_governador(cont_g):

    for elem in dicas:
      elem.draw(win)
    for elem in governador:
      elem.draw(win)
    cont = 0
    list_img=[]
    list_img_branco=[]
    lista_obj_numGovernador = ['','']
    n=''

    andamento = True
    while andamento:
      novo = f.digitos(win)
      print(novo)
      if novo=='encerra':
        solicitaSenha=f.encerrar_eleição(list_img, list_img_branco, lista_obj_numGovernador, governador, win)
        if solicitaSenha== False:
          return ('encerra')
      if novo in ['0','1','2','3','4','5','6','7','8','9'] and cont < len(lista_obj_numGovernador):
        if n=='branco':
          aviso= gf.Text(gf.Point(250,300), "PARA DIGITAR ESTA OPÇÃO,\n CORRIJA A ANTERIOR!")
          aviso.draw(win)
          sleep(2)
          aviso.undraw()
        else:
          n += novo
          lista_obj_numGovernador[cont] = f.geraNumero(novo,cont)    
          lista_obj_numGovernador[cont].draw(win)
          cont += 1
          if cont==len(lista_obj_numGovernador):
            list_img=f.desenha_cand(n, n_partidos_g, candidatos_g, 'governador')
            for elem in list_img:
              elem.draw(win)
          print(lista_obj_numGovernador) 

      elif novo == 'branco':
        if len(n) == 0:
          n=''
          n+=novo
          cont=0
          while cont < len(lista_obj_numGovernador):
            num = lista_obj_numGovernador[cont]
            if type(num) != str:      
              num.undraw()
              lista_obj_numGovernador[cont] = ''
            cont+=1
          cont=0
          for elem in list_img:
            elem.undraw()
          list_img_branco= f.desenha_cand(n, n_partidos_g, candidatos_g, 'governador')
          for elem in list_img_branco:
            elem.draw(win)
          click= f.digitos(win)
          if click == 'corrige':
            n=''
            cont=0
            for elem in list_img_branco:
              elem.undraw()
              list_img_branco.remove(elem)
            while cont < len(lista_obj_numGovernador):
              num = lista_obj_numGovernador[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numGovernador[cont] = ''
              cont+=1
            cont=0
          elif click == 'confirma':
            if n not in opcoes_votos_g:
              n='nulo'
              indice= opcoes_votos_g.index(n)
              cont_g[indice]+=1
              print(cont_g)
              cont =0
              n=''
              for elem in list_img:
                elem.undraw()
              for elem in list_img_branco:
                elem.undraw()
              while cont < len(lista_obj_numGovernador):
                num = lista_obj_numGovernador[cont]
                if type(num) != str:      
                  num.undraw()
                  lista_obj_numGovernador[cont] = ''
                cont += 1
              cont = 0
              for elem in governador:
                elem.undraw()
              for elem in dicas:
                elem.undraw()
              andamento = False
            else:
              indice= opcoes_votos_g.index(n)
              cont_g[indice]+=1
              print(cont_g)
              cont =0
              n=''
              for elem in list_img:
                elem.undraw()
              for elem in list_img_branco:
                elem.undraw()
              while cont < len(lista_obj_numGovernador):
                num = lista_obj_numGovernador[cont]
                if type(num) != str:      
                  num.undraw()
                  lista_obj_numGovernador[cont] = ''
                cont += 1
              cont = 0
              for elem in governador:
                elem.undraw()
              for elem in dicas:
                elem.undraw()
              andamento = False
        else:
          aviso= gf.Text(gf.Point(250,300), "PARA DIGITAR ESTA OPÇÃO,\n CORRIJA A ANTERIOR!")
          aviso.draw(win)
          sleep(2)
          aviso.undraw()
      elif novo == 'corrige':
        cont =0
        n=''
        for elem in list_img:
          elem.undraw()
        for elem in list_img_branco:
          elem.undraw()
        while cont < len(lista_obj_numGovernador):
          num = lista_obj_numGovernador[cont]
          if type(num) != str:      
            num.undraw()
            lista_obj_numGovernador[cont] = ''
          cont += 1
        cont = 0
      
      elif novo == 'confirma':
        if len(n)==1:
          pega_malicia= gf.Text(gf.Point(300, 250),'Voto inválido. \nDigite corretamente ou aperte "BRANCO".') #Verifica se usuario digitou apenas um nmr, dps pede para digitar mais.
          pega_malicia.setSize(15)
          pega_malicia.draw(win)
          sleep(1)
          pega_malicia.undraw()
        elif len(n)>0:
          if n not in opcoes_votos_g:
            n='nulo'
            indice= opcoes_votos_g.index(n)
            cont_g[indice]+=1
            cont =0
            n=''
            for elem in list_img:
              elem.undraw()
            for elem in list_img_branco:
              elem.undraw()
            while cont < len(lista_obj_numGovernador):
              num = lista_obj_numGovernador[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numGovernador[cont] = ''
              cont += 1
            cont = 0
            for elem in governador:
              elem.undraw()
            for elem in dicas:
              elem.undraw()
            andamento = False
          else:
            indice= opcoes_votos_g.index(n)
            cont_g[indice]+=1
            cont =0
            n=''
            for elem in list_img:
              elem.undraw()
            for elem in list_img_branco:
              elem.undraw()
            while cont < len(lista_obj_numGovernador):
              num = lista_obj_numGovernador[cont]
              if type(num) != str:      
                num.undraw()
                lista_obj_numGovernador[cont] = ''
              cont += 1
            cont = 0
            for elem in governador:
              elem.undraw()
            for elem in dicas:
              elem.undraw()
            andamento = False
        else:
          aviso= gf.Text(gf.Point(200,300), "Por favor, digite algo...")
          aviso.draw(win)
          sleep(1.4)
          aviso.undraw()
    return (cont_g)

  resultados_governador= vota_governador(cont_votos_g)
  if resultados_governador== 'encerra':
    break

  G=f.arqFinal_candidato(resultados_governador, opcoes_votos_g)
  arq= open('resultados_governador.csv','w')
  arq.write(G)
  arq.close()


  sleep(0.1)
  f.anima_grava(win)
  pygame.mixer.init()
  pygame.mixer.music.load('voto_final.wav')
  pygame.mixer.music.play()
  sleep(0.5)
  #------------------------------------------------------------------------------------------------------------------------------------------

  # FIM DAS VOTAÇÕES, FINALIZANDO A SESSÃO.

  #------------------------------------------------------------------------------------------------------------------------------------------


  fim= gf.Text(gf.Point(300,200),'FIM')
  fim.setSize(150) #!!!ATENÇÃO!!! -> NA BIBLIOTECA GRAPHICS NATIVA O TAMANHO MÁXIMO É 36!(Este tamanho só funciona na graphics alterada.)
  fim.draw(win)
  sleep(3)
  fim.undraw()
  sleep(0.5)

  # FIM.

#------------------------------------------------------------------------------------------------------------------------------------------

#FAZENDO O ARQUIVO FINAL

#O arquivo mostra a quantidade dos votos em cada candidato, para presidente e governador, e também suas porcentagens.

#------------------------------------------------------------------------------------------------------------------------------------------

# Primeiro salvo os dados dos arquivos em variáveis.

arq=open('resultados_presidente.csv', 'r') # Para presidente.
lista1=arq.readlines()
arq.close()

lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3= []
for elem in lista2:
  lista3.append(elem[-1:])
listaFINAL_resultP=[]
for elem in lista3:
  listaFINAL_resultP.append(int(elem))
print(listaFINAL_resultP)

arq=open('resultados_governador.csv', 'r') # Agora para governador.
lista1=arq.readlines()
arq.close()

lista2 = []
for elem in lista1:
  lista2.append(elem[0:-1])
lista3= []
for elem in lista2:
  lista3.append(elem[-1:])
listaFINAL_resultG=[]
for elem in lista3:
  listaFINAL_resultG.append(int(elem))
print(listaFINAL_resultG)

# Agora, é realizado a SOMA do resultado da sessão eleitoral com os dados anteriores dos arquivos, obtendo a quantia total atualizada.

quantiaTotalP=0
for elem in listaFINAL_resultP: # P = Presidente
  quantiaTotalP+=elem
print(quantiaTotalP)

quantiaTotalG=0
for elem in listaFINAL_resultG: # G = Governador
  quantiaTotalG+=elem
print(quantiaTotalG)

# Aqui é feito as porcentagens, com base nos novos dados obtidos.

lista_porcentagensP=[]
while len(lista_porcentagensP) < len(listaFINAL_resultP): 
  cont=0
  while cont<len(listaFINAL_resultP):#                    Presidente
    quotient = listaFINAL_resultP[cont] / quantiaTotalP
    percent = quotient * 100
    lista_porcentagensP.append(percent)
    cont+=1
print(lista_porcentagensP)

lista_porcentagensG=[]
while len(lista_porcentagensG) < len(listaFINAL_resultG):
  cont=0
  while cont<len(listaFINAL_resultG):#                     Governador
    quotient = listaFINAL_resultG[cont] / quantiaTotalG
    percent = quotient * 100
    lista_porcentagensG.append(percent)
    cont+=1
print(lista_porcentagensG)

# A partir daqui, é feito o arquivo final com todos os dados, para presidente e governador, com seus votos e porcentagens.

arq=open('arquivoFINAL.txt','w')
stringfinal=f'O total de votos para presidente: {quantiaTotalP}.\n'
cont=0
cont1=0
cont2=0
while cont<len(opcoes_votos_p):
  stringfinal+= f'{opcoes_votos_p[cont]}: {listaFINAL_resultP[cont2]} - {int(lista_porcentagensP[cont1])}%\n'
  cont+=1
  cont1+=1
  cont2+=1
stringfinal+=f'O total de votos para governador: {quantiaTotalG}.\n'
cont=0
cont1=0
cont2=0
print(stringfinal)
while cont<len(opcoes_votos_g):
  stringfinal+= f'{opcoes_votos_g[cont]}: {listaFINAL_resultG[cont2]} - {int(lista_porcentagensG[cont1])}%\n'
  cont+=1
  cont1+=1
  cont2+=1
print(stringfinal) # Mostrando no terminal.


var_final= arq.write(stringfinal)
arq.close() # Fechando os arquivos e, fim.

#------------------------------------------------------------------------------------------------------------------------------------------

# FIM

#------------------------------------------------------------------------------------------------------------------------------------------

if win.getMouse():
  win.close()

# Ass: Vitor de Ávila Freitas.