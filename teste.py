'''
Valores de variaveis: 
str (texto), int (inteiro), float(numeros com . ex:7.0), bool(True ou False)

#n1 = int(input('Digite um numero para somar: '))
#n2 = int(input('Digite o outro numero: '))
#r = n1 + n2 

#print('A soma entre {} e {} resulta em:{}'.format(n1,n2,r))

#Teste de variaveis: (is)
#n = input('Digita ai:') 
#n.isalnum()    (is alnum, retorna verdadeiro caso tenha texto [al], numero [num] ou ambos)
#n.isalpha()    (is alpha, retorna verdadeiro caso tenha apenas texto [apha])
#n.isnumeric()  (is numeric, retorna verdadeiro caso tenha apenas numero [numeric])
#print(n.isdigit()) (is digit, retorna verdadeiro caso tenha apenas digitos numericos)
#print(n.isdecimal())  #(is decimal, retorna verdadeiro se o texto contiver apenas caracteres decimais, 0 = True, 0.0 = False)

#v = input('Digite algo para verificarmos: ')
#print('\nO tipo primitivo do que você digitou é: {}\nOque você digitou é apenas numero? {}\nApenas texto? Se tiver espaço n vale tmb: {}\nAmbos ou algum deles? {}\nTem apenas numeros? {}\nÉ decimal? {}' .format(type(v),v.isnumeric(),v.isalpha(),v.isalnum(),v.isdigit(),v.isdecimal()))

#Operadores Matematicos:
#(Um operador, sempre precisa de um operando, e os matematicos são operadores binarios, precisam de 2 operando para funcioanar: 1+1)
#+: Adição , -: Subtração, *: Multiplicação, /: Divisão, **: Potência, //:Divisão inteiro, %: Resto da divisão

# /: Divisão: 5/2== 2.5, //:Divisão inteiro: 5/2 == 2, %: Resto da divisão: 5/2 == 1 (esse operador só mostra resultados inteiros o correto seria 0.5 mas como não é inteiro entao fica 1)
#n = 5%2
#print(n) 

#Truque matematico: Raiz quadrada: n**0.5 

#Ordem de precedência: 1º: () 2º: ** 3º: *, /, //, % 4º: +, -  (caso estejam na mesma ordem de precedência, resolve quem estiver primeiro)

#Funciona com string tbm
#print('my'*5)
#print('my'+' '+'eggs')

#n1 = int(input('Digita ai um numero caraio: '))
#n2 = int(input('Digita outro numero dnv nessa *****: '))
#s = n1+n2
#m = n1*n2
#d = n1/n2
#di = n1//n2
#p = n1**n2

#print('A Soma é {}\nMultiplicação:{}\nDivisão:{:.3f},'.format(s,m,d), end=' ')
#print('Divisão inteira: {}, Potência:{}'.format(di,p))
#end= '' serve para não quebrar a linha
#\n server para quebrar a linha
#na função print com o {} você consegue organizar oque aparecer:
#":" é o começo da definição da regra, "." significa mexer na parte decimal, "3" defini 3 casas serem vistas, "f" avisa que o numero é Float

#n = int(input('Digite um numero e eu direi seu sucessor e antecessor.\n'))
#print('O sucessor de {}, é {}, já seu antecessor seria o {}.' .format(n,n+1,n-1))

#n1 = int(input('Digite um numero e eu direi o dobro,triplo e a raiz quadrada dele.\n'))
#print('O dobro de {} é {}, o triplo:{} e sua raiz quadrada é:{}' .format(n1,n1*2,n1*3,n1**0.5))

#n1 = float(input('Direi a media do seu aluno apartir de duas notas.\nDigite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#r = n1+n2
#print('A média do aluno é:{}' .format(r/2))
#print('A média do aluno é:{}' .format((n1+n2)/2))

#n = float(input('Farei a conversão de um valor que você digitar em metros para varias medidas:\n'))
#km = n/1000
#hm = n/100
#dam = n/10
#dm = n*10
#cm = n*100
#mm = n*1000
#print('O resultado é {}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm' .format((km),(hm),(dam),int(dm),int(cm),int(mm)))


#KM(Quilômetro)| HM(Hectômetro)| DAM(DECÂMETRO) |          M(METRO)        |DM(DECÍMETRO) |CM(CENTÍMETRO) |MM(MILÍMETRO)|
#PRA CA DIVIDE POR 10 AUMENTANDO 0 A CADA MEDIDA|     <<< ESTOU AQUI >>>   |PRA CA MULTIPLICA POR 10 AUMENTANDO 0 A CADA MEDIDA
#Pra CA MULTIPLICA POR 0.1 E AUMENTA 0 DPS DO . |                          |Na lógica do código, dividir por um número menor que 1 faz o valor aumentar, então é mais segura utilizar a multiplicação "*".
#n/1000 ou n*0.001|n/100 ou n*0.01|n/10 ou n*0.1|                          |n*10          |n*100          |n*1000       |n/0.1 ou n/0.01 ou n/0.001 ~Matematicamente falando isto esta correto.

#n = int(input('Digite um numero para eu lhe mostrar sua tabuada.\n'))
#print('{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}\n' .format(n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10))

#n = float(input('Digite o valor em reais para eu converter em dolares.\n'))
#print('{} é igual a {:.2f} dolares' .format(n,n/5.014))

#n = float(input('Digite a largura e altura da sua parede em metros e eu calcularei a area e quanto de tinta você deve usar.\nDigite a largura:'))
#n2 = float(input('Digite a altura:'))
#r = n * n2

#print('Sua area é de {:.1f}m² então utilize {}L de tinta.\nCaso pegue uma lata de 18L {} ou de 3,6L {}\nSupondo ser apenas uma demão' .format(r,r/2,((r/2)+18-0.001)//18,((r/2)+3.6-0.001)//3.6))

#Formula matematica para arredondar contas de divisão para cima na programação "(A + B - 1) // B"

#n = float(input('Digite o valor do produto que recebera 5% de desconto:'))
#print('Com desconto fica: {:.2f}' .format(n-(n*5/100)))

#n == 100%   Regra de 3
#x == 5%

#print('Com desconto fica: {:.2f}' .format(n*0.95))

#n == 100%, o desconto é 5%, então o cliente vai pagar 95%.  
#n*0.95 = VALOR

#n = float(input('Digite seu salario e lhe mostrarei o novo valor com 15% de aumento.\n'))
#print('O seu novo salario é de R${:.2f}' .format(n*1.15))

#n = float(input('Digite a temperatura em ºC e lhe retornarei em ºF.\nºC:'))
#f = n*1.8+32
#print(f'A temperatura {n :.2f}ºC é {f :.2f}ºF')

#Testei o novo formato do .format()

#dist = float(input('Qual a distancia percorrida em KM do seu veiculo alugado?\n'))
#dias = int(input('Por quantos dias foi alugado o veiculo?\n'))
#pagar = dias * 60 + dist * 0.15

#print(f'Você deve pagar o valor de R${pagar}')

#import random
#num = random.randint(1,10)
#print (num)

#from math import sqrt, floor, ceil

#num = int(input('Digite um numero:'))
#raiz = sqrt(num)
#print(f'A raiz quadrada de {num} é {raiz :.2f}')
'''
'''
import math #importanto bibliotecas
n = float(input('Digite um numero real:'))
r = math.floor(n)
print (f'A parte inteira do seu numero é: {r}')'''

'''
import math
n1 = float(input('Vamos descobrir a hipotenusa, digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(n1, n2)
print(f'A hipotenusa é igual a:{h :.3f}')
#Hipotenusa == √(a² + b²) = CatOP == A, CatAD == b'''

'''
import math
anguloG = float(input('Digite o angulo, para que eu lhe mostre o Seno, Cosseno e Tangente.\n'))
anguloR = math.radians(anguloG)
seno = math.sin(anguloR)
coss = math.cos(anguloR)
tan = math.tan(anguloR)

print(f'A partir do angulo:{anguloG}º, Temos o seu Seno:{seno :.2f}, Cosseno:{coss :.2f} e Tangente:{tan :.2f}')'''

'''
import random
print('Sorteador de de aluno para apagar quadro, versão 4.0') 
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunosort = random.choice([aluno1,aluno2,aluno3,aluno4])
print(f'\nE o mais sortudo de todos é: {alunosort}')'''

'''
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

ordem = random.sample([aluno1,aluno2,aluno3,aluno4], k=4)
print(f'A ordem será:{ordem}')'''

'''
from playsound import playsound
from pathlib import Path #path é uma classe do módulo pathlib, que representa um caminho de arquivo ou diretório no sistema de arquivos. Ela fornece métodos e propriedades para manipular caminhos de forma conveniente e independente do sistema operacional.

basedoarquivo = Path(__file__).parent #__file__ retorna diretório onde o .py está e o .parent retorna o diretório pai do arquivo atual
pasta_sons = basedoarquivo / 'sons' #criamos o dicionario "sons" e atribuímos a ele o caminho completo para a pasta "sons" que está localizada no mesmo diretório do arquivo Python atual. A "/" é usada para concatenar o caminho do diretório "sons" ao caminho do arquivo atual, criando um caminho absoluto para a pasta de sons.
sons = {
    'jesus': pasta_sons / 'avemariajesus.mp3',
    'slow': pasta_sons / 'avemariaslow.mp3',
    'normal': pasta_sons / 'avemarianormal.mp3',
} #o dicionario é uma estrutura de dados que armazena pares de chave-valor, onde cada chave é única e está associada a um valor correspondente, o dicionário "sons" é usado para mapear nomes de versões de áudio (como 'jesus', 'slow' e 'normal') para os caminhos dos arquivos de áudio correspondentes.

print('====AVE MARIA DOIDO PLAYER INSANE====')
escolhadousuario = input('Escolha a versão para ser escutada: jesus, slow ou normal.\n').strip().lower() #strip() remove espaços em branco no inicio e no final da string, lower() transforma a string em minusculo
arquivosom = sons.get(escolhadousuario) #sons.get procura dentro do dicionario sons oque está na variavel escolhausuario
if arquivosom and arquivosom.exists(): #o "and" significa que ambas as condições devem ser verdadeiras e o .exists() verifica se o arquivo de áudio existe no caminho especificado, retornando True se existir e False caso contrário
    print(f'Você está ouvindo a versão braba do {arquivosom.name}') #.name retorna nome + extensão
    playsound(str(arquivosom)) #foi convertida em string usando str(), pois o playsound busca o valor da variavel em string
else:
    print('Digite apenas as opções acima, ou verifique a pasta "sons".')'''
'''
palavra = 'Sou deveras muito macho' #0 a 22, esta é a posição de cada letra
print(palavra[4:22]) #Fatiando String, o total é 22 porém para mostrar tudo tem que colocar 23, pois o ultimo valor não é contado
print(palavra[:23]) #caso n coloque nada ele considera o inicio da string
print(palavra[4:]) #mesma situação, só que ele considera o final da string
print(palavra[::2]) #o 2 é o passo, então ele vai mostrando de 2 em 2.
print("""texto muito grande mesmo ele tem varios caracteres e eu estou escrevendo para mostrar o uso de 3 aspas,
utilizando ele no começo da frase ele vai até o final
e já considera o texte inteiro mesmo eu não tendo ido até o final da frase,
então ele vai mostrar tudo que está entre as aspas triplas, e não só uma linha,
como se fosse uma string normal.""") #print( + """ + texto enome + """) ajuda com textos enormes
print(palavra.count('o')) #conta quantas vezes a letra "o" aparece na string
print(palavra.count('O'))#conta quantas vezes a letra "O" aparece na string, lembrando que o python diferencia maiusculas de minusculas
print(palavra.upper().count('O')) #transforma a string em maiuscula e consequentemente muda o resultado da contagem anterior
print(len(palavra)) #conta quantos caracteres tem na string, incluindo espaços
print(len(palavra.strip())) #strip() remove os espaços em branco no inicio e no final da string, mudando o resultado da contagem anterior
print(palavra.replace('muito', 'pouquito')) #substitui a palavra "muito" por "pouquito" na string, porém isto não altera o valor da variavel, só neste momento
palavra = palavra.replace('muito', 'mucho') #agora sim, a variavel palavra foi alterada
print(palavra.find('muito')) #procura a palavra "muito" na string, caso não encontre ele retorna -1
print(palavra.lower().find('sou')) #transforma a string em minusculo e retorna a posição da palavra "sou"
dividido = palavra.split() #divide a string em uma lista, separando as palavras pelos espaços
print(dividido)
print(dividido[0] + ' ' + dividido[-1]) #mostra a primeira, utilizamos o "+" para concatenar com um espaço " " e a e ultima palavra da lista, idependente do tamanho da lista, -1 = ultimo, -2 = penultimo, -3 = antepenultimo e assim por diante
print(dividido[1][2:]) #mostra a segunda palavra da lista, e a partir da terceira letra da segunda palavra
'''
'''
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(f'Seu nome completo tem o total de: {len(''.join(dividido))} letras') #6 + 8 + 7 = 21, total de letras, juntas pelo ''.join(dividido)
print(f'Seu primeiro nome tem o total de: {len(dividido[0])} letras')
'''
'''
#validações:
nentrada = input('Digite um valor de 0 a 9999: ').strip()
if not nentrada.isdigit(): #Verifica se o valor dentro da variavel são apenas numeros
    print('Erro! Digite apenas numeros!')
else:  nrange = int(nentrada)
if not 0 <= nrange <= 9999: #Validação para impor um range entre o 0 até 9999
    print('Erro! Digite um valor até 9999!')
else :
    nformato = nentrada.zfill(4) #.zfill preenche strings com 0 a esquerda, o numero (4) significa: menor que 4, exemplo: 10 > 0010, 12563 > 12563 (não preenche numero maior que o numero que colocamos, por isso é importante garantir o limite com a validação acima)
    uni = nformato[-1]
    dec = nformato[-2] #Aqui criamos outra variavel para receber o valor da entrada + os 0 a esquerda do zfill e tambem para separar por processo
    cen = nformato[-3]
    mil = nformato[-4]

    print(f'Unidade: {uni}')
    print(f'Dezena: {dec}')
    print(f'Centena: {cen}')
    print(f'Milhar: {mil}')
'''
'''
ent = input('Digite o nome e lhe direi se começa há Silva.\n').upper().strip()
if -1 == ent.find('SILVA'):
    print('Não tem :)')
else:
    print('Tem :)')
'''
'''
ent = input('Digite o nome da cicade e lhe direi se começa com SANTO: ').upper().strip()
if not 0 == ent.find('SANTO'):
    print('Não tem')
else:
    print('Tem')
'''
'''
ent = input('Digite uma frase:').strip().upper()
print(f'Sua frase tem {ent.count('A')} de letras "A"')
print(f'E a primeira fez que A aparece é na posição {ent.find('A')}')
print(f'Além disso a posição que aparece a ultima vez é {ent.rfind('A')}') # .rfind() faz a busca de trás para frente
'''
'''
ent = input('Digite seu nome: ').strip()
if True == ent.isdigit():
   print('Digite nome com letras!')
else:
   if -1 == ent.find(' '):
      print('Separe o seu nome por espaços.\nEx:Filipe Oliveira Balbino')
   else:
      div = ent.split()
      print(f'Seu nome é: {ent}\nO seu primeiro nome é: {div[0]}\nO ultimo nome é: {div[-1]} ')
'''
'''
nome = str(input('Qual seu nome?\n'))
if nome == 'Filipe':
    print('Esse nome é zika padrin')
else:
    print(f'Nome legal ({nome} KKKKKKK)')
print(f'Boa noite {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print (f'Sua media é {n}')
if n <= 5:
    print('Passou raspando em, estuda ai meno')
else:
    print('Amassou!')
'''
'''
import random
from time import sleep #dentro da biblioteca time tem o sleep que faz o codigo "dormir" por alguns segundos antes de continuar
print('--=--' * 12 )
print('Random Games com seu programa: Qual numero estou pensando?')
print('--=--' * 12)
n = input('Digite um numero de 0 a 5: ').strip()
if n.isdigit():
    n1 = int(n)
    if 0 <= n1 <= 5:
        n2 = random.randint(0,5)
        print('PROCESSANDO...')
        sleep(1.5) #aqui deu deixei o comando parado por 1,5 sec
        if n1 == n2:
            print(f'Caramba, você realmente acertou! Parabéns!\nPensei em {n2}')
        else:
            print(f'Errouuu KKKKK Pensei em {n2} BURRO')
    else:
        print('O numero digitado deve estar no intervalado de 0 até 5!')
else:
    print('Digite apenas numeros de 0 a 5!')
'''
'''
print('---' *8)
print('|Simulador de Radar 3.0|')
print('---' *8)
n = input('Qual a velocidade do Meliante?\n')
if n.isdigit():
    n1 = float(n)
    multa = (n1 - 80) * 7.00
    if n1 > 80:
        print(f'\033[31mParabéns! Você foi multado! no baixo valor de R${multa:.2F}\033[0m') #\033[ começa o código de cor (caractere de escape também escrito como \x1b) e 31 é o vermelho | o 0m reseta a cor "\033[0m"
else:
    print('Digite apenas numeros!')
'''
'''
from time import sleep
print('|Simulador de Par ou Impar 7.5|')
n = input('Digite o numero que será analisado: ')
print('Analisando...')
sleep(1)
if n.isdigit():
    n1 = int(n)%2
    if n1 == 0:
        print('\033[32mPar!\033[0m')
    else:
        print('\033[34mImpar\033[0m')
else:
    print('Digite apenas numeros')
'''
'''
print('|Simulador de Cobrador de viagem|')
n = input('Digite a distância da sua vigem em km:\nexemplo: 25\n')
if n.isdigit():
    passagem = int(n)
    if passagem <= 200:
        valor1 = passagem * 0.50
        print(f'Sua passagem custará R${valor1:.2F} ')
    else:
        valor1 = passagem * 0.45
        print(f'Sua passagem custará R${valor1:.2F}')
else:
    print('Por favor, digite apenas numeros')
'''
'''
from datetime import date
print('|Simulador de analisador de ano bissexto|')
ent = input('Digite o ano a ser analisado ou 0 para o ano atual:\nExemplo: 1948\n')
if ent.isdigit():
    ano = int(ent)
    if ano == 0:
        ano = date.today().year #o .today() puxa a data atual do computador que esta executando e volta o ano com .year
    if ano%100 == 0:
        if ano%400 == 0:
            print(f'O ano de {ano} é bi com certeza')
        else:
            print(f'O ano de {ano} não é bi com certeza')
    else:
        if ano%4 == 0:
            print(f'O ano de {ano} é bi')
        else:
            print(f'O ano de {ano} não é bi')
else:
    print('Digite apenas numeros correspondentes ao ano a ser analisado!')
'''
'''
print('|Simulador de Analisador de numeros, Qual será o maior?')
ent0 = input('Digite o primeiro numero a ser analisado: ')
ent1 = input('Digite o segundo: ')
ent2 = input('Digite o terceiro: ')
if ent0.isdigit() and ent1.isdigit() and ent2.isdigit():
    n0 = int(ent0)
    n1 = int(ent1)
    n2 = int(ent2)
    if n0 != n1 and n0 != n2 and n1 != n2:
        if n0 > n1 and n0 > n2 :
            print(f'Primeiro:{n0}')
            if n1 > n2 :
                print(f'Segundo:{n1}\nTerceiro:{n2}')
            else:
                print(f'Segundo:{n2}\nTerceiro:{n1}')
        else:
            if n1 > n0 and n1 > n2:
                print(f'Primeiro:{n1}')
                if n0 > n2:
                    print(f'Segundo:{n0}\nTerceiro:{n2}')
                else:
                    print(f'Segundo:{n2}\nTerceiro:{n0}')
            else:
                if n2 > n0 and n2 > n1:
                    print(f'Primeiro:{n2}')
                    if n0 > n1:
                        print(f'Segundo:{n0}\nTerceiro:{n1}')
                    else:
                        print(f'Segundo:{n1}\nTerceiro:{n0}')
    else:
        print('Não pode haver numeros iguais!')            
else:
    print('Todos devem ser numeros, digite apenas numeros!')
'''
'''
print('|Simulador de Calculador de Salarío|')
ent = input('Digite o valor do seu salario. Exemplo:3126.25\n').strip()
if not ent.isdigit():
    print('Digite apenas numeros!')
else:
    salario = float(ent)
    if salario <= 1250.00:
        print(f'Seu salario após o ajuste será R${salario*1.15}')
    else:
        print(f'Seu salario após o ajuste sera R${salario*1.10}')
'''
'''
print('|Simulador de existencia de Triângulo|')
ent0 = input('Digite o valor da primeira reta. Exemplo: 10.5\n').strip()
ent1 = input('Digite o valor da segunda:').strip()
ent2 = input('Digite o valor da terceira:').strip()
try: #Significa tente isto, o try depende de nada ter dado errado no seu bloco
    a = float(ent0)
    b = float(ent1)
    c = float(ent2)    
except ValueError: #Leitura: caso de erro, faça isso .Ele Roda se algum valor não puder ser convertido (erro), o .isdigit() só aceita numeros inteiros positivos, e nesse caso o triangulo pode ser 10.5, então desta maneira ele verifica o valor da variavel, exemplo: 10.5 está em str mas pode ser convertido para float / jota quest está em str e não pode ser convertido para float pq nem numero é
    print('Digite apenas numeros!. Além de preencher o valor de todas as 3 retas!')
else:
    if a <= 0 or b <= 0 or c <= 0: #o float aceita numeros com . e - (10,6 ele não aceita, deve ser 10.6) / então numeros negativos -10.5 ou 0 passam reto dos filtros acima, a soma dos menores devem passar o maior numero, com eles sendo 0 não há essa possibilidade.
        print('Valores menores ou igual a zero não formam um Triângulo')
    else:
        numeros = [a,b,c] #lista numeros
        maiornum = max(numeros) #o max() devolve o maior valor, existe o min() que faz contrario, devolvendo o menor valor
        numeros.remove(max(numeros)) #o remove() tira algo de dentro da lista
        if sum(numeros) <= maiornum: #sum() soma os valores de uma lista
            print('Não formam um Triângulo')
        else:
            print('Formam um Triângulo')
'''
# git remote add origin https://github.com/filipeobalbino/python_desafios_guanabara.git
# git branch -M main
# git push -u origin main