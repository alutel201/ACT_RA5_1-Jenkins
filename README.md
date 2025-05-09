# ACT_RA5_1-Jenkins
ACT_RA5_1 : Jenkins

En este repositorio tengo todo lo que necesito para realizar las tareas de Jenkins

![Imagen 1](imagenes/jenkins.png)

![Imagen2](imagenes/menu.png)


TAREAS 1 Y 2

![Imagen3](imagenes/new_job.png)

En esta primera parte tenemos en la carpeta de python dos programas simples que son la calculadora y las pruebas,
en nuestra web jenkins configurando una pipeline tipo git, con la url de este repositorio hacia el jenkins file, 
definiendo el /main y haciendo que se ejecute cada minuto, la pipeline comprobara si se ha realizado algun cambio en el repositorio
debido a lo configurado en el jenkinsfile, de ser asi, ejecutara los programas dentro de la carpeta python, siendo mas especificos,
los test, si los test salen bien, es decir el porgrama va bien, saldra OK, ahora si el programa con los test se modifica y fallan, nos saldra en fallo en jenkins

![Imagen 4](imagenes/job_funcionando.png)

![Imagen 5](imagenes/success.png)

Esto es lo que saltaria si el test saliera mal.

![Imagen 6](imagenes/fallo.png)



Ejercicio 3.2

Para este ejericio he necesitado instalar docker con apt, en vez de snap ya que me daba errores, 
y asegurame que tenia instalado lo necesario para que ejecutara los comandos docker compose, y no docker-compose.

He generado un jenkinsfile.docker, que realiza todo esto:

- Ejecuta en un entorno Docker la pipeline
- Crear una imagen de docker
- Ejecuta el docker
- Ejecuta los test en el docker

Para que funione simplemente con tener instalado docker y docker compose, el resto es crear la pipeline igual que la anterior, solo que esta vez en vez de apuntar a el jenkinsfile, apunta a el jenkinsfile.docker.

Este es el log de ejecucion correcto de la pipeline.


Ejecucion final 
Lanzada por el usuario admin<br>
Obtained Jenkinsfile.docker from git https://github.com/alutel201/ACT_RA5_1-Jenkins.git<br>
[Pipeline] Start of Pipeline<br>
[Pipeline] node<br>
Running on Jenkins  in /var/lib/jenkins/workspace/docker_calculadora<br>
[Pipeline] {<br>
[Pipeline] stage<br>
[Pipeline] { (Declarative: Checkout SCM)<br>
[Pipeline] checkout<br>
Selected Git installation does not exist. Using Default<br>
The recommended git tool is: NONE<br>
No credentials specified<br>
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/docker_calculadora/.git # timeout=10<br>
Fetching changes from the remote Git repository<br>
 > git config remote.origin.url https://github.com/alutel201/ACT_RA5_1-Jenkins.git # timeout=10<br>
Fetching upstream changes from https://github.com/alutel201/ACT_RA5_1-Jenkins.git<br>
 > git --version # timeout=10<br>
 > git --version # 'git version 2.43.0'<br>
 > git fetch --tags --force --progress -- https://github.com/alutel201/ACT_RA5_1-Jenkins.git +refs/heads/*:refs/remotes/origin/* # timeout=10<br>
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10<br>
Checking out Revision 45cf0dd477bce85f6d54f055063168d34dc31e0a (refs/remotes/origin/main)<br>
 > git config core.sparsecheckout # timeout=10<br>
 > git checkout -f 45cf0dd477bce85f6d54f055063168d34dc31e0a # timeout=10<br>
Commit message: "Update Jenkinsfile.docker"<br>
 > git rev-list --no-walk 8ea8e956a3a4fa0fcab6dee11abe31785f4d2356 # timeout=10<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] withEnv<br>
[Pipeline] {<br>
[Pipeline] stage<br>
[Pipeline] { (Construir imagen Docker)<br>
[Pipeline] sh<br>
+ docker build -t calculadora-python .<br>
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.<br>
            Install the buildx component to build images with BuildKit:<br>
            https://docs.docker.com/go/buildx/<br>
Sending build context to Docker daemon  165.9kB<br>
Step 1/5 : FROM python:3.10-slim<br>
 ---> b32fa0454ca1<br>
Step 2/5 : WORKDIR /app<br>
 ---> Using cache<br>
 ---> 356ccf3bfd56<br>
Step 3/5 : COPY ./python ./python<br>
 ---> Using cache<br>
 ---> 0f389725cb40<br>
Step 4/5 : WORKDIR /app/python<br>
 ---> Using cache<br>
 ---> 800cf5961167<br>
Step 5/5 : CMD ["python3", "calculadora.py"]<br>
 ---> Using cache<br>
 ---> c280af8b4dec<br>
Successfully built c280af8b4dec<br>
Successfully tagged calculadora-python:latest<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] stage<br>
[Pipeline] { (Ejecutar contenedor)<br>
[Pipeline] sh<br>
+ docker run -d --name calculadora_test calculadora-python sleep 5<br>
ead267bd1338adf8d8842733224ef335a12414921b3de3696732092571cf8911<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] stage<br>
[Pipeline] { (Ejecutar tests dentro del contenedor)<br>
[Pipeline] sh<br>
+ docker exec calculadora_test python3 /app/python/test_calculadora.py<br>
.<br>
----------------------------------------------------------------------<br>
Ran 1 test in 0.001s<br>
<br>
OK<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] stage<br>
[Pipeline] { (Verificar docker-compose)<br>
[Pipeline] sh<br>
+ docker compose config<br>
name: docker_calculadora<br>
services:<br>
  calculadora:<br>
    build:<br>
      context: /var/lib/jenkins/workspace/docker_calculadora<br>
      dockerfile: Dockerfile<br>
    command:<br>
      - python3<br>
      - /app/python/calculadora.py<br>
    container_name: calculadora_compose<br>
    networks:<br>
      default: null<br>
networks:<br>
  default:<br>
    name: docker_calculadora_default<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] stage<br>
[Pipeline] { (Ejecutar docker-compose)<br>
[Pipeline] sh<br>
+ docker compose up -d<br>
#0 building with "default" instance using docker driver<br>
#1 [calculadora internal] load build definition from dockerfile<br>
#1 transferring dockerfile: 153B 0.0s done<br>
#1 DONE 0.1s<br>
#2 [calculadora internal] load metadata for docker.io/library/python:3.10-slim<br>
#2 DONE 0.0s<br>
#3 [calculadora internal] load .dockerignore<br>
#3 transferring context: 2B done<br>
#3 DONE 0.1s<br>
#4 [calculadora internal] load build context<br>
#4 transferring context: 1.25kB 0.0s done<br>
#4 DONE 0.2s<br>
#5 [calculadora 1/4] FROM docker.io/library/python:3.10-slim<br>
#5 DONE 0.2s<br>
#6 [calculadora 2/4] WORKDIR /app<br>
#6 DONE 1.3s<br>
#7 [calculadora 3/4] COPY ./python ./python<br>
#7 DONE 1.9s<br>
#8 [calculadora 4/4] WORKDIR /app/python<br>
#8 DONE 1.1s<br>
#9 [calculadora] exporting to image<br>
#9 exporting layers 0.1s done<br>
#9 writing image sha256:9ddf1b3e473d044608ee118f5e64a6ac63bf22ca805647f0850f6a9e821740f6 done<br>
#9 naming to docker.io/library/docker_calculadora-calculadora<br>
#9 naming to docker.io/library/docker_calculadora-calculadora done<br>
#9 DONE 0.1s<br>
 Network docker_calculadora_default  Creating<br>
 Network docker_calculadora_default  Created<br>
 Container calculadora_compose  Creating<br>
 Container calculadora_compose  Created<br>
 Container calculadora_compose  Starting<br>
 Container calculadora_compose  Started<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] stage<br>
[Pipeline] { (Declarative: Post Actions)<br>
[Pipeline] sh<br>
+ docker rm -f calculadora_test<br>
calculadora_test<br>
[Pipeline] sh<br>
+ docker compose down<br>
 Container calculadora_compose  Stopping<br>
 Container calculadora_compose  Stopped<br>
 Container calculadora_compose  Removing<br>
 Container calculadora_compose  Removed<br>
 Network docker_calculadora_default  Removing<br>
 Network docker_calculadora_default  Removed<br>
[Pipeline] }<br>
[Pipeline] // stage<br>
[Pipeline] }<br>
[Pipeline] // node<br>
[Pipeline] End of Pipeline<br>
Finished: SUCCESS
