# Sample Public School - Django Website

Single-file Django website: public pages, admissions forms, contact form,
gallery, news & events, mandatory disclosure, and an admin panel.

## Setup

    pip install -r requirements.txt

## Run

    python school_site.py                    # migrate, demo data, start server
    python school_site.py createsuperuser    # admin account (one time)

Open:
- Website: http://127.0.0.1:8000/
- Admin:   http://127.0.0.1:8000/admin/

Data is stored in school.sqlite3 and uploads go to media/ (created automatically).
