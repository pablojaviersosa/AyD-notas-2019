@startuml

Caso de uso: Loguearse en el sistema
=================================

**ID**: CU001

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

|  | 3a. El sistema informa que el usuario es incorrecto y solicita que se modifique, blanqueando los datos ingresados|
|  | 4a. El sistema activa algún tipo de protección de robots|
3b. ...

Section: A subsection of the use case, e.g. Paying by cash
-----------
| Actor Action | System Response |
|:--------------|:----------------|
| 1. This use case begins when Actor wants to initiate an event.| |
| 2. The Actor does something... | 3. The system determines something or responds... |
|4. ||
|5. | 6. |
@enduml

