	# baltarteste1

	E aí Pessoal?!!

	Gostaria muito ajudar um colega e preciso de vocês para essa tarefa. Caso não consigam solucionar todos os problemas não tem problema, por isso trabalhamos em equipe. ;)

	Vamos a questão...


	Meu colega é um empresário Sul-Africano chamado Noel Sumk.

	Sumk acabou de concluir o projeto do principal produto da sua empresa, Setla Motorcycle, a motocicleta 100% elétrica (Qualquer semelhança é mera coincidência.. =D). A ideia não seria comercializar a motocicleta e sim ter um sistema de entregas rápidas para mercadoria de pequeno porte em perímetros urbanos, usando energia limpa e sustentável.
	Com a engenharia do veículo resolvida, ele iniciou a etapa de integração com o usuário e seus colaboradores. Aí onde vai entrar a nossa ajuda...
	O controle dos pilotos será feito através de um token RFID (Chaveiro ou Cartão Mifare), que ao ser aproximado do leitor fornecerá um UID para o dispositivo, que fará a liberação ou não da motocicleta para o piloto.

	Dividimos o problema em etapas para facilitar o entendimento e a solução:

	- Leitura do cartão/chaveiro usando um dispositivo micro-controlado. Escolhemos o Arduino;
	- Comunicação pela Porta Serial do Arduino com um computador. Escolhemos Python para tratar as informações vindas do Arduino;
	- Usando Python, fazer uma requisição web para um servidor remoto onde está o banco de dados com o cadastro dos pilotos;
	- Usar PHP para receber essa requisição e responder se o piloto está ou não cadastrado como piloto válido.