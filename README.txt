
Pasos para correr el servicio y la aplicación web asumiendo que que python 2.7 y pip están instalados y mongodb corriendo en localhost en el puerto 27017 (configuración estándar):

1) Instalar todas las dependencias necesarias (pymongo, flask, flask_cors y django). Esto puede hacerse ejecutando el siguiente comando en un terminal bash:

	pip install -r requirements.txt

2) Crear una base de datos mongodb con la información de los campamentos. Para ello, ejecutar el archivo load_database.py. Esto puede hacerse en un terminal bash ejecutando el comando:
	python service.py
	

3) Ejecutar el servicio. Esto se hace ejecutando el archivo service.py a través del comando:

	python service.py

El servicio estará disponible en localhost bajo el subdominio camps en el puerto 9000 a través del método get. Recogerá como parámetros el ratio, el valor absoluto de la latitud y el valor absoluto de la longitud en ese orden, todos escritos como floats (x = x.0 en caso de tratarse de un número entero). Por ejemplo, para acceder a los campamentos a un radio no mayor a 0.05 (grados) desde el punto con latud -33.7 y longitud -70.67 se ingresa a la siguiente url:

http://localhost:9000/camps/0.05&33.7&70.67


4) Ejecutar la aplicación web. Para eso, con el servicio corriendo, se ejecuta la aplicación desarrollada en django con el siguiente comando:

	python manage.py runserver

Esto permitirá acceder a la aplicación en localhost en el puerto 8000. Específicamente en la url: http://localhost:8000/campamentos/


Para utilizar la aplicación basta ingresar un ratio de búsqueda y hacer click en el boton de búsqueda.





