#Definindo as funcoes

servidor ="localhost"
porta = 27017


def salvarnomongodb(documento):
    from pymongo import Connection
    conn = Connection(servidor,porta)
    db = conn.basepadrao
    db.colecao1.save(documento)
    return

def populardb():
    print "Populando..."
    salvarnomongodb({"nome":"Felipe Antunes","idade":30})
    salvarnomongodb({"nome":"Jose Antunes","idade":43})
    salvarnomongodb({"nome":"Jose da Silva","idade":23})
    salvarnomongodb({"nome":"Felipe da Silva","idade":18})
    salvarnomongodb({"nome":"Silva Antunes","idade":45})
    return

def inserir():
    print "Inserir novo documento..."
    nome = raw_input("Entre com nome:")
    idade = int(raw_input("Entre com idade:"))
    documento = {"nome":nome,"idade":idade}

    salvarnomongodb(documento)
   
    return

def procurarpornome():
    print "Busca por nome..."
    from pymongo import Connection
    conn = Connection(servidor,porta)
    
    chave = raw_input("Qual nome deseja procurar?")
    db = conn.basepadrao
    retorno = db.colecao1.find({"nome":chave})
    for item in retorno:
        print "Nome:",item["nome"]
        print "Idade:",item["idade"]
    return
                    
def transferircolecao():
    print "Tranferindo para outracolecao"
    from pymongo import Connection
    conn = Connection(servidor,porta)
    db = conn.basepadrao
    origem = db.colecao1
    destino = db.outracolecao

    for dado in origem.find():
        destino.save(dado);

    origem.remove();
    print "Transferidos! Base limpa"
    


# Inicio

print "1 - Popular Database"
print "2 - Inserir novo documento"
print "3 - Fazer busca por nome"
print "4 - Transferir colecao"


while True:
    a=raw_input("Entrar com operacao:")

    if a=="1":
        acao = populardb
    elif a=="2":     
        acao = inserir
    elif a=="3":     
        acao = procurarpornome
    elif a=="4":
        acao = transferircolecao
    else:
        print "Operacao invalida"
    #Executa acao escolhida
    acao()




    
