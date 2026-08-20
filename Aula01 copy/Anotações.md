## Configuração do Servidor Educacional

o objetivo e simular um ambiente real de produção

````mermaid
graph LR
A[Cliente]<--<b>Dados-->B[Servidor]
````
### Treino

>Olha uma caixinha
---

**Objetivo**: 

-Experiência Real de Mercado,

-Administração de recursos,

-Experiência em Servidores Linux.

---

### Servidor de Arquivos
-Servidor Educacional para arquivos, assim não depedendo da rede externa.

````mermaid
graph TD
A[Servidor Senai 
\\10.87.36.10]--Arquivos-->B[Computador]-->R1[mouse]
````
### Servidor de Deselvolvimento
Cada Aluno recebe o seu proprio acesso. Cada maquina recebe um endereço de IP diferente.


**Meu IP do meu Servidor**:

>192.168.10.29

*passWord*:

>Wolfgang

|Recurso|Configuração|
|-------|------------|
|CPU|2 cores|
|RAM|512 mb|
|Disco| 6 GB|
|Sistema operacional| Ubunto 26.04 LTS|
|Acessos | SSH(Secure Shell)
-----

### Comandos
comando para visualizar os recuros
````
htop
````
comando alteração de senha
````
passwd
````

Dados de acesso:
|campo|valor|
|-----|-----|
|Ip do container|192.168.10.29|
|Usuario|root|
|Senha inicial|aluno01|
---------------------

## Banco De Dados
Dados: informaçoes isoladas, não dizem muita coisa. Ex: Platini, caneta, R$ 10, 31/08

Informação:Dados estruturados. Ex: No dia 31/08, platini comprou uma ceneta por R$ 10.

Conhecimento: Oque podemos extrair destes dados. Ex: O platini usa canetar, a loja estava aberta do dia 31/08, o platini tinha R$ 10.

````mermaid
graph LR
A[Dados:Caneta]-->B[Processamento]-->C[Informação: precisa de canetas]
````
---
O fluxo normal normal de um banco de Dados esta representado Abaixo:
````mermaid
graph LR
A[Usuário] --> B[Aplicação] --> C[(Banco de Dados)]

````

>Por qual razão, as empresas não salvam os dados em arquivo comuns?
````mermaid
graph TD
A[guardar dados]-->B[Banco de dados]
A[guardar dados] --> C[Arquivo/Planilhas]
B-->B1[Vários usuários ao mesmo tempo]
B-->B2[Backup e sincronização]
B-->B3[Consultas otimizadas
e rapidas]
C-->C1[Um arquivo por vez]
C-->C2[Não tem backup]
````


SGBD - Sistema Gerenciador de Banco de Dados

>POSTGRESQL: SGBD OpenSource e muito completo.

Primeiro, começamos atualizando os pacotes:
````bash
sudo apt update && upgrade
````
 Diagramas
 postgress


 06/08/2026
 para a instalação do Postgresql:
 ````bash
 sudo apt install -y postgresql
 ````
