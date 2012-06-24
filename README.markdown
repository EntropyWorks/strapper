About
=====

Strapper is a web application to manage the mapping between MAC addresses and different releases of boot images. It is written in Python and is based on the Flask microframework.

Details
=======

Strapper reads the files matching /var/www/pxeboot/<image>/<release>/boot.pxe, and presents them as releases of different boot images. 

Whenever a node requests boot configuration from http://bootstrap/boot/XX:XX:XX:XX:XX:XX (MAC address), it becomes visible in the web interface and can be mapped to an image and release. At the next boot request, the node will boot from the specific image.

Features
========

* Logging to syslog and /var/log/strapper/. The latter is also presented in the web interface.
* The nodes are logically grouped together based on the domain part in the reverse DNS name of the IP addresses.
* Configuration for each MAC address is stored in json structures in /var/lib/strapper/ and is easy to replicate between bootstrap servers using unison or similar software.

Common requirements
===================

* A DHCP server allocate IP-addresses.
* A TFTP server to serve iPXE boot firmware.
* A web server for the strapper and the boot images.
* Some Python standard modules for the strapper.
* Write access to /var/log/strapper/ and /var/lib/strapper/.

