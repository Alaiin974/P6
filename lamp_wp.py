#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import os
import time

##### PACKAGES INSTALLATON #####

print ("----- PACKAGES INSTALLATON : APACHE2, MARIADB-SERVER, PHP, WGET -----")
time.sleep(2)

os.system('apt install apache2 -y')
os.system('apt install mariadb-server -y')
os.system('apt install php7.3 php7.3-mysql -y')
os.system('apt install wget -y')

##### LATEST WORDPRESS ARCHIVE #####

print ("----- DOWNLOAD AND UNCOMPRESS LATEST WORDPRESS ARCHIVE -----")
time.sleep(2)

#os.system('wget https://wordpress.org/latest.tar.gz')
os.system ('tar xvf latest.tar.gz')

##### /VAR/WWW/HTML & APACHE CONF #####

print ("----- SETTING DEFAULT APACHE DIRECTORY -----")
time.sleep(2)

a2dir = ("sed -i 's/html//g' /etc/apache2/sites-enabled/000-default.conf")

os.system(a2dir)
os.system('rm -r /var/www/html')

##### WORDPRESS DIRECTORY #####

print ("----- SET WORDPRESS DIRECTORY -----")
time.sleep(2)

wpdir = '/var/www/' 
wpdirname = raw_input ("Wordpress Directory Name ? " )
wpdirname1 = 'mv wordpress ' + '/var/www/' + wpdirname
chwpdir = 'chmod -R 755 /var/www/' + wpdirname + ' && chown -R www-data:www-data /var/www/' + wpdirname 

os.system(wpdirname1)
os.system(chwpdir)

##### VIRTUALHOST #####

print ("----- SET VIRTUALHOST -----")
time.sleep(2)

vhconfname = raw_input ("Virtualhost.conf Name ? ")
vhconfcp = 'cp virtualhost.conf /etc/apache2/sites-available/' + vhconfname
servername = raw_input ("Server Name ? ")
vhservername = "sed -i 's/wp.default/" + servername + "/g' /etc/apache2/sites-available/" + vhconfname
vhdocroot = "sed -i 's/wpdefault/" + wpdirname + "/g' /etc/apache2/sites-available/" + vhconfname

os.system(vhconfcp)
os.system(vhservername)
os.system(vhdocroot)

##### SET /ETC/HOSTS #####

print ("----- SETTING /ETC/HOSTS -----")
time.sleep(2)

hosts = "sed -i '1i\127.0.1.1       " + servername + " \n' /etc/hosts"

os.system(hosts)

##### SET HOSTNAME #####

print ("----- SETTING HOSTNAME -----")
time.sleep(2)

hostname = "sed -i 's/.*/" + wpdirname + "/g' /etc/hostname"

os.system(hostname)

##### ENABLE SITE & RESTART APACHE #####

print ("----- ENABLE SITE  & RESTART APACHE -----")
time.sleep(2)

a2enre = 'a2enmod rewrite && a2ensite ' + vhconfname + ' && systemctl restart apache2'

os.system(a2enre)

##### SET TIMEZONE #####

print ("----- SET TIMEZONE -----")
time.sleep(2)

os.system("dpkg-reconfigure tzdata")

##### DATABASE #####

print ("-----SET WORDPRESS DATABASE -----")
time.sleep(2)

##### DATABASE #####

print ("-----SET WORDPRESS DATABASE -----")
time.sleep(2)

dbname = raw_input ("Database Name ? ")
dbname2 = "mysql -u root -e " + '"create database ' + dbname +  '"'

os.system(dbname2)

dbusername = raw_input ("Database User ? ")
dbpassword = raw_input ("Database User Password ? ")

dbuser = "mysql -u root -e " + '"grant all privileges on *.* to ' + dbusername + '@localhost' + " identified by " + "'" + dbpassword + "'" + '"'

os.system(dbuser)
os.system("systemctl restart mariadb")

##### DATABASE CONNECTION #####

print ("----- SETTING DATABASE CONNECTION -----")
time.sleep(2)

dbconn = "mv /var/www/" + wpdirname + "/wp-config-sample.php /var/www/" + wpdirname + "/wp-config.php"
dbconn2 = "sed -i 's/votre_nom_de_bdd/" + dbname + "/g' /var/www/" + wpdirname + "/wp-config.php"
dbconn3 = "sed -i 's/votre_utilisateur_de_bdd/" + dbusername + "/g' /var/www/" + wpdirname + "/wp-config.php"
dbconn4 = "sed -i 's/votre_mdp_de_bdd/" + dbpassword + "/g' /var/www/" + wpdirname + "/wp-config.php"

os.system (dbconn)
os.system (dbconn2)
os.system (dbconn3)
os.system (dbconn4)

##### WORDPRESS READY #####

print ("----- WORDPRESS IS READY TO INSTALL ! -----")
time.sleep(2)

print ("----- SERVER IS GOING TO REBOOT -----")
time.sleep(2)

print ("----- WHEN SERVER IS REBOOTED : GO TO http://" + servername + "/ -----")
time.sleep(5)

os.system("systemctl reboot")
