![GitHub Logo](./static/img/dockerlogo.png)  DOCKER DEMO - Contenedor básico
--------------------------------------------------------

**IMPORTANTE**
Si se usa Windows, se requiere que los siguientes servicios estén activos y ejecutándose:
- [x] HV Host Service
- [x] Hyper-V Host Compute Service
- [x] Hyper-V Virtual Machine Management
--------------------------------------------------------


CREAR EL ENTORNO DE TRABAJO PARA DOCKER
--------------------------------------------------------

1. Crear una cuenta en https://www.docker.com/  (para este ejemplo, la cuenta es becerrajm)

2. Loguearse con la cuenta creada, e ir a https://hub.docker.com/

3. Crear un repositorio (para este ejemplo, el nombre del repositorio es docker-test)

4. Si se usa Windows, instalar Docker Desktop desde https://www.docker.com/products/docker-desktop y configurar la cuenta creada en el paso 1

--------------------------------------------------------
CREAR UNA APLICACIÓN EN EL LENGUAJE ELEGIDO
--------------------------------------------------------

5. Crear la aplicación en una carpeta


--------------------------------------------------------
CREAR LOS ARCHIVOS DE METADATOS DE DOCKER
--------------------------------------------------------

6. Crear los archivos Dockerfile y requirements.txt


--------------------------------------------------------
CONSTRUIR LA IMAGEN DE LA APLICACIÓN
--------------------------------------------------------

7. Desde la línea de comandos (recomendado PowerShell), situarse en la carpeta raiz de la aplicación

8. Construir la imagen a partir de la carpeta actual, tomando en cuenta lo definido en los archivos Dockerfile y requirements.txt
```
    docker build --tag=dockertest:0.0.1 .
```

9. Desde la línea de comandos, verificar que la imagen ha sido creada
```
    docker image ls
```


--------------------------------------------------------
EJECUTAR LA APLICACIÓN EN UN CONTENEDOR DOCKER, BASADO EN LA IMAGEN
--------------------------------------------------------

10. Desde la línea de comandos, ejecutar la imagen (es decir, instanciar el contenedor) en la PC local

```
    docker run -d -p 6000:5000 dockertest:0.0.1
```

> Verificar que el contenedor se está ejecutando: ```docker ps```
> Verificar que funciona desde el navegador de internet, en la dirección: http://localhost:6000

11. Desde la línea de comandos, detener la ejecución del contenedor
    * Determinar el ID del contenedor: ```docker image ls```
    * Detener el contenedor utilizando el ID: ```docker stop <id>```


--------------------------------------------------------
PUBLICAR LA IMAGEN EN EL REPOSITORIO DE DOCKER HUB
--------------------------------------------------------

12. Desde la línea de comandos, loguearse a Docker

```
    docker login
```

13. Desde la línea de comandos, asignar la etiqueta con la imagen que será publicada en el repositorio de Docker Hub

```
    docker tag dockertest:0.0.1 becerrajm/docker-test:0.0.1
```
El comando genérico es: 
```
    docker tag local-image:tagname reponame:tagname
```

14. Desde la línea de comandos, publicar la imagen en el repositorio de Docker Hub

```
    docker push becerrajm/docker-test:0.0.1
```

El comando genérico es: 
```
    docker push reponame:tagname
```


--------------------------------------------------------
EJECUTAR LA APLICACIÓN INVOCANDO LA IMAGEN EN EL REPOSITORIO DOCKER HUB
--------------------------------------------------------

15. Desde la línea de comandos, ejecutar la imagen desde el repositorio de Docker Hub
```
    docker run -d -p 6000:5000 becerrajm/dockertest:0.0.1
```
> Verificar que funciona desde el navegador de internet, en la dirección: http://localhost:6000

--------------------------------------------------------

> Se recomienda hacer el tutorial de la documentación oficial de Docker: https://docs.docker.com/get-started/