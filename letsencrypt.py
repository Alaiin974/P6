#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import os
import time

os.system("apt install sudo snap")
os.system("sudo snap install core; sudo snap refresh core")
os.system("sudo snap install --classic certbot")
os.system("sudo ln -s /snap/bin/certbot /usr/bin/certbot")
os.system("sudo certbot --apache")
os.system("sudo certbot renew --dry-run")