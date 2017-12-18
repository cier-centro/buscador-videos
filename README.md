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

