# Hardening
hardening o endurecimiento es el proceso de asegurar un sistema reduciendo sus vulnerabilidades o agujeros de seguridad.

## HoneypotSS.py
en este scritpt **de 24 lineas** presento un honeypot (tarro de miel) que combinado con un Banneo (bloqueo de ip a nivel de cortafuegos). 
Nos va ha permitir parar/bloquear muchos ataques incluso antes de que se produzcan.

Explicacion: en el caso de los servidores una buena tactica de defensa es anticiparse a los ataques. Bloqueando al atacante incluso antes de que se inicie dicho ataque.

Como: casi todo ataque va precedido de una deteccion/escaner. En este caso colocaremos un servicio muy goloso pero falso. (de ahi viene lo de honeypot o tarro de miel)

```
#!/usr/bin/python
import socket
import os

puerto  = 23 #23 puerto telnet

honey_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
honey_socket.bind( ('', puerto) )
honey_socket.listen( 1 )
print 'Honeypot a la escucha puerto: ', puerto

while True:
    conexion_entrante,info_conexion = honey_socket.accept()
    conexion_entrante.send('Ups... te has equivocado esto es un honeypot\r\n')
    conexion_entrante.close()
    print "honeypot conexion desde " , info_conexion[0]  
    #os.system("logger -p auth.info honeypot conexion desde "+ info_conexion[0])
    #os.system("iptables -A INPUT -s " + info_conexion[0] + " -j DROP ")
    os.system("fail2ban-client set ssh banip "+info_conexion[0])

honey_socket.close()
print 'Fin programa!'

```


## antiNmapS.py
Gracias al ataque que un amigo realizo contra mi honeypot
descubrimos que no detectaba algunos escaneos nmap.
asi que mejoramos el honeypot.

**y ademas surgio la idea de detectar escaneos nmap pasivamente.**
(sin tener un socket abierto)

en este script detecto las conexiones que realiza nmap contra una IP
** sin tan siquiera tener un socket a la escucha **
