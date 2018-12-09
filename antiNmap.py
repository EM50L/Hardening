#!/usr/bin/python
import os
print 'detecta y bannea(bloquea) ips que intentan escanear este servidor.'
filtro_pcap="inbound and (dst portrange 1-79 or dst portrange 81-442 or dst portrange 444-1879)"

while True:
    tcpdump=os.popen('tcpdump -c1 -nn -l "'+filtro_pcap+'"').read()
    print tcpdump #tcpdump contiene la informacion en bruto del paquete capturado

    ip_mala=tcpdump.split(' ')[2].split('.')#la ip esta en la 3palabra[2] desde el principio
    ip_mala=ip_mala[0]+"."+ip_mala[1]+"."+ip_mala[2]+"."+ip_mala[3]#recompongo(quitando ultimo bloque .XXXX)
    print "ip_mala:",ip_mala

    puerto = tcpdump.split('.')[9].split(',')[0].replace(' ','').replace('Flags[','').replace(']','')
    print "puerto:",puerto

    os.system("fail2ban-client set ssh banip "+ip_mala)
    #os.system("curl 'http://honeyServer/ipban?ip="+ip_mala+"&m=antiNmap192+P"+puerto+"'")#ojo con los &

print 'Fin programa!'
