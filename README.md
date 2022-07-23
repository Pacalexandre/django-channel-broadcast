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
- arquivo html usando bootstrap 5 'http://https://getbootstrap.com/'
- configurando acesso a API jokes 'http://api.icndb.com/jokes/ramdom'
- instalando e configurando redis
    - dependencias do celery com redis ``` pip install 'celery[redis]' ```
- instalando e configurando celery 
    - broker
    - task
    - start processo beats with: ```bash celery -A app beats -l INFO```
    - start processo worker with: ```bash celery -A app worker -l INFO```

![](app/static/beat.png) ![](app/static/worker.PNG)

- agora criar o websocket install channels
- configurando websocket da aplicacao


### Celery help

```bash
Usage: celery [OPTIONS] COMMAND [ARGS]...

  Celery command entrypoint.

Options:
  -A, --app APPLICATION
  -b, --broker TEXT
  --result-backend TEXT
  --loader TEXT
  --config TEXT
  --workdir PATH
  -C, --no-color
  -q, --quiet
  --version
  --help                 Show this message and exit.

Commands:
  amqp     AMQP Administration Shell.
  beat     Start the beat periodic task scheduler.
  call     Call a task by name.
  control  Workers remote control.
  events   Event-stream utilities.
  graph    The ``celery graph`` command.
  inspect  Inspect the worker at runtime.
  list     Get info from broker.
  logtool  The ``celery logtool`` command.
  migrate  Migrate tasks from one broker to another.
  multi    Start multiple worker instances.
  purge    Erase all messages from all known task queues.
  report   Shows information useful to include in bug-reports.
  result   Print the return value for a given task id.
  shell    Start shell session with convenient access to celery symbols.
  status   Show list of workers that are online.
  upgrade  Perform upgrade between versions.
  worker   Start worker instance.
```

## Fonts na internet 
 
 - https://www.youtube.com/watch?v=AZNp1CfOjtE