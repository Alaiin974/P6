# P6 (Alain CLAIN - OpenClassRooms - 2021)

Ce script a pour but d'installer et faire une configuration minimale :
LAMP (Apache MariaDB PHP) & déploiement Wordpress.

## PREREQUIS ##
apt install python && apt install python3

## Installation des paquets ##
apt install apache2 && apt install mariadb-server && apt install php7.3 && apt install "php-extensions-for-wordpress" && apt install wget

## Déploiement de Wordpress ##

wget "archive wordpress" | tar xvf "archive wordpress" | mv "archive wordpress" wordpress | cp -r wordpress /var/www/ | chmod -R 755 /var/www/wordpress | chown -R www-data:www-data /var/www/wordpress

## Création d'un Virtualhost ##
/etc/apache2/sites-available/wordpress.conf | systemctl a2ensite wordpress

## Création d'un utilisateur MariaDB & Crédation d'une BDD
user "wordpress" | pass "admin" | bdd "wordpress" | privileges

## Redémarrage des services
systemctl restart apache2 && systemctl restart mariadb
