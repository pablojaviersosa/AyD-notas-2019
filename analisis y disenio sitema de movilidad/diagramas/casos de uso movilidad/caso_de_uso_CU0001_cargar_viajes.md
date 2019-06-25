@startuml

Caso de uso: Loguearse en el sistema
=================================

**ID**: CU0001

**Actores**: Investigador, Estudiante.

**Proposito**: Permite el acceso de los usuarios al sistema.

**Tipo**: Primario  

**Precondiciones**: El investgador debe haber registrado su cuenta previamente y debe encontrarse activa.
El Estudiante debe ser debe ser asignado aun formulario.

**Postcondiciones**: El usuario se encuentra en su vista inicial del sistema y dispone de todas sus funcionalidades.

Curso típico de las acciones:
----------------------

| Actor Acción | Respuesta del sistema |
|:--------------|:----------------|
| 1. El Investigador ingresa su usuario y contraseña en la pagina de login| |
|  | 2. El sistema verifica que exista el usuario y que la contraseña sea correcta||
|3.El investigador accede a la pantalla inicial del sistema||

Cursos Alternativos:
-----------
3a. El usuario es incorrecto 

|  | 3a. El sistema informa que el usuario o la contraseña es incorrecta y solicita que se modifique, blanqueando los datos ingresados|
|  | 4a. El sistema activa protección de robots|

3b. La contraseña

| Actor Acción | Respuesta del sistema |
|:--------------|:----------------|
||3b.El sistema envia un mensaje informando que el usuario o la contraseña son incorrectas, para no dar informacion de mas a posibles ataques |
||4b.El sistema blanquea los campos para que el usuario pueda ingresar los datos nuevamente|
||5b.El sitema habilita proteccion contra robots|

Seccion: El usuario ingresa mal su contraseña mas de 3 veces.
-----------
| Actor Acción | Respuesta del sistema |
|:--------------|:----------------|
| |1.El sistema bloquea la cuenta de usuario|
|  |2. El sistema envia mail de reactivacion de cuenta al usuario|
||3.El investigador accede al enlace ||
|||4.El sistema pide nueva contraseña|
||5.El usuario ingresa la contraseña||
|||6.El sistema pide confirmar contraseña|
||7.El usuario confirma la contraseña||
|||8.El sistema permite acceder a la pantalla inicial del sistema|

Cursos Alternativos:
-----------
3a.El usuario no ingresa al enlace 

|  | 3a. El sistema informa que el usuario o la contraseña es incorrecta y solicita que se modifique, blanqueando los datos ingresados|
|  | 4a. El sistema activa protección de robots|
@enduml

