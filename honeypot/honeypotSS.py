#!/usr/bin/python
import socket
import os

puerto = 23 #23 puerto telnet (el mas atacado) otros 22 y 445

honey_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
honey_socket.bind( ('', puerto) )
honey_socket.listen( 1 )
print 'Honeypot a la escucha puerto: ', puerto

while True:
    conexion_entrante,info_conexion = honey_socket.accept()
    try:
	    conexion_entrante.send('Ups... te has equivocado esto es un honeypot\r\n')
    except socket.error, e:
	    print "honeypotSS2 error en socket:", e, "=> nmap -ST", info_conexion[0]
    conexion_entrante.close()
    print "honeypot conexion desde " , info_conexion[0]
	
    # Aqui decides que quieres hacer con los datos de la ip capturada.
    # ej Registrar avisar , banear .....
    #os.system("logger -p auth.info honeypot conexion desde "+ info_conexion[0])
    #os.system("iptables -A INPUT -s " + info_conexion[0] + " -j DROP ")
    os.system("fail2ban-client set ssh banip "+info_conexion[0])
    #os.system("curl 'http://honeymap_server/ipban?ip="+info_conexion[0]+"&m=honeypot'&")#ojo con los &
    #os.system("echo "+info_conexion[0]+" > /dev/udp/honeymap_server/1234")

honey_socket.close()
print 'Fin programa!'
