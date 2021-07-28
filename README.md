# P6 (Alain CLAIN - OpenClassRooms - 2021)

#Ce script a pour but d'installer et faire une configuration minimale :
#LAMP (Apache MariaDB PHP) & déploiement Wordpress.

## PREREQUIS ##
## apt install python && apt install python3

1) Installation Apache2
--> apt install apache2

2) Installation MariaDB
--> apt install mariadb-server

3) Installation PHP
--> apt install php7.3 + php-extensions-for-wordpress

4) Installation wget
--> apt install wget

5) Déploiement de Wordpress
--> wget "archive wordpress"
--> tar xvf "archive wordpress"
--> mv "archive wordpress" wordpress
--> cp -r wordpress /var/www/
--> chmod -R 755 /var/www/wordpress
--> chown -R www-data:www-data /var/www/wordpress

6) Création d'un Virtualhost
--> /etc/apache2/sites-available/wordpress.conf
--> systemctl a2ensite wordpress

7) Création d'un utilisateur MariaDB & Création d'une BDD

8) systemctl restart apache2 && systemctl restart mariadb
