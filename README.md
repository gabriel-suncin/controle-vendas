# Controle de Vendas
Plataforma de controle de vendas
Desenvolvido em Python + Django, foi utilizado tanto o framework Django RestFramework quanto o python puro para 
serializar e devolver JsonResponses
Versão do Python -> 3.8
Desenvolvido para o teste técnico para a vaga de Back-end - PL 


# Instruções:
- <strong>Crie um ambiente virtual com Python-3.8 e instale todos os requirements do Projeto "requirements.txt"</strong> 

- <strong>Importe o Banco de Dados do Projeto:</strong>
      Fiz o upload neste projeto também do banco que utilizei com algumas tabelas populadas com Produtos, Pedidos, 
      Lotes e Clientes, aconselho que utilize o mesmo banco para facilitar a validação dos testes;

- <strong>Importe todas as coleções do Postman:</strong>
        Durante o desenvolvimento do projeto utilizei o Postman para os requests, criei uma Collection com 
        todos os testes desenvolvidos e deixei uma cópia desta Collection neste git com o nome de:
            => "controle-vendas.postman_collection.json"

- <strong>Realize o login no Postman:</strong>
        Para utilizar o Postman deve primeiro realizar o login no sistema, utilizei o decorator de login_required
        para todas as requisições, restringindo o programa para apenas usuarios logados, caso utilize o banco que 
        anexei no git, os dados de login são: 
              usuário: "dev",
              senha: "P1!2DyceH#oS"
        Obs. Requisição de Login  pronta na Collection do Postman em "login" na aba Body no Form-data.
  
- <strong>Utilize as requisições do Postman:</strong>
        Utilize todos os testes da Collection através dos endpoints criados
  
Obs. Todos os exemplos de requisições estão salvas na cópia 'exportada' do Postman na raíz do projeto
  
# EndPoints


- Produtos

Listar produtos -> http://127.0.0.1:8000/list-produtos/ método GET para listar todos os produtos, deve 
realizar um GET pelo Postman na url do endpoint (127.0.0.1:8000/) + list-produtos/
http://127.0.0.1:8000/list-produtos/
--- Retorna um Json com todos os Produtos


Listar produtos + filtro -> http://127.0.0.1:8000/list-produtos/?nome=xxxx&valor=yyyy Método get para listar todos os produtos com filtro,
substituir os valores "xxxx" e "yyyy" pelos valores desejados para realizar a busca
--- Retorna um Json com todos os Produtos


Detalhar produto -> http://127.0.0.1:8000/detail-produtos/1 Método GET para visualizar detalhes do produto,
é necessário inserir na url do endpoint (127.0.0.1:8000/) + detail-produtos/ + o id do produto 
--- Retorna um Json com todos os dados do Produto buscado


Adicionar Produto -> http://127.0.0.1:8000/add-produtos/ Método POST para adicionar produtos, durante os testes utilizei
o Postman para adicionar via Body>form-data, é necessário informar os parâmetros de acordo com o seguinte:

        {'identificador': Numero do identificador do Produto, 
        'nome': Nome do Produto, 
        'numero_lote': numero Identificador do Lote do Produto,
        'valor': caso precise de um numero com casas decimais, utilizar o ponto para separá-las, 
        'cor': nome da cor, 
        'descricao':Descrição do produto}

- Pedidos

Listar pedidos -> http://127.0.0.1:8000/list-pedidos/ método GET para visualizar todos os pedidos, deve 
realizar um GET pelo Postman na url do endpoint (127.0.0.1:8000/) + list-pedidos/
--- Retorna um Json com todos os Pedidos

Listar produtos + filtro -> http://127.0.0.1:8000/list-pedidos/?valor_total=xxxx&data_compra=yyyy
Método get para listar todos os pedidos com filtro, substituir os valores "xxxx" e "yyyy" pelos valores 
desejados para realizar a busca
--- Retorna um Json com todos os Pedidos

Detalhar Pedido -> http://127.0.0.1:8000/detail-pedidos/1 Método GET para visualizar detalhes do pedido,
é necessário inserir na url do endpoint (127.0.0.1:8000/) + detail-pedidos/ + o id do pedido
--- Retorna um Json com todos os dados do Pedido buscado

Adicionar Pedido -> http://127.0.0.1:8000/add-pedidos/ Método POST para adicionar pedidos, durante os testes utilizei
o Postman para adicionar via Body>form-data, é necessário informar os parâmetros de acordo com o seguinte:

        {'identificador': Numero do identificador do Pedido, 
        'produtos': Numero de Identificação dos Produtos (separar por espaços em branco, ex: '12 1952'), 
        'status': numero do status, Ativo = 1; Pendente = 2; Concluido = 3; Cancelado = 4,
        'cliente': Nome completo do Cliente cadastrado no sistema, 
        'cor': nome da cor, 
        'vendedor': Utilizar o username do vendedor cadastrado,
        'valor_total': caso precise de um numero com casas decimais, utilizar o ponto para separá-las}

- Lotes

Listar lotes -> http://127.0.0.1:8000/list-lotes/ método GET para visualizar todos os lotes, necessário 
realizar um GET na url do endpoint (127.0.0.1:8000/) + list-lotes/
--- Retorna um Json com todos os Lotes

Detalhar Lote -> http://127.0.0.1:8000/detail-lotes/1 Método GET para visualizar detalhes do lote,
é necessário inserir na url do endpoint (127.0.0.1:8000/) + detail-lotes/ + o id do lote
--- Retorna um Json com todos os dados do Lote buscado


- Clientes

Listar clientes -> http://127.0.0.1:8000/list-clientes/ método GET para visualizar todos os lotes, necessário 
realizar um GET na url do endpoint (127.0.0.1:8000/) + list-lotes/
--- Retorna um Json com todos os Clientes

Detalhar cliente -> http://127.0.0.1:8000/detail-clientes/1 Método GET para visualizar detalhes do lote,
é necessário inserir na url do endpoint (127.0.0.1:8000/) + detail-lotes/ + o id do lote
--- Retorna um Json com todos os dados do Cliente buscado

- Auth

path('login/', api_login, name='login'),

path('logout/', auth_views.logout_then_login, name='logout'),



Desenvolvido por: Gabriel Suncin - 12/2020