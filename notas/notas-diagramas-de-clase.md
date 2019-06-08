#Notas sobre diagramas de clases

##Construyendo el diagrama de Dominio del sitema

###Relaciones entre clases.

<!-- * Asociacion  -->

<img src="../analisis y disenio sitema de movilidad/diagramas/asociaciones-uml.png"
alt="Asociaciones"
style="float: left; margin-right: 10px;" />

###Diagramas de maquinas de estados

Los estados se conectan por transiciones.

Los estados pueden tener actividaes. Entry Do, Exit

**De Comportamiento**
:  Especifica la implementacion de objetos.

**De Protocolo**
:
- No sera implementado.
 - Describe una secuencia de eventos sin mostrar el comportamiento especifico del objeto.


- Cada estado puede llevar actividades
- La transicion lleva una etiqueta que se conoce como firma.
- <gatillo>[<guard>]/<efecto>
- Gatillo es el evento
- Guarda es la condición.
- Efecto es la actividad que sucede durante la trnsición.
