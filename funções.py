from playsound import playsound
import pygame
import graphics as gf
from time import sleep

def estrutura_dicas(): #Função que desenha as dicas na tela da urna
  list=[]
  dica1 = gf.Text(gf.Point(408, 348), "Aperte a tecla:")
  dica1.setSize(8)
  list.append(dica1)
  dica2 = gf.Text(gf.Point(470, 364), "CONFIRMA para CONFIRMAR este voto.")
  dica2.setSize(8)
  list.append(dica2)
  dica3 = gf.Text(gf.Point(461, 380), "CORRIGE para REINICIAR este voto.")
  dica3.setSize(8)
  list.append(dica3)
  return (list)

def estrutura_presidente(): #Função que desenha as caixas e o nome "presidente"
  list=[]
  presidente = gf.Text(gf.Point(106, 120), "PRESIDENTE")
  presidente.setSize(15)
  list.append(presidente)
  box1 = gf.Rectangle(gf.Point(60, 140), gf.Point(95, 180))
  box1.setWidth(1.5)
  list.append(box1)
  box2 = gf.Rectangle(gf.Point(100, 140 ), gf.Point(135, 180))
  box2.setWidth(1.5)
  list.append(box2)
  return(list)

def estrutura_governador(): #Função que desenha as caixas de digito e o nome "governador"
  list=[]
  governador = gf.Text(gf.Point(106, 120), "GOVERNADOR")
  governador.setSize(15)
  list.append(governador)
  box1 = gf.Rectangle(gf.Point(60, 140), gf.Point(95, 180))
  box1.setWidth(1.5)
  list.append(box1)
  box2 = gf.Rectangle(gf.Point(100, 140 ), gf.Point(135, 180))
  box2.setWidth(1.5)
  list.append(box2)
  return(list)

def digitos(win): #Funçao do teclado da urna
  
  digitados= ''
  while True:
    if len(digitados)>0:
      return (digitados)
    click = win.getMouse()
    if 664 < click.getX() < 716 and 130 < click.getY() < 170:  #BOTÃO 1
      digitados+='1'

    elif 732 < click.getX() < 783 and 130 < click.getY() < 170:  #BOTÃO 2
      digitados+='2'

    elif 802 < click.getX() < 854 and 130 < click.getY() < 170:  #BOTÃO 3
      digitados+='3'

    elif 664 < click.getX() < 716 and 188 < click.getY() < 226:  #BOTÃO 4
      digitados+='4'

    elif 732 < click.getX() < 783 and 188 < click.getY() < 226:  #BOTÃO 5
      print('5')
      digitados+='5'

    elif 802 < click.getX() < 854 and 188 < click.getY() < 226:  #BOTÃO 6
      digitados+='6'

    elif 664 < click.getX() < 716 and 248 < click.getY() < 287:  #BOTÃO 7
      digitados+='7'

    elif 732 < click.getX() < 783 and 248 < click.getY() < 287:  #BOTÃO 8
      digitados+='8'

    elif 802 < click.getX() < 854 and 248 < click.getY() < 287:  #BOTÃO 9
      digitados+='9'

    elif 732 < click.getX() < 783 and 302 < click.getY() < 344:  #BOTÃO 0
      digitados+='0'

    elif 634 < click.getX() < 704 and 359 < click.getY() < 397:  #BOTÃO BRANCO
      print('BRANCO')
      digitados=''
      digitados+= 'branco'
  
    elif 723 < click.getX() < 793 and 359 < click.getY() < 397:  #BOTÃO CORRIGE
      print('CORRIGE')
      digitados+= 'corrige'
  
    elif 813 < click.getX() < 883 and 348 < click.getY() < 397:  #BOTÃO CONFIRMA
      print('CONFIRMA')
      digitados+='confirma'

    elif 38 < click.getX() < 107 and 353 < click.getY() < 390:  #BOTÃO CONFIRMA
      print('ENCERRA')
      digitados+='encerra'
        
def geraNumero(num,posicao): #Função que gera o OBJETO do numero que será desenhado na tela.
  nmr= gf.Text(gf.Point(77+posicao*40,162), num)
  nmr.setSize(30)
  print(nmr)
  return(nmr)

def desenha_cand(num, n_part, cand, cargo): #Função que desenha o nome e a foto do candidado caso o numero seja válido, caso não seja, coloca branco ou nulo.
  lista_obj_imgCANDIDATO=[]
  if num == 'branco':
    branco= gf.Text(gf.Point(360,200), "VOTO EM BRANCO")
    branco.setSize(30)
    lista_obj_imgCANDIDATO.append(branco)
    return (lista_obj_imgCANDIDATO)
  elif num in n_part:
    indice= n_part.index(num)
    if cargo == 'governador': 
      print('ue')
      foto= gf.Image(gf.Point(500, 176), f"{cand[indice]}.gif")
      lista_obj_imgCANDIDATO.append(foto)
    else:
      print('uuuuue')
      foto= gf.Image(gf.Point(500, 176), f"{num}.gif")
      lista_obj_imgCANDIDATO.append(foto)
    nome= gf.Text(gf.Point(500,300), cand[indice])
    nome.setSize(20)
    lista_obj_imgCANDIDATO.append(nome)
    return (lista_obj_imgCANDIDATO)
  else:
    nulo= gf.Text(gf.Point(360,200), "VOTO NULO")
    nulo.setSize(30)
    lista_obj_imgCANDIDATO.append(nulo)
    return (lista_obj_imgCANDIDATO)

def encerrar_eleição(Limg, LimgB, LobjNP, cargo, win): #Função do botão encerra, no qual solicita a senha e faz as demais verificações.
    for elem in cargo:
        elem.undraw()
    cont =0
    n=''
    for elem in Limg:
        elem.undraw()
    for elem in LimgB:
        elem.undraw()
    while cont < len(LobjNP):
        num = LobjNP[cont]
        if type(num) != str:      
            num.undraw()
        LobjNP[cont] = ''
        cont += 1
    cont = 0
    encerrar= gf.Text(gf.Point(300,200), "DIGITE A SENHA\n DE ENCERRAMENTO")
    encerrar.setSize(30)
    encerrar.draw(win)
    senha_digitada=''
    senha_encerra='1313'
    ast1=gf.Text(gf.Point(270,300),'*')
    ast1.setSize(30)
    ast2=gf.Text(gf.Point(290,300),'*')
    ast2.setSize(30)
    ast3=gf.Text(gf.Point(310,300),'*')
    ast3.setSize(30)
    ast4=gf.Text(gf.Point(330,300),'*')
    ast4.setSize(30)
    asterisco_pass=[ast1,ast2,ast3,ast4]
    while True:
        contador_pass=0
        while len(senha_digitada)<len(senha_encerra):
            digito_encerra=digitos(win)
            if digito_encerra in ['0','1','2','3','4','5','6','7','8','9']:
                asterisco_pass[contador_pass].draw(win)
                contador_pass+=1
                senha_digitada+=digito_encerra
        sleep(0.5)  
        if senha_digitada==senha_encerra:
            encerrar.undraw()
            for elem in asterisco_pass:
                elem.undraw()
            return(False)
        else:
            digito_encerra=''
            senha_digitada=''
            print("aqui",asterisco_pass)
            for elem in asterisco_pass:
                elem.undraw()
            avisoDe_senhaErrada= gf.Text(gf.Point(300,280), "SENHA ERRADA...\n DIGITE NOVAMENTE.")
            avisoDe_senhaErrada.draw(win)
            sleep(1)
            avisoDe_senhaErrada.undraw()

def anima_grava(win):
  textinho= gf.Text(gf.Point(303,200), "GRAVANDO")
  textinho.setSize(30)
  textinho.draw(win)
  retangulo_borda= gf.Rectangle(gf.Point(200, 260), gf.Point(400,240))
  retangulo_borda.setWidth(2)
  retangulo_borda.draw(win)
  cont=0
  while cont<6:
    retanguloPreenche1=gf.Rectangle(gf.Point(201, 258), gf.Point(200+cont*40,241))
    retanguloPreenche1.setOutline('green')
    retanguloPreenche1.setFill('green')
    retanguloPreenche1.draw(win)
    sleep(0.1)
    retanguloPreenche1.undraw()
    cont+=1
    print(cont)
    sleep(0.0000000000000000000000001)

  textinho.undraw()
  retangulo_borda.undraw()
  retanguloPreenche1.undraw()

def arqFinal_candidato(result, opcoes): #Função que constrói os arquivos dos resultados. (Nesse caso, para presidente.) Usando de parametro o resultado que saiu da função de votar.
    arquivoFinal=''
    cont=0
    cont1=0
    while cont<len(opcoes):
        arquivoFinal+= opcoes[cont]+';'+str(result[cont1])+'\n' #Aqui armazena numa string o nome do candidato + ; + string do numero de votos com o indice do candidato na lista que armazena os votos.
        cont+=1
        cont1+=1

    print(arquivoFinal)
    return(arquivoFinal)



