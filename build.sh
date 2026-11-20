#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python school_site.py collectstatic --noinput
python school_site.py migrate
