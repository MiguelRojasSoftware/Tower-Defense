Tower Defense

Un juego básico de Tower Defense desarrollado en Python utilizando la librería Pygame. El objetivo del juego es colocar torres estratégicamente en el mapa para detener a los enemigos antes de que lleguen al final del camino.
Características:

    Enemigos: Se generan enemigos que siguen un camino predefinido.
    Torres: Puedes colocar torres para disparar a los enemigos y detenerlos.
    Puntuación: Obtén puntos y dinero por cada enemigo destruido.
    Botones: Incluye botones para reiniciar el nivel o salir del juego.
    Finalización del nivel: El juego se completa cuando se llega al numero de enemigos derrotados por nivel, y puedes reiniciar el nivel para continuar jugando.

Controles:

    Colocar Torres: Haz clic en el mapa para colocar torres.
    Reiniciar Nivel: Haz clic en el botón de "Reiniciar Nivel" para reiniciar el juego.
    Salir: Haz clic en el botón de "Salir" para cerrar el juego.

Limitaciones:

    Interacción con los botones: Al hacer clic en el área de los botones (reiniciar o salir), puede ocurrir que se coloque una torre accidentalmente en el botón. Se recomienda hacer clic cuidadosamente.
    Limitado a una torre en el juego: El sistema solo permite colocar una torre de un tipo básico, sin opciones de mejorarla.
    Enemigos básicos: Los enemigos en este juego son simples, sin comportamientos complejos ni variaciones significativas de dificultad.
    Dificultad: Puesto que es un juego sencillo y basico el nivel 1 es muy facil de pasar, aun asi esto puede escalar a crear una clase para generar caminos mas complejos y multiplicar el numero de enemigos basico que trae por defecto el nivel 1 en main.
    Aspectos Esteticos: Algunas figuras estan realizadas de forma sencilla por lo mismo algunos textos salen de su espacio asignado.

Errores:

    Trayectoria de proyectiles: la trayectoria de proyectiles es sencilla y utiliza la posicion del enemigo al que se le disparo por lo mismo el movimiento del proyectile hace movimientos extraños al dirigirse hacia el enemigo.
