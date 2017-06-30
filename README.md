# Switch Cipher
Switch Cipher é uma cifra criptográfica que troca a ordem das letras de acordo com a key.

## Funcionamento

O Switch Cipher trabalha com a chave da seguinte maneira: Tendo um alfabeto, a primeira letra da chave é posta no início e a posição original dessa letra é retirada, a segundo letra é posta no fim, e novamente a posição original dessa letra é retirada, fazendo assim até o final da chave. Quando terminar temos um novo alfabeto composto de letras desordenadas. Após isso, é feita a reconstrução da palavra usando o "novo alfabeto".

## Como usar

Para usar, há dois argumentos obrigatórios e dois que são os que definem se é para encriptar os decriptar. Onde eu tenho os seguintes parâmetros:

**-e** ou **--encrypt**: Define o programa para encriptar uma palavra.

**-d** ou **--decrypt**: Define o programa para decriptar uma palavra.

**-w** ou **--word**: Define a palavra ou frase para ser encriptada ou decriptada.

**-k** ou **--key**: Define a chave que será usada.

### Exemplos

```
Switch-Cipher.py -e -w Criptografia -k mykey
```

Irá retornar: *Mrgptodrycgy*

Para decriptar, então, usamos:

```
Switch-Cipher.py -d -w Mrgptodrycgy -k mykey
```

Irá retornar: *Criptografia*

## Limitações

* Tudo que não seja letra não é criptografado, ou seja, seu estado é preservado.
* Não suporta chaves que contenham caracteres que não sejam letras.
* Números não são criptografados.

## Direitos de Uso

Esse software é disponibilizado "do jeito que é", sem nenhuma garantia. Você poderá utilizar da maneira que bem entender, modificando, adicionando módulos, usando em outro programa, desde que ponha os devidos créditos
