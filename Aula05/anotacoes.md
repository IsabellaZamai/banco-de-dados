# Aula 05 - Comandos SQL Analize de Dados
### 25/08/2026

### Parte 1
Criação e inserção de Dados, realizando algumas consultas avançadas.


Utilizei esse comando para entrar no postgres
![alt text](image.png)

![alt text](image-1.png)



Criamos aqui
![alt text](image-2.png)

Em uma base de Dados muito grande é interessante filtrar os 5 primeiros, usando o LIMIT para limitar a quantidade.

![alt text](image-3.png)

para filtrar colunas:
````sql
SELECT nome,valor,categoria FROM produtos;

````

Para escolher apenas uma categoria é assim:

![alt text](image-4.png)

### Parte-2
Filtro de Dados.


Oque é um vetor?
na matematica é um segmento de reta que possuie modulo direção e sentido.
no banco de dados, cada Dados é um vetor, que possuie modo direção e sentido.




![alt text](image-5.png)


````sql
SELECT nome,estoque
FROM produtos
WHERE categoria = 'Redes';
````
Filtros de Valores mais caros:

````sql
SELECT nome,estoque, valor
FROM produtos
WHERE valor > 1000;
````

![alt text](image-7.png)


< > = aritimeticos
and = logicos
if,else = condicionais

Filtro entre faixas de valores:
````sql
SELECT nome,estoque,valor
FROM produtos
WHERE valor BETWEEN 100 AND 500;
````

![alt text](image-8.png)

Busca por trecho de texto,

````sql
SELECT nome,estoque 
FROM produtos
WHERE nome LIKE 'Mouse%'
````
![alt text](image-9.png)

>o porcentagem e o operador coringa:

O ILIKE
Desconsidera letras maiusculas:
````sql
SELECT nome,estoque 
FROM produtos
WHERE nome ILIKE 'Mouse%'
````



SELECT * FORM LIVROS LIMIT 10;