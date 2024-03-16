# Broken Object Level Authorization

Criei esta API para abordar a vulnerabilidade conhecida como BOLA, que afeta APIs. Além disso, elaborei uma prova de conceito (PoC) para ilustrar como essa vulnerabilidade pode ser explorada. Você pode conferir o link para o meu LinkedIn abaixo.
https://www.linkedin.com/feed/update/urn:li:activity:7174808124057391104/

### 📋 Pré-requisitos
```
Docker
```
### 🔧 Instalação:
Primeiro, baixe o repositório:
```
git clone https://github.com/turnerlk/B-O-L-A.git
```
Em seguida, atualize o gerenciador de pacotes:

```
sudo apt update
```

Posteriormente, proceda com a instalação do Docker caso ainda não o tenha instalado:

```
sudo apt install docker-ce docker-ce-cli containerd.io
```

A seguir, utilize os comandos abaixo para construir e iniciar a aplicação:

```
sudo docker build -t api-bola .
sudo docker run -p 8081:8080 api-bola
```
Essas são todas as etapas necessárias! A aplicação estará em execução e você poderá explorar a vulnerabilidade BOLA ao acessar:

```
http://127.0.0.1:8081
```

