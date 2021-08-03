## P6 (Alain CLAIN - OpenClassRooms - 2021) ##

|1| lamp-wp-py : Script deploying LAMP for Wordpress
|2| letsencrypt.py : Script deploying Free R3 SSL Cerficate

## REQUIREMENTS ##

1) The Server is freshly installed with Debian 10 Buster (Should work with Debian 9 Stretch)
--> PLEASE DO A SNAPSHOT BEFORE EXECUTING THE SCRIPT <--

2) A public IP address has to be set
--> PLEASE VERIFY THAT YOU HAVE AN INTERNET ACCESS <--

3) Theses packages have to be installed :
apt install python git

## |1| WHAT IT DOES ? ##

1) Set Timezone
2) Install apache2, mariadb-server, php7.3, php7.3-mysql, wget
3) Download & Uncompress latest Wordpress archive
4) Define "DocumentRoot /var/www/" in 000-default.conf && Delete 'html' directory in '/var/www'
5) Move Wordpress directory to /var/www/ & chmod 755 + chown www-data:www-data
6) Create virtualhost & Define ServerName & Define DocumentRoot
7) Edit /etc/hosts
8) Edit /etc/hostname
9) Activate a2enrewrite & enable site & restart apache2
10) Create Wordpress Database & User & Password & restart mariadb
11) Connect Wordpress to Database

--> After rebooting, you can go to http://yourdomain/ to finish wordpress installation.

## |2| WHAT IT DOES ? ##

Check : https://certbot.eff.org/lets-encrypt/debianbuster-apache

## SUPPORT MAIL : clai_alain97423@outlook.fr
