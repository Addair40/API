# API

##  CREAR LA IMAGEN DE DOCKER

```bash
docker build -t API:10.06.22
```

##  CREAR LA IMAGEN DE DOCKER

```bash
docker run -it -v "$PWD"/code:/home/code --net host --nmae API
-h API API:10.06.22
```
