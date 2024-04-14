# Backend + Base de datos + Servidor de correos

Este proyecto consiste en un backend desarrollado con Python y Django que incluye una base de datos PostgreSQL y un servidor de correos para enviar correos electrónicos. A continuación se detallan los pasos de configuración y explicación.

## Crea variables de entorno virtuales

```bash
pip install virtualenv
python -m venv venv
```

## Dependencias

Antes de comenzar, asegúrate de tener instalado Python, Django y las siguientes dependencias. Puedes verificar las dependencias ejecutando el siguiente comando en la consola dentro de la carpeta del backend:

```bash
pip list
```

Si falta alguna dependencia, instálala utilizando pip.

```bash
pip install django coreapi coreschema django-cors-headers djangoresframework
```

Realiza las migraciones necesarias para guardar los cambios:

```bash
python manage.py makemigrations employee
python manage.py migrate
```


Este README.md proporciona una guía completa sobre cómo configurar el backend, la base de datos y el servidor de correos, junto con las explicaciones necesarias para cada paso.
