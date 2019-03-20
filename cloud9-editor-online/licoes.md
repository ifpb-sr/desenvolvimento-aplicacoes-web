# Primeira utilização

Este documento descreve passos para utilização de ambiente virtual de desenvolvimento cloud9 (IDE online).

**NOTE**: Cuidado para não ficar muito tempo inativo senão a sessão é encerrada e precisará fazer login novamente.

# 0 Aceitando convite e criando senha

[Acesse esta planilha](https://docs.google.com/spreadsheets/d/1vMEN4TDSmUPKY7SMlYHfnbOjTlYStS8l8Ws64xhIUxo/edit#gid=0) e veja qual e-mail seu foi cadastrado.

Localize o e-mail com o título "Your AWS Educate Application" e abra-o. Depois clique em "Click here" para finalizar o cadastro.

Altere o idioma em *Prefere language* para portuguese. Preencham os dados do formulário.

O primeiro ano é quando vocês irão concluir o segundo a data de nascimento.

Clique numa "Clique aqui para seleciona uma conta aws educatate starter"

Abra o e-mail e clique no link na nova mensagem.

Leiam o termo e condições e aceitem ou não. Brincaderinha, clique em Eu aceito. (Requer descer a tela inteira). Depois clica em **Enviar**.

Depois um novo e-mail com aprovação será recebido. Nele haverá um vídeo explicando a AWS Education e um link para criar um login e password. Clique para criar o login e password. `Click here to set you password and login`. 

Antes de criar a senha, leia as instruções abaixo sobre como a senha deve ser.

Agora, ANOTE no celular a senha que irão colocar, depois tatuem ela. Ou apenas não esqueçam.

Clique em *Classroms* depois em no botão **Go to classroom** e **Continue**. 

Leiam os termos de condições novamente e aceitem. 

Agora cliquem em **AWS Console**. Quando não aparecer nada é pq o navegador está bloqueando popups. Permite a abertura da popups no navegador. Isso é feito no ícone ao lado do de traduzir a página. Clique nele e marque sempre permitir abrir pop-ups nesse site. em seguida, clique em **AWS Console** novamente.

# 1. Acessando awseducate

- Acessem a [awseducate](https://www.awseducate.com/educator/s/awssite). (Abram numa nova aba)
- Cliquem em **Go to your AWS Educate Starter Account** (pode está em **My Classes**).

Para acessar o console clique em "Console AWS":

![aws-console](https://user-images.githubusercontent.com/3603111/54686894-128c2f80-4af9-11e9-8e93-4f44d1e4d936.png)

No **Console de gerenciamento da AWS** localize o serviço `cloud9`.

Vamos realizar uma **Configuração expressa para o AWS Cloud9**.

# 2 Solicitar criação do ambiente

- Clicar em create enviroment:

![create-enviroment](https://user-images.githubusercontent.com/3603111/54687384-356b1380-4afa-11e9-8644-1ef6952dbd6f.png)

# 3 Preencendo dados

- Preencha o **Name** do ambiente com `Python-para-Web`. E na descrição coloque: `Primeiro ambiente`.


![python-para-web](https://user-images.githubusercontent.com/3603111/54687531-9561ba00-4afa-11e9-9222-d5cfb111cc00.png)


# 4 Entendendo as configurações

![configuracoes](https://user-images.githubusercontent.com/3603111/54687847-5718ca80-4afb-11e9-82db-e488b1eaa076.png)

**NOTE**: Nós temos $ 100,00 dólares de créditos para executar as aplicações na núvem.

## Configuração pardão

Nós vamos iniciar uma IDE num computador remoto **micro**, com configuração de 1 GB de RAM e *single core*. A cada minuto de uso os nossos créditos serão debitados. A cada 30min de inatividade o servidor é hibernado para não gastar nossos créditos indefinidamente.

Clique em **Next step**.

# 5 Leias configurações do ambiente solicitado

Leia as recomendações:

- Use source control and backup your environment frequently. AWS Cloud9 does not perform automatic backups.
- Perform regular updates of software on your environment. AWS Cloud9 does not perform automatic updates on your behalf.
- Turn on AWS CloudTrail in your AWS account to track activity in your environment. Learn more
- Only share your environment with trusted users. Sharing your environment may put your AWS access credentials at risk. Learn more

Clique em **Create environment**.

# 6 Aguarde a criação

![criando](https://user-images.githubusercontent.com/3603111/54688449-5f253a00-4afc-11e9-99d5-305aac259c7e.png)


# 7 Entre em tela cheia

Entre no modo Tele cheia.

**OBS**: Eu precirei ir para outra aba, pressionar F11 e depois voltei para a aba anterior. Use `CTRL+Page Up` para trocar de abas.

# 8 Aprendendo a acessar a documentação

- Clique em `Support` e depois em `Read documentation`.
- Baixe a documentação em português em PDF:

![baixe-pdf](https://user-images.githubusercontent.com/3603111/54689086-9cd69280-4afd-11e9-9f25-1d65270a435f.png)

# 9 Vamos realizar as três operações de Get stated

![get-stated](https://user-images.githubusercontent.com/3603111/54689617-ac0a1000-4afe-11e9-9677-282b3c30d05e.png)

- Criar arquivo
- Enviar arquivo
- Clonar repositório

## Crie um arquivo diario.md

Crie e salve um arquivo diario.md com o seguinte conteúdo:

```markdown
# Diário

Contém minhas anotações sobre as atividades de desenvolvimento.

## 21/03/2019

Como eu me senti ao *criar um arquivo*: 

Como eu me senti ao *enviar um arquivo*: 

Como eu me senti ao *clonar repositório*: 

```

Salve o arquivo!

![meu-diario](https://user-images.githubusercontent.com/3603111/54691401-f3de6680-4b01-11e9-8b55-efe3520d45df.png)


## Enviando um arquivo

Tire um printscreen e envie o arquivo para lá.


![arquivo-enviado](https://user-images.githubusercontent.com/3603111/54691435-fe98fb80-4b01-11e9-9db9-1feb71f0415d.png)

NOTE: Perceba que a imagem foi enviada.

## Clonando repositório

Tente clonar o repositório e verifique que deu erro:

![clone-erro](https://user-images.githubusercontent.com/3603111/54691487-16707f80-4b02-11e9-956f-9a189ef28181.png)

### Configurando chaves de criptografia SSH

Precisamos configurar [as chaves de acesso SSH antes](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). Faça isso agora.

Estou fazendo para o meu e-mail (eduardo.ufpb@gmail.com), faça para o seu. Deixe a passphrase vazia, basta dar ENTER.

```
vocstartsoft:~/environment $ ssh-keygen -t rsa -b 4096 -C eduardo.ufpb@gmail.com
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ec2-user/.ssh/id_rsa): yes
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in yes.
Your public key has been saved in yes.pub.
The key fingerprint is:
SHA256:I+UjUjyP51G1hoDuZ4ZRuYBuOPwQRhS/foRA2d3+d4g eduardo.ufpb@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
| o=+ o o..  .    |
| .+.o.+ +. o .   |
| o.+..++..o o    |
|  =.o+o*o. .     |
|   =+.=oS. . .   |
|   ..oo=++E o .  |
|    . .+.  . .   |
|     .           |
|                 |
+----[SHA256]-----+

vocstartsoft:~/environment $ eval "$(ssh-agent -s)"
Agent pid 6597

vocstartsoft:~/environment $ ssh-add yes
Identity added: yes (yes)
```

Depois ir em [Add the SSH key to your GitHub account](https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account).


![cat yes pub](https://user-images.githubusercontent.com/3603111/54692449-d1e5e380-4b03-11e9-991c-e279ae4e7a59.png)

![add-key-github](https://user-images.githubusercontent.com/3603111/54692470-d90cf180-4b03-11e9-81ab-0698a856277e.png)

## Clonando novamente

Depois que as chaves foram configuradas, podemos clonar com sucesso:

NOTE: Você deve clonar um repostório *forkado*.

```
vocstartsoft:~/environment $ git clone git@github.com:ifpb-sr/desenvolvimento-aplicacoes-web.git
Cloning into 'desenvolvimento-aplicacoes-web'...
remote: Enumerating objects: 71, done.
remote: Counting objects: 100% (71/71), done.
remote: Compressing objects: 100% (51/51), done.
remote: Total 71 (delta 27), reused 19 (delta 5), pack-reused 0
Receiving objects: 100% (71/71), 13.58 KiB | 463.00 KiB/s, done.
Resolving deltas: 100% (27/27), done.
vocstartsoft:~/environment $ 
```

# 10 Executando a aplicação em Vamos executar 

Vamos entrar em `environment/desenvolvimento-aplicacoes-web/verbos-http` e executar a aplicação `aprendendo_metodos.py`. Leia os READMEs para lembrar como instalar as dependencias e executar a aplicação.

Boa sorte!

![](http://img.glimboo.com/recado/boa_sorte/boa_sorte_406865.png)
