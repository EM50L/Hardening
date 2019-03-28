# Hardening
hardening o endurecimiento es el proceso de asegurar un sistema reduciendo sus vulnerabilidades o agujeros de seguridad.

## HoneypotSS.py
en este scritpt **de 24 lineas** presento un honeypot (tarro de miel) que combinado con un Banneo (bloqueo de ip a nivel de cortafuegos). 
Nos va ha permitir parar/bloquear muchos ataques incluso antes de que se produzcan.

Explicacion: en el caso de los servidores una buena tactica de defensa es anticiparse a los ataques. Bloqueando al atacante incluso antes de que se inicie dicho ataque.

Como: casi todo ataque va precedido de una deteccion/escaner. En este caso colocaremos un servicio muy goloso pero falso. (de ahi viene lo de honeypot o tarro de miel)
