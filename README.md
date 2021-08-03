## P6 (Alain CLAIN - OpenClassRooms - [AIC] - 2021) ##

|1| lamp-wp.py : Script deploying LAMP & Wordpress
|2| letsencrypt.py : Script deploying Free R3 SSL Cerficate

## REQUIREMENTS ##

1) The Server is freshly installed with Debian 10 Buster (Should work with Debian 9 Stretch)
--> PLEASE DO A SNAPSHOT BEFORE EXECUTING THE SCRIPT <--

2) A private/public IP address has to be set
--> PLEASE CHECK THAT YOU HAVE AN INTERNET ACCESS <--

INFO : If you want to generate R3 SSL Certificate, the server must have a public IP. 

3) Theses packages have to be installed :
apt install python git

## TO EXECUTE A SCRIPT, DO :

python script.py

## |1| lamp-wp.py - WHAT IT DOES ? ##

1) Set Timezone
2) Install apache2, mariadb-server, php7.3, php7.3-mysql, wget
3) Do mysql_secure_installation
4) Download & Uncompress latest Wordpress archive
5) Define "DocumentRoot /var/www/" in 000-default.conf && Delete 'html' directory in '/var/www'
6) Move Wordpress directory to /var/www/ & chmod 755 + chown www-data:www-data
7) Create virtualhost & Define ServerName & Define DocumentRoot
8) Edit /etc/hosts
9) Edit /etc/hostname
10) Activate Rewrite & Enable site & Restart apache2
11) Create Wordpress Database & User & Password & Restart mariadb
12) Connect Wordpress to Database

--> After rebooting, you can go to http://your.domain/ to finish wordpress installation.

## |2| letsencrypt.py - WHAT IT DOES ? ##

Check : https://certbot.eff.org/lets-encrypt/debianbuster-apache

## SUPPORT MAIL :
clain_alain97423@outlook.fr
