# baltarteste1

E aí Pessoal?!!

Gostaria muito ajudar um colega e preciso de vocês para essa tarefa. Caso não consigam solucionar todos os problemas, fiquem tranquilos, por isso trabalhamos em equipe. ;)

Vamos a questão...


Meu colega é um empresário Sul-Africano chamado Noel Sumk.

Sumk acabou de concluir o projeto do principal produto da sua empresa, Setla Motorcycle, a motocicleta 100% elétrica (Qualquer semelhança é mera coincidência.. =D). A ideia não seria comercializar a motocicleta e sim ter um sistema de entregas rápidas para mercadoria de pequeno porte em perímetros urbanos, usando energia limpa e sustentável. Com a engenharia do veículo resolvida, ele iniciou a etapa de integração com o usuário e seus colaboradores.

Aí onde vai entrar a nossa ajuda...

O controle dos pilotos será feito através de um token RFID (Chaveiro ou Cartão Mifare), que ao ser aproximado do leitor fornecerá um UID para o dispositivo, que fará a liberação ou não da motocicleta para o piloto.

Dividimos o problema em etapas para facilitar o entendimento e a solução:

- Leitura do cartão/chaveiro usando um dispositivo micro-controlado. Escolhemos o Arduino;
- Comunicação pela Porta Serial do Arduino com um computador. Temos o Python para tratar as informações do Arduino;
- Usando Python, fazer uma requisição para um servidor remoto onde está o banco de dados com o cadastro dos pilotos;
- Usar PHP para receber essa requisição e responder se o piloto está ou não cadastrado como piloto válido.

Vamos separar nosso projeto em pastas aqui nesse repositório, uma para cada solução, nomeadas com a linguagem de progração utilizada, nelas estão as instruções para completarmos esse desafio. Vocês podem clonar ele ou fazer o download dos arquivos, assim que concluírem respondam o e-mail que tinha o link para cá com os arquivos zipado. Nós só vamos avaliar os e-mails recebidos até **terça-feira (19/09)**.

Valeu pessoal...Boa Sorte e vamos tentar ao máximo solucionar esse problema do Noel, vai que ele fecha um contrato com a gente... =D

As pastas são:

- C_Arduino
- Python
- PHP
