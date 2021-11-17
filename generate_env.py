#!/usr/bin/env python3
#
# Generates new django secret key, and required environment variables
# to enable local builds of website
#
# To use - run python ./generate_env.py
# if .env exists script will error
# if .env.sh exists it will be overwritten
#
# once created, load environment variables into shell with . .env.sh

from django.core.management.utils import get_random_secret_key
import secrets
import string
alphabet = string.ascii_letters + string.digits + "-_"


MARIADB_ROOT_PASSWORD = ''.join(secrets.choice(alphabet) for i in range(32))

secret = get_random_secret_key()
f = open(".env", "x")
f.write("SECRET_KEY=\"" + secret + "\"\n")
f.write("MARIADB_ROOT_PASSWORD=\"" + MARIADB_ROOT_PASSWORD + "\"\n")
f.write("DJANGO_ALLOWED_HOSTS=\"*\"\n")
f.write("DEBUG=\"1\"\n")
f.write("EMAIL_HOST_USER=\"SAMPLE-USERNAME\"\n")
f.write("EMAIL_HOST_PASSWORD=\"SAMPLE-PASSWORD\"\n")


f = open(".env.sh", "w")
f.write("export SECRET_KEY=\"" + secret + "\"\n")
f.write("MARIADB_ROOT_PASSWORD=\"" + MARIADB_ROOT_PASSWORD + "\"\n")
f.write("export DJANGO_ALLOWED_HOSTS=\"*\"\n")
f.write("export DEBUG=\"1\"\n")
f.write("export EMAIL_HOST_USER=\"SAMPLE-USERNAME\"\n")
f.write("export EMAIL_HOST_PASSWORD=\"SAMPLE-PASSWORD\"\n")

f.close()
