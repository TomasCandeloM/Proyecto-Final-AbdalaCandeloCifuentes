# Proyecto-Final-Abdala Candelo Cifuentes

## **Parte 1: Redes Definidas por Software (SDN)**

Las redes tradicionales se ven altamente caracterizadas por la presencia de dispositivos como lo son routers y switches principalmente, que cuentan con un plano de datos, encargado del reenvío de información, y un plano de control que es donde se implementa el software encargado de el correcto funcionamiento de cada dispositivo. Los avances en comunicaciones que se están presentando están comenzando a desvelar dificultades en las redes tradicionales entre las que destacan la gran inversión de tiempo que se requiere para añadir nuevos dispositivos a una red debido a la complejidad que se requiere para administrarlas, y la poca escalabilidad que se da con las redes tradicionales debido a los avances casi inexistentes que se han dado en el campo en los últimos años [1]. Por ello se proponen las SDN (Redes Definidas por Software).
Las SDN surgen como un paradigma de red relativamente nuevo [1]. El principal cambio con las redes tradicionales es el desacople que se hace entre el plano de reenvío de datos y el plano de control. En otras palabras, el principal objetivo de esta solución es que se sigan manteniendo los dispositivos de red tradicionales, pero que el software necesario para su funcionamiento sea configurado por medio de un controlador central que usa un protocolo para comunicarse con los controladores de red, este protocolo se llama OpenFlow y permite programar de manera más sencilla y eficiente el funcionamiento de cada uno de los dispositivos pertenecientes a la red, brindando facilidad a la hora de gestionar la misma [2].

![Esquema gráfico de diferenciación entre redes tradicionales y redes SDN](images/esquema_comparación.png)

OpenFlow recopila por medio de mensajes estandarizados datos relacionados con el flujo, esto con el propósito de crear tablas que determinen cuál es la mejor manera de reenviar paquetes y de esta manera brindar la información y cambios necesarios a los dispositivos de red para mejorar la eficiencia de la red de una manera dinámica y automatizada, reduciendo notablemente el tiempo de configuración y los costos operacionales en las empresas de telecomunicaciones [2].

## Tipos de SDN

Las SDN pueden verse divididas en principalmente cuatro tipos [3] cuales son:

·        SDN Overlay Model: Los dispositivos son programables por aplicaciones como lo puede ser OnePK, estas aplicaciones se ejecutan en el mismo dispositivo o en un servidor en la red.

·        Open SDN: Utiliza un controlador centralizado el cual tiene conocimiento sobre todos los dispositivos de la red, lo que da una facilidad mayor a la hora de gestionar la red desde el controlador.

·        SDN by APIs: Las políticas están establecidas principalmente para recopilarlos y así determinar el comportamiento de la red. Se deben priorizar ciertos casos para así anticipar algunas situaciones que podrían afectar el desarrollo de la red.

·        Hybrid SDN: Este tipo de SDN es la combinación de una SDN perteneciente a cualquiera de las anteriores tres con una de red tradicional para poder ejecutar diferentes funciones verificando que no se generen dificultades por el cambio de estructura o de configuración de las redes.

## Funcionamiento del paradigma SDN 

El SDN presenta diferencias frente al tradicional, la más importantes son los llamados controllers, pueden ser representados como servidores con la capacidad de ejecutar el software controlador.[4] La figura muestra la topología de una red implementada a través de SDN

![Topologia de red con paradigma SDN](images/topologia_paradigmaSDN.png)

Para establecer comunicación entre el PC-A y el PC-B, envía una trama a través de la interfaz conectada al switch como en el paradigma tradicional, cuando la trama está dentro de switch el paradigma entra en uso, esté observa y analizar los encabezados recibidos, puede analizar headers de capa 2, 3 y 4, mientras que el paradigma tradicional solo revisar los de capa 2. Si el switch no tiene información en sus tablas de flujo este paquete será enviado al controlador para obtener información necesaria sobre qué hacer con dicho paquete, el controlador indica al switch que el paquete se debe enviar por el puerto 1 dándole nueva información a su tabla de flujo, este proceso se repetirá cada vez que el paquete pase de un dispositivo a otro. Cuando llega a su destino, si se genera una respuesta el paquete hace este mismo procedimiento para determinar la ruta, cuando genera comunicación bidireccional los paquetes enviados entre estos dos hosts no se envían al controlador[4].

Las políticas de enrutamiento para definir el comportamiento de la red son definidas por el administrador o programador de la red en el controlador, permite programar el comportamiento de la red a voluntad del administrador haciendo que el paquete se enruta hacia determinado puerto de muchas maneras, algunas son la dirección MAC, IPv4 o IPv6 de origen o destino, entre otras. Cada dispositivo tiene una tabla de enrutamiento, pero el controlador tiene el mapa controlador que llena la tabla de cada switch en base a su necesidad [4].

Adicionalmente con la arquitectura del SDN se obtiene una gestión independiente del proveedor en toda la red desde un aspecto lógico, simplificando el diseño de red en operadores basados en software los cuales componen la capa de control que es intermediaria para las capas de infraestructura y la capa de aplicación[5].

![Arquitectura del paradigma SDN](images/arquitectura_paradigma_SDN.png)

## Ventajas del paradigma SDN frente al modelo tradicional

Un estudio [6] busco analizar los resultados entre una topología tradicional y una con SDN, realizando consultas a través del ICMP la obtención de datos se realizó observando los parámetros del sistema durante la simulación, los resultados determinaron dos ventajas del SDN: Su rendimiento es mejor y su base en protocolos y estándares abiertos, este último tiene algunos inconvenientes: incompatibilidad entre protocolos SDN, características de funcionalidad exclusivas definidas por  proveedores, limitando a marcas específicas al considerar la escalabilidad para tener una mayor productividad en la infraestructura de red[6].

Otra ventaja es la adaptabilidad a la naturaleza cambiante de las funciones y aplicaciones inteligentes, esta capacidad reduce costes de infraestructura y administración simplificada. Las implementaciones de modelos basados en SDN permiten la facilidad de estas aplicaciones en redes amplias, aunque el alcance a redes LAN está condicionado a su funcionamiento[6].

Algunos beneficios adicionales propuestos por Vadluri [5], son la eficiencia en la gestión, esta permite manipular las cualidades de la red desde otra ubicación, la programabilidad de la red se maneja de forma más eficiente y centralizada mejorando la funcionalidad del diseño del tráfico y disminuir el bloqueo y ofrece vigilancia delicada en los dispositivos mejorando la protección de un entorno virtualizado[5].

## **Parte 2 Red Empresarial Mininet**

## Instalación
## Oracle VM Virtual Box
Debido a los requerimientos para el uso de Mininet, software que solo puede ser ejecutado en el sistema operativo Linux, fue necesario hacer uso del servicio Oracle VM Virtual Box ofrecido por la empresa Oracle con el propósito de crear un entorno virtualizado que trabaje bajo el sistema operativo anteriormente mencionado. Para ello es necesario descargar la aplicación desde el sitio oficial de la empresa e instalarla. Si bien es posible crear directamente un entorno de Linux haciendo uso del servicio, se prefirió por facilidades del desarrollo del proyecto crear la máquina virtual por medio de el Software Vagrand que nos brinda directamente las herramientas necesarias para el desarrollo del proyecto sin necesidad de requerir una gran cantidad de instalaciones adicionales ya dentro de la máquina virtual. Si bien más adelante se hablará de la instalación de Vagrand, por el momento es importante tener en cuenta que, si bien la máquina virtual es creada con este software, esta puede ser inicializada desde Oracle VM Virtual Box como si se hubiera creado en la aplicación, facilitando el acceso al entrono virtualizado que se usará para el desarrollo del proyecto.

![Logo Oracle VM Virtual Box](images/ORACLE_VM_LOGO.jpg)


## Vagrant

Como ya fue mencionado vagrant sera el sistema que nos permitira tener las herramientas de mininet a la mano para poder realizar los requerimientos del proyecto, para la instalación descargamos el programa en la pagina de vagrant y lo instalamos. 

Posteriormente necesitamos clonar un repositorio de git que utilizamos para instalar mininet, para este proyecto utilizamos el siguiente git: https://gitlab.cs.washington.edu/561p-course-staff/mininet-environment. Est git especificamente tiene caracteristicas necesarias para el uso de mininet que otros metodos de instalación no tenian como lo son caracteristicas adicionales en el vagrant file. 

Una vez ya tenemos clonado el repositorio de git, creamos una carpeta donde esta clonado el git, en el cmd accedemos a esta carpeta y utilizamos el comando **vagrant up**, con este comando iniciaremos vagrant, el cual implementara todas las funciones de mininet, cuando este termina podremos ver en nuestra maquina virtual, que la instancia de mininet ha sido creada y esta corriendo en segundo plano

![Instalación de vagrant en la virtual machine](images/virtual-box-vagrant.png)

## puTTY

Para el desarrollo del laboratorio fue necesario hacer uso de la herramienta puTTY, esto con el propósito de crear una conexión SSH con cada nodo de la topología establecida. Esto funciona para poder acceder a la línea a de comando de cada nodo de manera más fácil y administrarlos como si se estuviera trabajando directamente en cada uno. Con esto se puede monitorizar y hacer pruebas de funcionamiento para el desarrollo del proyecto. 
La instalación de puTTY es bastante simple. Lo primero será descargarlo desde su sitio web e instalarlo en el dispositivo. Después de haber iniciado sesión como usuario Vagrant, será necesario hacer uso del servicio puTTY Key Generator, esta herramienta será usada para lograr hacer que la private key que nos brinda Vagrant pueda ser leída y entendida por puTTY.

![puTTY Key Generator](images/puTTY-KEY-GENERATOR.png)

Se guardará el archivo de la nueva private key que después tendrá que ser configurada en puTTY. Seguido a esto, ya podremos comenzar a configurar desde puTTY. Ya dentro de la aplicación , Vagrant nos dará unas especificaciones como por ejemplo el puerto, lo que será necesario al momento de configurarlo.

![puTTY Configuration](images/puTTY-CONFIGURATION.png)

Después de esto, será necesario activar el servicio Xming, este no abrirá ninguna ventana, sin embargo, comenzará a correr en segundo plano. En la barra de tareas, este servicio nos brindara un dato que también es necesario para configurar en puTTY.

![puTTY and Xming Connection](images/puTTY-XMING-CONNECTION.png)

Seguido a esto, será necesario brindarle las credenciales de acceso del usuario de Vagrand a puTTY para que este pueda acceder de manera automática cuando sea necesario.

![puTTY Credentials](images/puTTY-CREDENTIALS.png)

Finalmente, se guardarán todas las configuraciones asignadas en un usuario llamado Vagrant (Fue el elegido, no necesariamente tiene que ser esta) que será el que nos brinde la posibilidad de usar todas las opciones de puTTY en la máquina virtual creada por Vagrant.

## SSH en visual studio
Una vez tenemos los componentes presentados anteriormente, para el caso de este grupo decidimos manipular la caracteristicas de mininet a travèz de visual studio ya que es mucho más sencillo de realizar los requerimientos que en la propia consola de la maquina virtual.

Para establecer conexion entre nuestra maquina virtual y el entorno de visual studio por medio de ssh y configurar las propiedades de los archivos, en el powershell de microsoft usamos el comando **vagrant ssh-config**. Este comando nos proporcionara diferente información. 

Desde visual studio sera necesario instalar la extención de remote developer, esta de igual manera instalara automaticamente algunas extenciones adicionales **(ssh, ssh editing)** cuando esta instalado, en la esquina inferior izquierda del visual studio aparecera un boton con simbologia similar a ><, precionamos el boton y nos saldran diferente opciones de conexión. 

![Diferente opciones de conxión con ssh en visual studio](images/tipos-conexion-ssh.png)

En este caso nos queremos conectar a un host, le damos a **configure SSH host** apareceran dos archivos que tienen guardada nuestra configuración SSH,  escogemos la primer opción, en el archivo que nos muestre copiamos la información que obtubimos gracias al comando vagrant ssh-config, toda esta información sera la necesaria para la conexión ssh. Guardamos estos cambios y regresamos a la opción de connect to host y usamos la instancia previamente creada, esto abrira una pestaña la cual nos preguntara que tipo de sistema estamos conectando, para este caso elegimos la opción **Linux** y en la parte inferior podemos observar que ya tenemos la conexión al hosto por medio de ssh.

![Información conexión SSH](images/info-ssh.png)

Finalmente abrimos la carpeta desde la altura más alta para las carpetas de mininet donde esta el acceso a los dos proyectos, como pueba podemos usar el comando ls para ver las diferente carpetas desde la maquina virtual y podemos ver que dichas carpetas tambien son visibles y manipulables en visual. 

![Visualización de las carpetas en visual studio y en la virtual machine](images/verificacion-carpetasSSH.png)

## Xming

Para poder visualizar nuestra topologia y tener una acceso a miniedit, que es la interfaz grafica para visualizar todos los procesos realizados en mininiet, utilizamos Xming el cual es una implementación protatil que ofrece un sistema de ventanas para microsoft, para el caso de este proyecto utilizamos PuTTY para realizar una implemantación SSH con la que, al conectar con nuestro PuTTY, podremos tener una vista grafica.

Para utilizar Xming abrimos nuestro installer de PuTTY y entramos a miniedit, posterioremente necesitamos configurar PuTTY para indicarle en ssh que pueda realizar forwardin en X11 para mandar GUI a otro lado, Xming corre por defecto en el :0.0 por lo que tnemos que especificar este en el x11, cuando lo guardamos ya sabe a donde mandar la parte virtual. 

Ya con la interfaz abierta podemos abrir y movernos por las diferentes carpetas con las que viene la insatalación 

![Interfaz grafica de miniedit](images/Xming_interface.png)


## **Planteamiento**

## Topologia

Para ambos aprendizajes de este proyecto (necesario y experto) utilizamos la misma topologia de red empresaria expuesta a continuación, ya que para el proyecto se nos pidio plantear este tipo de redes en el paradigma SDN con las diferentes caracteristica que expondremos más adelante 

![Topologia usada para los proyectos de mininet](images/Topologia-mininet.png)

¿Comó sabemos que esta topologia pertenece a una red empresarial? Pues como podemos observar en las dirección IP que hacen parte de los host podemos darnoas cuenta que hacen parte de subredes diferentes ya que su tercer octeto incrementa con cada host con los que cuenta la topologia, ademas el servidor 1 y el switch dcs31 estan agrupado por aparte, estos dos dispositivos forman lo que es un datacenter dentro las red privada a la cual los demas hos pueden acceder por medio del cores21 y Finalmente el servidor hnottrust hace parte de una red publica, por eso lleva dicho nombre. 

Con estas caracteristicas principales podemos determinar que la topologia efectivamente es de una red empresarial.


## **Parte 3 verificación de funcionamiento**

## **Parte 4 recomendaciones y conclusiones**

## Recomendaciones

- Al momento de realizar la instalación de mininet existen variedades de opciones para usar mininet en la virtual box, sin embargo se recomienda la instalación presentada en el documento con Washington ya que este permitira una manipulación y configuración más eficiente por medio de visual studio

- Se recomienda la implementación de ssh con visual studio ya que permite una mayor facilidad y libertad para la configuración e implementación de la red, en especial para el apartado del aprendizaje experto fue una herramienta de mucha ayuda que nos permitio realizar diferentes modificaciones para hacer troubleshooting en nuestro codigo y solucionar muchos problemas 

- El uso de PuTTY consideramos que es un valor agregado ya que permite librarse de varios contras con los que cuenta el cmd de virtual box, cuando esta configurado tiene un axceso directo a xming para poder ver miniedit y simultaneamente tenr el apartado del pox controller, es decir que podemos tener varios PuTTys corriendo al tiempo, ademas de que corre en tu propio host por lo que todas tus caracteristicas pueden seguir siendo usadas y su navegación es mucho más sencilla.

## Conclusiones

Con la realización de este proyecto tanto en el apartado investigativo como en el apartado practico tenemos las siguientes conclusiones:

- Las redes SDN son paradigmas de red que estan en crecimiento, los cuales son configuraciones que permiten un mayor control en el trafico de paquetes, este paradigma trae consigo muchas ventajas como lo puede ser su libertad de configuración y que si se llega a presentar un problema en la topologia podemos arreglar el problema mucho más rapido que con el paradigma norma, sin embargo de igual manera cuenta con algunas desventajas como lo puede ser sus limitaciones y dificultad en la realización de las configuraciones. En resumen, el SDN es un paradigma muy util pero de igual maner requiere un conocimiento significativo para sacar todo el provecho de este


## **Bibliografia**

## Documentación parte 1

[1]      	J. Silva, «Tecnología de red definida por software para el aprendizaje en grupos de investigación y educación», Revista Innova Educación, vol. 3, n.o 3, pp. 85-96, jul. 2021, doi: 10.35622/j.rie.2021.03.005.

[2]      	D. Iglesias De La Torre, F. Álvarez Paliza y A. Ramos Fleites, «Combinación de los Mecanismos MPLS en una Arquitectura SDN,» Revista Telemática, vol. 18, n.° 1, pp. 1-10 ene. 2019.

[3]      	VM Ware, «VM Ware - Software Defined Networking,» VM Ware, 2023. [En línea]. Available: https://www.vmware.com/topics/glossary/content/software-defined-networking.html. [Último acceso: 09 05 2023].

[4]    	M. Ramírez and A. López, “Redes de datos definidas por software - SDN, arquitectura, componentes y funcionamiento Software,” Journal de ciencia e ingeniría, vol. vol.10, no, no. Redes de datos definidas por software, p. 7, 2018.

[5]    	M. Benifits and O. F. Sdn, “A COMPREHENSIVE REVIEW ON SDN ARCHITECTURE , APPLICATIONS AND A COMPREHENSIVE REVIEW ON SDN ARCHITECTURE , APPLICATIONS AND MAJOR BENIFITS OF SDN,” no. January, 2019.

[6]    	P. Alcívar and M. Navia, “Comparison between traditional network and software defined network: Case of study ESPAM MFL | Comparativa entre red tradicional y red definida por software: Caso de estudio ESPAM MFL,” RISTI - Revista Iberica de Sistemas e Tecnologias de Informacao, vol. 2020, no. E29, pp. 79–90, 2020.

## documentcación parte 2

- https://courses.cs.washington.edu/courses/csep561/22sp/projects/project2/
- https://gist.github.com/leomindez/3e6d29d341a0fd666e6ae799bfa32ca1
- https://courses.cs.washington.edu/courses/csep561/22sp/projects/project2/
- https://courses.cs.washington.edu/courses/csep561/22sp/projects/project1/
- https://noxrepo.github.io/pox-doc/html/#forwarding-l3-learning
- https://gitlab.cs.washington.edu/561p-course-staff/mininet-environment
- https://www.youtube.com/watch?v=MlACzrm0SCw&t=8s