#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import os
import time

##### VARIABLES #####

a2dir = "sed -i 's/html//g' /etc/apache2/sites-enabled/000-default.conf"

wpdir = '/var/www/'
## ADMIN INTERACTION |1|
wpdirname = raw_input ("|1| Choose a name for the Wordpress Directory : " )
wpdirname1 = 'mv wordpress ' + '/var/www/' + wpdirname
chwpdir = 'chmod -R 755 /var/www/' + wpdirname + ' && chown -R www-data:www-data /var/www/' + wpdirname

vhconfname = wpdirname + ".conf"
vhconfcp = 'cp virtualhost.conf /etc/apache2/sites-available/' + vhconfname
## ADMIN INTERACTION |2|
servername = raw_input ("|2| Specify the domain name for the Wordpress website : ")
vhservername = "sed -i 's/wp.default/" + servername + "/g' /etc/apache2/sites-available/" + vhconfname
vhdocroot = "sed -i 's/wpdefault/" + wpdirname + "/g' /etc/apache2/sites-available/" + vhconfname

hosts = "sed -i '1i/" + "127.0.1.1       " + servername + " \n' /etc/hosts"

hostname = "sed -i 's/.*/" + wpdirname + "/g' /etc/hostname"

a2enre = 'a2enmod rewrite && a2ensite ' + vhconfname + ' && systemctl restart apache2'

## ADMIN INTERACTION |3|
dbname = raw_input ("|3| Choose a name for the Wordpress Database : ")
dbname2 = "mysql -u root -e " + '"create database ' + dbname +  '"'
## ADMIN INTERACTION |4|
dbusername = raw_input ("|4| Choose a name for the Database User : ")
## ADMIN INTERACTION |5|
dbpassword = raw_input ("|5| Choose a password for the Database User : ")

dbuser = "mysql -u root -e " + '"grant all privileges on *.* to ' + dbusername + '@localhost' + " identified by " + "'" + dbpassword + "'" + '"'

dbconn = "mv /var/www/" + wpdirname + "/wp-config-sample.php /var/www/" + wpdirname + "/wp-config.php"
dbconn2 = "sed -i 's/votre_nom_de_bdd/" + dbname + "/g' /var/www/" + wpdirname + "/wp-config.php"
dbconn3 = "sed -i 's/votre_utilisateur_de_bdd/" + dbusername + "/g' /var/www/" + wpdirname + "/wp-config.php"
dbconn4 = "sed -i 's/votre_mdp_de_bdd/" + dbpassword + "/g' /var/www/" + wpdirname + "/wp-config.php"

##### SET TIMEZONE #####

print ("----- SET TIMEZONE -----")
time.sleep(2)

os.system("dpkg-reconfigure tzdata")

##### PACKAGES INSTALLATON #####

print ("----- PACKAGES INSTALLATON : APACHE2, MARIADB-SERVER, PHP7.3, PHP7.3-MYSQL, WGET -----")
time.sleep(2)

os.system('apt install apache2 -y')
os.system('apt install mariadb-server -y')
os.system('apt install php7.3 php7.3-mysql -y')
os.system('apt install wget -y')

##### LATEST WORDPRESS ARCHIVE #####

print ("----- DOWNLOADING AND UNCOMPRESSING LATEST WORDPRESS ARCHIVE -----")
time.sleep(2)

#os.system('wget https://wordpress.org/latest.tar.gz')
os.system ('tar xvf latest.tar.gz')

##### /VAR/WWW/HTML & APACHE CONF #####

print ("----- SETTING DEFAULT APACHE DIRECTORY -----")
time.sleep(2)

os.system(a2dir)
os.system('rm -r /var/www/html')

##### WORDPRESS DIRECTORY #####

print ("----- SETTING WORDPRESS DIRECTORY -----")
time.sleep(2)

os.system(wpdirname1)
os.system(chwpdir)

##### VIRTUALHOST #####

print ("----- SETTING VIRTUALHOST -----")
time.sleep(2)

os.system(vhconfcp)
os.system(vhservername)
os.system(vhdocroot)

##### /ETC/HOSTS #####

print ("----- SETTING /ETC/HOSTS -----")
time.sleep(2)

os.system(hosts)

##### /ETC/HOSTNAME #####

print ("----- SETTING /ETC/HOSTNAME -----")
time.sleep(2)

os.system(hostname)

##### ENABLE SITE & RESTART APACHE #####

print ("----- ENABLING SITE  & RESTARTING APACHE -----")
time.sleep(2)

os.system(a2enre)

##### WORDPRESS DATABASE #####

print ("-----SETTING WORDPRESS DATABASE -----")
time.sleep(2)

os.system(dbname2)
os.system(dbuser)
os.system("systemctl restart mariadb")

##### DATABASE CONNECTION #####

print ("----- SETTING DATABASE CONNECTION -----")
time.sleep(2)

os.system(dbconn)
os.system(dbconn2)
os.system(dbconn3)
os.system(dbconn4)

##### SECURE MARIADB #####

print ("----- SECURE MARIADB -----")
time.sleep(2)

os.system("mysql_secure_installation")

##### WORDPRESS READY #####

print ("----- WORDPRESS IS READY TO INSTALL ! -----")
time.sleep(2)

print ("----- SERVER IS GOING TO REBOOT -----")
time.sleep(2)

print ("----- WHEN SERVER IS REBOOTED : GO TO http://" + servername + "/ -----")
time.sleep(5)

os.system("systemctl reboot")
