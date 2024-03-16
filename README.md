Ei, tudo bem?

Eu desenvolvi esta API para explicar sobre a vulnerabilidade BOLA, que ocorre em APIs. Também fiz uma prova de conceito (PoC) demonstrando como explorar essa vulnerabilidade no meu LinkedIn (confira o link abaixo).

Para executar esta aplicação, siga estes passos simples:

Primeiro, baixe o repositório:

git clone https://github.com/turnerlk/B-O-L-A.git

Em seguida, atualize o gerenciador de pacotes:

sudo apt update

Depois, instale o Docker:

sudo apt install docker-ce docker-ce-cli containerd.io

Agora, execute o comando abaixo para iniciar a aplicação:

sudo docker run -p 8081:8080 api-bola

Isso é tudo! A aplicação estará rodando e você pode explorar a vulnerabilidade BOLA.

