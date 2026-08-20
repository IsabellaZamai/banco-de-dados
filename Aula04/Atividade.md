## Banco de Dados-Streaming
### atividade- 20/08/2026


O primeiro passo foi criar o Banco de Dados,
Utilizei o comando:


````sql
sudo psql -h 127.0.0.1 -U postgres
````
e o 
````sql
CREATE DATABASE Streaming;
````
E com o \l vemos que criou

![alt text](image-1.png)

Apos isso no VSCOde Adicionei um Banco de Dados:


![alt text](image-10.png)


E criei um TABLE de nome FilmesESeries com as tabelas:

```sql
INSERT INTO filmeseseries(Nome,duracao,nota)
 VALUES('Orgulho e Preconceito',119,4);
```

![alt text](image-3.png)

Adicionei os dados, entre eles Filmes e Series,

![alt text](image-4.png)

Atualizei a tabela com o Comando, mudando a nota de 5 filmes:
````sql
UPDATE filmeseseries
SET nota = 2
WHERE id = 3;
````

![alt text](image-5.png)

Aqui ja eu atualizei os 5 filmes que podem ser vistos em baixo de todos os outros.
![alt text](image-6.png)

E para finalizar  Deletei 5 filmes com o comando:

````sql
DELETE FROM filmeseseries WHERE id=10;
````
![alt text](image-7.png)


![alt text](image-8.png)

E no fim a tabela ficou com esta aparência:

![alt text](image-9.png)


No fim, por motivos esteticos Eu usei o comando:
````sql
SELECT * FROM filmeseseries
ORDER BY nota DESC;
````