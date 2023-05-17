# Part 2 of UWCSE's Mininet-SDN project2
#
# based on Lab Final from UCSC's Networking Class
# which is based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.packet.arp import arp
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.ipv6 import ipv6
import pox.lib.packet as pkt

from pox.lib.packet.ethernet import ethernet
from pox.lib.addresses import IPAddr, IPAddr6, EthAddr

from pox.lib.util import str_to_bool, dpidToStr
from pox.lib.recoco import Timer

log = core.getLogger()

# Convenience mappings of hostnames to ips
IPS = {
    "h10": "10.0.1.10",
    "h20": "10.0.2.20",
    "h30": "10.0.3.30",
    "serv1": "10.0.4.10",
    "hnotrust": "172.16.10.100",
}

# Convenience mappings of hostnames to subnets
SUBNETS = {
    "h10": "10.0.1.0/24",
    "h20": "10.0.2.0/24",
    "h30": "10.0.3.0/24",
    "serv1": "10.0.4.0/24",
    "hnotrust": "172.16.10.0/24",
}


class Part4Controller(object):
    """
    A Connection object for that switch is passed to the __init__ function.
    """

    def __init__(self, connection):
        print(connection.dpid)
        # Keep track of the connection to the switch so that we can
        # send it messages!
        self.connection = connection

        # This binds our PacketIn event listener
        connection.addListeners(self)
        # use the dpid to figure out what switch is being created
        if connection.dpid == 1:
            self.s1_setup()
        elif connection.dpid == 2:
            self.s2_setup()
        elif connection.dpid == 3:
            self.s3_setup()
        elif connection.dpid == 21:
            self.cores21_setup()
        elif connection.dpid == 31:
            self.dcs31_setup()
        else:
            print("UNKNOWN SWITCH")
            exit(1)

    def s1_setup(self):
        print('Pasa trafico por S1')
        self._flood()
        pass

    def s2_setup(self):
        self._flood()
        pass

    def s3_setup(self):
        self._flood()
        pass

    def cores21_setup(self):
        self._block()
        self._table = {}  # Aqui guardaremos IP : (MAC,PUERTO)
        pass

    def dcs31_setup(self):
        self._flood()
        pass

    # Se manda todo el trafico a todos los puertos. Permitido por el proyecto
    def _flood(self, act=of.ofp_action_output(port=of.OFPP_FLOOD)):
        self.connection.send(of.ofp_flow_mod(action=of.ofp_action_output(port=of.OFPP_FLOOD),
                                             priority=1
                                             ))

    # Reglas para bloquear el host publico. Aplica a Cores
    def _block(self):
        self.connection.send(of.ofp_flow_mod(  # action=of.ofp_action_output(port = of.OFPP_NONE),
            priority=50,
            match=of.ofp_match(dl_type=0x0800,
                               nw_src=IPS['hnotrust'],
                               nw_dst=IPS['serv1'])))

        self.connection.send(of.ofp_flow_mod(  # action=of.ofp_action_output(port = of.OFPP_NONE),
            priority=40,
            match=of.ofp_match(dl_type=0x0800,
                               nw_src=IPS['hnotrust'],
                               nw_proto=pkt.ipv4.ICMP_PROTOCOL)))

    #Cuando un paquete no pasa por ninguna regla entra aquí
    def _handle_PacketIn(self, event):
        """
        Packets not handled by the router rules will be
        forwarded to this method to be handled by the controller
        """

        packet = event.parsed  # This is the parsed packet data.
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        packet_in = event.ofp  # The actual ofp_packet_in message.

        print("--------------------------------------")
        if packet.type == packet.ARP_TYPE:
            print("Entra ARP")
            self._handle_ARP(packet, event)
            return
        elif isinstance(packet.next, ipv4):
            print("Entra IPv4")
            self._handle_traffic(packet, event)
            return
        elif isinstance(packet.next, ipv6):
            print("La topología no maneja paquetes IPv6.")
            return

        print(
            "Unhandled packet from " + str(self.connection.dpid) + ":" + packet.dump()
        )
        

    def _handle_ARP(self, p, event):
        n = p.next

        # Se verifica que sea una peticion ARP
        if n.opcode == arp.REQUEST:
            print("ARP request desde: " +
                  str(n.protosrc) + " a: " + str(n.protodst))

            # Se actualiza la info de la tabla
            self._update(event.port, p, isArp=True)
            print("Actualizado")

            # Se responde a la request
            self._reply_arp(p, event)

    # Funcion que guarda y actualiza la tabla del switch-router
    def _update(self, inport, packet, isArp=False):
        # Se escoge la direccion segun el tipo de mensaje
        if isArp:
            src = packet.next.protosrc
        else:
            src = packet.next.srcip

        # Se indica si se actualizo o se gano nueva info
        if src in self._table and self._table[src] != (packet.src, inport):
            print("Cambio en la tabla para: " + str(src))
        elif src not in self._table:
            print("Se descubrio: " + str(src))

        # Se hace el cambio
        self._table[src] = (packet.src, inport)
        print("Tabla: ")
        print(self._table)

    #Funcion que responde la ARP request
    def _reply_arp(self, p, event):
        
        print("Generando respuesta ARP")
        me = event.connection.dpid
        n = p.next

        # Se crea una ARP reply, esto de aqui es solo el contenido
        r = pkt.arp() #Que protocolo es
        r.hwtype = n.hwtype
        r.prototype = n.prototype
        r.hwlen = n.hwlen
        r.protolen = n.protolen
        r.opcode = pkt.arp.REPLY #Que tipo de mensaje es
        r.hwsrc = EthAddr("%012x" % (me & 0xffFFffFFffFF,)) #Cual es la direccion MAC source. Como estamos finjiendo que es una respuesta, subimos la direccion que le deberia estar respondiendo    ##IMPORTANTE##
        r.hwdst = n.hwsrc #Cual es la direccion MAC destino. Como estamos finjiendo que es una respuesta, subimos la direccion del host que lo pidio
        r.protosrc = n.protodst #Cual es la direccion IP source. Mismo razonamiento anterior
        r.protodst = n.protosrc #Cual es la direccion IP de destino. Mismo razonamiento anterior
        
        # Este contenido se encapsula en un paquete ethernet
        e = pkt.ethernet(type=pkt.ethernet.ARP_TYPE, 
                         src=EthAddr("%012x" % (me & 0xffFFffFFffFF,)), 
                         dst=n.hwsrc)
        e.set_payload(r)

        # Se crea el mensaje y se envia
        msg = of.ofp_packet_out()
        msg.data = e.pack()
        msg.actions.append(of.ofp_action_output(port=of.OFPP_IN_PORT))
        msg.in_port = event.port
        event.connection.send(msg)
        print("Se respondio a: " + str(r.protosrc) + " con " + str(r))


    # Se reenvia el paquete y se añade la regla según lo indicado en el proyecto
    def _handle_traffic(self, p, event):
        
        #De nuevo, se actualiza por si hay info nueva
        self._update(event.port, p)

        #Conozco la direccion de destino
        if p.next.dstip in self._table:
            ip = p.next.dstip

            dst = (self._table[ip][0], self._table[ip][1])  # MAC, PUERTO

            # Verifica que la tabla no esté mal. Si quiere salir por el de llegada, algo va mal
            if dst[1] == event.port:                            
                print("El mensaje quiere ser reenviado por el puerto de entrada " + str(event.port))
            else:
                # Se define la acción
                act = [of.ofp_action_dl_addr.set_dst(dst[0]),      
                      of.ofp_action_output(port=dst[1])]         
                 
                # Se define el match
                print("Paquete: " + str(p))
                match = of.ofp_match.from_packet(p, event.port)

                # Se construye una nueva regla
                regla = of.ofp_flow_mod(command=of.OFPFC_ADD,   
                                        idle_timeout=10,        
                                        hard_timeout=of.OFP_FLOW_PERMANENT,
                                        buffer_id=event.ofp.buffer_id,
                                        actions=act,
                                        match=match)
                
                event.connection.send(regla)
                
                print('Se añadió regla. Tráfico para ' + str(ip) + ' sale por ' + str(dst[1]))
                print("Regla: " + str(regla))
                print("Accion: " + str(act))
            
        else:
            print("No se conoce " + str(p.next.dstip))


def launch():
    """
    Starts the component
    """

    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        Part4Controller(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)

