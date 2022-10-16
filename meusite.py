from crypt import methods
from flask import Flask, render_template, request
import sqlite3
from random import randint
import math, datetime, time

app = Flask(__name__)

#conecte banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    variavel = "Você esta progranmando em Python - FLASK"
    return render_template("index.html", variavel_base = variavel)


@app.route('/game', methods=["GET", "POST"])
def game():
    variavel = "Game: Adivinhe o número correto"
    if request.method == "GET":
        return render_template("game.html", variavel_base = variavel)
    else:
        numero = randint(1,20)
        palpite = int(request.form.get("name"))
        
        if numero == palpite:
            mostraResultado = "Você Ganhou"
            return render_template("base.html", variavel_base = mostraResultado)
            #return '<h2> Resultado: Você ganhou</h2>'
        else: 
            mostraResultado = "Você Perdeu"
            return render_template("base.html", variavel_base = mostraResultado)
            #return '<h2> Resultado: Você perdeu</h2>'

# criando uma página
@app.route('/sobre')
def sobre():
    return 'meu nome é Douglas, sou programador Python'

# criando página não encontrada
@app.route('/<string:nome>')
def error(nome):
    variavel = f'Página ({nome}) não existe'
    return render_template("base.html", variavel_base = variavel)

# Página ano Bissexto
@app.route('/bissexto', methods=["GET", "POST"])
def bissexto():
    valor = "Python"

    if request.method == "GET":
        return render_template("bissexto.html", variavel_base = valor)
    else:
        mostraValor1 = "O ano digitado é BISSEXTO"
        mostraValor2 = "O ano digitado Não é BISSEXTO"
        ano = int(request.form.get("name"))

        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            return render_template("base.html", variavel_base = mostraValor1)
        else:
            return render_template("base.html", variavel_base = mostraValor2)


@app.route('/hypot', methods=["GET", "POST"])
def hypot():
    valor = "inválido methodo GET"

    if request.method == "GET":
        return render_template("hypot.html", variavel_base = valor)
    else:
        oposto = float(request.form.get("oposto"))
        adjacente = float(request.form.get("adjacente"))
        hi = math.hypot(oposto, adjacente)
        descri = "o valor da hipotenusa é {:.2f}".format(hi)

        return render_template("base.html", variavel_base = descri)

@app.route('/udcm', methods=["GET", "POST"])
def udcm():
    valor = ""

    if request.method == "GET":
        return render_template("udcm.html", variavel_base = valor)
    else:
        num = int(request.form.get("qual"))

        uni = num // 1 % 10
        dez = num // 10 % 10
        cen = num // 100 % 10
        mil = num // 1000 % 10

        descri = "unidade é {}\n dezena é {}\n centena é {}\n milhar é {}\n".format(uni, dez, cen, mil)
        
        return render_template("base.html", variavel_base = descri)

@app.route('/datahora')
def datahora():
    now = datetime.datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "base.html",
        title = now,
        message = "Primo Programador",
        content = " on " + formatted_now)