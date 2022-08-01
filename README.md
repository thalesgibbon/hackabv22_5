## BomMotorista


A solução tem como objetivo criar um score de bom motorista para apoiar tomada de decisao de precos de renovacao de
seguros para cliente.

Para isso, criamos um servico que recebe a identificacao do motorista que recebera o seguro, analisa o historico de
viagens alem de diversas outras informacoes que o proprio aplicativo de corridas oferece.

Considerando que para desenvolver o modelo de ML, seria necessario as informacoes historicas de viagens, criamos um
esboco de arquitetura no qual valida a viabilidade tecnica do projeto.


## Hipoteses de features:


1. Quantidade de Corridas do motorista

2. Frequencia realizada das corridas 

3. Horário realizado das corridas

4. Regioes das corridas realizadas

5. Historico de avaliacoes

6. Quantidade de acidentes apontados no aplicativo

7. Quantidade de aplicativos utilizados

8. Satisfacao de clientes


## Jornada da solução

1. cliente entra no nosso site e faz o nosso login

2. cliente autoriza nosso site em buscar os dados sobre ele na Uber/Outros com objetivo de gerar o score bom motorista

3. nós redirecionamos o cliente para fazer login na Uber/Outros.

4. após login bem sucedido, cliente é redirecionado para nosso site com tela de sucesso

5. nos buscamos e armazenamos as informacoes dos clientes

6. geramos um score daquele cliente que sera acessado pela BV/Outros com objetivo de entregar uma taxa mais atrativa.

7. os scores dos clientes serao acessados atraves de uma API


## Integrantes

| Nome | Skill |
|---|---|
| Thales Gibbon | Eng de Dados |
| Jonatas Lima | Eng de Dados |
| Carol Pereira | Designer | 
| Eliane | Marketing |
