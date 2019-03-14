# desenvolvimento-aplicacoes-web

## Criando ambiente virtual python

- [https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)
- [http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html](http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html)

Neste projeto os seguintes comandos foram utilizados:

        $ which python3
        /usr/bin/python3
        $ virtualenv --python=`which python3` myenv
        $ pip install flask
        

Ativando o ambiente:

        $ source myenv/bin/activate
