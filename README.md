# Rogue_AP_manager

1)Je voulais initialement réaliser une petite interface graphique permettant différentes interactions (start un AP avec DHCP et DNS avec la possibilité d'utiliser un proxy HTTPS-->HTTP), l'idée était de pouvoir ajouter facilement d'autres interactions avec un type de programmation événementielle.

2)Deux principaux dossiers conf contenant tous les fichiers de configurations, et le dossier interface, contenant l'interface en question.

3) Configuration initiale
Penser à désactiver les services écoutant sur le port 53, personnellement j'avais le systemd-resolved qui fonctionnait sur le port 53. Pour lister les services écoutant sur le port 53 il suffit de faire la commande `sudo ss -lp 'sport = :domain' ## list service on port 53`. Je dois donc mettre une valeur à la main dans le fichier `/etc/resolv.conf` exemple : `nameserver 1.1.1.1`, qui servira de serveur DNS.
Avant de lancer `manager.py`, il faut une interface `wlan0mon` pour le monitoring.
Pour lancer : sudo Python3 ./manager.py

4) Utilisation et explication
- `config.sh` : Contient la configuration initiale permettant le routing des paquets. 
- `dnsmasq.conf` et `hostapd.conf` : Contiennent les configurations pour l'AP ainsi que pour le serveur DHCP/DNS
- `moniter_mode.sh` : Permet de passer une interface Wi-Fi en monitor mode
- `start_dnsmasq.sh` et `start_hostapd.sh` : Permettent de lancer l'AP ainsi que le serveur DHCP/DNS
- `stop_config.sh` : Permet d'arrêter le Forward des paquets.


Les différents éléments de l'interface : 
- Les deux listes représentent d'une les AP accessiblent, et l'autre la liste des clients.
- Le bouton Refresh permet d'actualiser ces listes
- Le bouton Deauth Client permet de déconnecter l'utilisateur connecté (Il faut selectionner le client et la borne Wi-fi).
- Range ip local : Définie la range d'IP fournit par DNSmasq.
- Nom interface pour l'AP : Représente la valeur de l'interface qui sera utilisée pour diffuser l'AP.
- Nom de l'AP : Représente le nom de l'AP
- Nom de l'interface vers internet : Représente la valeur de l'interface sortante.
- IP de l'interface pour l'AP : Représente l'ip de l'interface ainsi que la Gateway du client.
- Le bouton Set value interface/name : Permet de définir les valeurs des champs texte dans les fichiers de configuration.
- Le bouton Start/Stop fake AP : Permet de lancer l'AP, d'éditer les règles de Forward. Il permet également d'arrêter l'AP et de rollback les configurations
- Le bouton Start/Stop SSLstrip attack: Permet de lancer le proxy MITM pour faire du https--> http. Il applique également la bonne règle d'IPtables. Ce bouton sert également à désactiver le proxy, et à rollback la règle IPtables
- Le bouton Info : Permet de voir quel service tourne.

                