# buscador-videos
## Despliegue
### Local
#### Backend

##### Clonando el repositorio
El repositorio se clona con:

```bash
git clone https://github.com/cier-centro/buscador-videos.git
```
##### Poblando la base de datos con los valores por defecto

Se crea un entorno virtual y se ejecutan los comandos:

```bash
virtualenv env #así se crea el entorno virtual
source env/bin/activate # Así se activa en linux, más info en https://virtualenv.pypa.io/en/stable/
cd buscavideos
pip install -r requirements.txt
python manage.py migrate

```
**nota**: es necesario tener instalado previamente [virtualenv](https://virtualenv.pypa.io/en/stable/)
**nota2**: por favor, asegurarse de no commitear la carpeta del entorno virtual.


##### Creación del superusuario
Se crea un superusuario con el comando 

```bash 
python manage.py createsuperuser
```

##### Correr el sistema
El sistema arranca localmente en modo de pruebas con los comandos 

```bash
python manage.py runserver
```

Pero solo estará disponible el admin en http://localhost:8000/admin/

### API
Se puede acceder a la API para descargar los datos de los videos

#### Lista de videos
##### Todos los videos
Se puede descargar el json con la lista de todos los videos en:

> http://localhost:8000/api/v1/videolist

#### Filtrados
Se puede descargar el json con videos filtrados por tags como se muestra en los siguientes ejemplos:

>  http://localhost:8000/api/v1/videolist?tag=TAG1

>  http://localhost:8000/api/v1/videolist?tag=TAG1&tag=TAG2

donde TAG1 y TAG2 son tags de los videos, en el primer ejemplo se muestran todos los videos que tienen el tag TAG1, en el segundo se muestran todos aquellos que tienen como tag TAG1 o TAG2.
