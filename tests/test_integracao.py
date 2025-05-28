from main.app import app
import pytest
import unittest
from unittest.mock import patch
from main.app import buscar_endereco, email_existe, criar_usuario

class TestUsuario(unittest.TestCase):
        def setUp(self):
    
                self.mock_enderecos = {
                '1234-5678': {'rua': 'Rua Teste A', 'bairro': 'Bairro Teste A', 'cidade': 'Cidade Teste A', 'estado': 'Estado Teste A'},
                '8765-4321': {'rua': 'Rua Teste B', 'bairro': 'Bairro Teste B', 'cidade': 'Cidade Teste B', 'estado': 'Estado Teste B'},
                '9999-8888': {'rua': 'Rua Teste C', 'bairro': 'Bairro Teste C', 'cidade': 'Cidade Teste C', 'estado': 'Estado Teste C'},
                '3333-2222': {}
        }
        
        @patch('main.app.buscar_endereco', return_value={'rua': 'Rua Teste A', 'bairro': 'Bairro Teste A', 'cidade': 'Cidade Teste A', 'estado': 'Estado Teste A'})
        def test_criar_usuario_sucesso(self, mock_buscar_endereco):
                mock_buscar_endereco.return_value = self.mock_enderecos['8765-4321']

                response = criar_usuario('Paes', 'paes@teste.com', 23, '8765-4321')
                self.assertEqual(response,{'rua': 'Rua Teste B', 'bairro': 'Bairro Teste B', 'cidade': 'Cidade Teste B', 'estado': 'Estado Teste B'})
        
    

     
        @patch('main.app.email_existe')
        def test_email_existe(self, mock_email_existe):
                mock_email_existe.return_value = {'erro': 'E-mail já cadastrado!'}

                response = criar_usuario('Beatriz', 'beatriz@teste.com', 23, '1234-5678')
                self.assertEqual(response, {'erro': 'E-mail já cadastrado!'})

        #Outro jeito de fazer
        # @patch('main.app.email_existe', return_value = {'erro': 'E-mail já cadastrado!'})
        # def test_email_existe(self, mock_email_existe):

        #         response = criar_usuario('Beatriz', 'beatriz@teste.com', 23, '1234-5678')
        #         self.assertEqual(response, {'erro': 'E-mail já cadastrado!'})



        @patch('main.app.criar_usuario', return_value={'erro': 'E-mail inválido!'})
        def test_email_invalido(self, mock_buscar_endereco):
                mock_buscar_endereco.return_value = self.mock_enderecos['1234-5678']
                response = criar_usuario('Beatriz', 'beatrizteste.com', 23, '1234-5678')
                self.assertEqual( response, {'erro': 'E-mail inválido!'})
        
    
        @patch('main.app.criar_usuario', return_value={'erro': 'Idade deve ser maior ou igual a 18'})
        def test_idade_menor_18(self, mock_buscar_endereco):
                mock_buscar_endereco.return_value = self.mock_enderecos['9999-8888']
                response = criar_usuario('Rafael', 'Rafael@teste.com', 12, '9999-8888')
                self.assertEqual(response, {'erro': 'Idade deve ser maior ou igual a 18'})

        @patch('main.app.buscar_endereco', return_value={'erro': 'CEP inválido!'})
        def test_cep_invalido(self, mock_buscar_endereco):
                mock_buscar_endereco.return_value = self.mock_enderecos['3333-2222']
                response = criar_usuario('Lucas', 'Lucas@teste.com', 25, '3333-2222')
                self.assertEqual(response, {'erro': 'CEP inválido!'})

   

if __name__ == '__main__':
    unittest.main()