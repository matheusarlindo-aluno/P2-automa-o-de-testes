# from flask import Flask, jsonify, request
# app = Flask(__name__)

usuarios_lista = [{'nome': 'Luiz', "email": "luiz@teste.com", "idade": "13", "cep": "8765-4321"},
        {'nome': 'Beatriz', "email": "beatriz@teste.com", "idade": "23", "cep": "1234-5678"},
        {'nome': 'João', "email": "joaoteste.com", "idade": "18", "cep": "9999-8888"} ]

def buscar_endereco(cep):
    enderecos = {
        '1234-5678': {'rua': 'Rua Teste A', 'bairro': 'Bairro Teste A', 'cidade': 'Cidade Teste A', 'estado': 'Estado Teste A'},
        '8765-4321': {'rua': 'Rua Teste B', 'bairro': 'Bairro Teste B', 'cidade': 'Cidade Teste B', 'estado': 'Estado Teste B'},
        '9999-8888': {'rua': 'Rua Teste C', 'bairro': 'Bairro Teste C', 'cidade': 'Cidade Teste C', 'estado': 'Estado Teste C'},
        '1111-2222': {'rua': 'Rua Teste D', 'bairro': 'Bairro Teste D', 'cidade': 'Cidade Teste D', 'estado': 'Estado Teste D'},
        '3333-2222': {}
    }
    return enderecos.get(cep, None)


def email_existe(email):
    for usuario in usuarios_lista:
        if usuario['email'] == email:
            return True
    return False


def criar_usuario(nome, email, idade, cep):
    if not nome or not email or not idade or not cep:
        return {'erro': 'Todos os campos são obrigatórios!'}

    if email_existe(email):
        return {'erro': 'E-mail já cadastrado!'}

    if '@' not in email:
        return {'erro': 'E-mail inválido!'}

    if int(idade) < 18:
        return {'erro': 'Idade deve ser maior ou igual a 18'}

    endereco = buscar_endereco(cep)
    if not endereco:
        return {'erro': 'CEP inválido!'}

    usuario = {
        'nome': nome,
        'email': email,
        'idade': idade,
        'cep': cep,
        'endereco': endereco
    }
    usuarios_lista.append(usuario)
    return endereco




























# @app.route('/usuarios', methods=['POST'])
# def criar_usuario():
#     dados = request.get_json()
#     nome = dados.get('nome')
#     email = dados.get('email')
#     idade = dados.get(int)
#     cep = dados.get('CEP')

#     if not nome or not email or not idade or not cep:
#         return jsonify({'erro': 'Todos os campos são obrigatórios!'})

#     usuario = {
#         'nome': nome,
#         'email': email,
#         int: idade,
#         'CEP': cep
#     }
#     usuarios_lista.append(usuario)
#     return jsonify(usuario)