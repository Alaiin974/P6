#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

########## PRÉREQUIS ##########

#apt install python

########## PRÉREQUIS ##########

import os
import time

##### PACKAGES INSTALLATON #####

#print ("## PACKAGES INSTALLATON : APACHE2, MARIADB-SERVER, PHP, WGET ##")
#time.sleep(2)

#os.system('apt install apache2 -y')
#os.system('apt install mariadb-server -y')
#os.system('apt install php7.3 -y')
#os.system('apt install wget -y')

##### LATEST WORDPRESS ARCHIVE #####

#print ("## DOWNLOAD AND UNCOMPRESS LATEST WORDPRESS ARCHIVE ##")
#time.sleep(2)

#os.system('wget https://wordpress.org/latest.tar.gz')
#os.system ('tar xvf latest.tar.gz')

##### WORDPRESS DIRECTORY #####

#print ("## SET WORDPRESS DIRECTORY ##")
#time.sleep(2)

#wpdir = '/var/www/' 
#wpdirname = raw_input ("Wordpress Directory Name ?" )
#wpdirname1 = 'mv wordpress ' + '/var/www/' + wpdirname
#chwpdir = 'chmod -R 755 /var/www/' + wpdirname + ' && chown -R www-data:www-data /var/www/' + wpdirname 

#os.system(wpdirname1)
#os.system(chwpdir)

#print("## Directory is : /var/wwww/" + wpdirname + " width chmod 755 & chown www-data:www-data ##")

##### /VAR/WWW/HTML & APACHE CONF #####

print ("## SET DEFAULT APACHE DIRECTORY ##")
time.sleep(2)

a2dir = ("sed -i 's/html//g' /etc/apache2/sites-enabled/000-default.conf")

os.system(a2dir)
os.system('rm -r /var/www/html')
