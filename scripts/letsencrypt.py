#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import os
import time

##### https://certbot.eff.org/lets-encrypt/debianbuster-apache #####

print ("----- PACKAGES INSTALLATION : SUDO, SNAPD -----")
time.sleep(2)

os.system("apt install sudo snapd")

print ("----- SNAPD LATEST VERSION CHECK -----")
time.sleep(2)

os.system("sudo snap install core; sudo snap refresh core")

print ("----- INSTALL CERTBOT -----")
time.sleep(2)

os.system("sudo snap install --classic certbot")

print ("----- ENABLE CERTBOT COMMAND -----")
time.sleep(2)

os.system("sudo ln -s /snap/bin/certbot /usr/bin/certbot")

print ("----- GENERATE SSL CERTIFICATE -----")
time.sleep(2)

os.system("sudo certbot --apache")

print ("----- ENABLE AUTOMATIC SSL CERTIFICATE RENEWAL -----")
time.sleep(2)

os.system("sudo certbot renew --dry-run")
