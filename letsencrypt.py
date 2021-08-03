#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import os

##### https://certbot.eff.org/lets-encrypt/debianbuster-apache #####

print ("----- PACKAGES INSTALLATION : SUDO, SNAPD -----")
os.system("apt install sudo snapd")

print ("----- SNAPD LATEST VERSION CHECK -----")
os.system("sudo snap install core; sudo snap refresh core")

print ("----- INSTALL CERTBOT -----")
os.system("sudo snap install --classic certbot")

print ("----- ENABLE CERTBOT COMMAND -----")
os.system("sudo ln -s /snap/bin/certbot /usr/bin/certbot")

print ("----- GENERATE SSL CERTIFICATE -----")
os.system("sudo certbot --apache")

print ("----- ENABLE AUTOMATIC SSL CERTIFICATE RENEWAL -----")
os.system("sudo certbot renew --dry-run")
