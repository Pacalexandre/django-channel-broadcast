# django-channel-broadcast

Vamos implementar um broadcast de Piadas do Chuck Norris com .devcontainer e filas no celery
vamos utilizar uma API publica para buscar as mensagens e vamos utilizar celery mas o channel para 
mandar as mensagens para todos os breowsers conectados, Essa implementação vai utilizar devcontainer
com toda a integração necessária para rodar em uma maquina com docker instalado Windows, Linux ou Mac.

- pré requisitos
    - docker - Docker version 20.10.8, build 3967b7d
    - docker-compose - Docker Compose version v2.2.2
    - visual studio
    - extensions: Remote - Containers
    - [documentação](https://code.visualstudio.com/docs/remote/containers)

## Configurando a aplicação todos os passos já realizados

- instalando django 
- configurando dev container para instalação de dependencias e migrate  
- configurando dependencias do projeto settings / templates
- definindo no va chave de segurança settings
- crianto pastas e arquivos de templates
- rota padrao para acesso na url base
- configurando acesso a API jokes 'http://api.icndb.com/jokes/ramdom'

