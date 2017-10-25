
Pasos para correr el servicio y la aplicación web asumiendo que que python y pip están instalados:

1) Instalar todas las dependencias necesarias (pymongo, flask, flask_cors y django). Esto puede hacerse ejecutando el siguiente comando en un terminal bash:

	pip install -r requirements.txt

2) Ejecutar el servicio. Esto se hace ejecutando el archivo service.py a través del comando:

	python service.py

El servicio estará disponible en localhost bajo el subdominio camps en el puerto 9000 a través del método get. Recogerá como parámetros el ratio, el valor absoluto de la latitud y el valor absoluto de la longitud en ese orden. Por ejemplo, para acceder a los campamentos a un radio no mayor a 0.05 (grados) desde el punto con latud -33.7 y longitud -70.67 se ingresa a la siguiente url:

http://localhost:9000/camps/0.05&33.7&70.67

El servicio recoge la información de una base de datos MongoDB que está corriendo en un servidor. Para cargar la información en la base de datos desde el archivo JSON se utilizó el ejecutable load_database.py. Si se ejecuta volverá a cargar los datos.

3) Ejecutar la aplicación web. Para eso, con el servicio corriendo, se ejecuta la aplicación desarrollada en django con el siguiente comando:

	python manage.py runserver

Esto permitirá acceder a la aplicación en localhost en el puerto 8000. Específicamente en la url: http://localhost:8000/campamentos/


Para utilizar la aplicación basta ingresar un ratio de búsqueda y hacer click en el boton de búsqueda.





