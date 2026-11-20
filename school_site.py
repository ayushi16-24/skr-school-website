"""
Sample Public School - ek hi file me poori Django website.

Setup (ek baar):
    pip install django pillow

Chalane ke liye:
    python school_site.py                 # migrate + demo data + server start
    python school_site.py createsuperuser # admin user banane ke liye

Phir browser me:
    http://127.0.0.1:8000/      (website)
    http://127.0.0.1:8000/admin/ (admin panel)
"""
import os
import re
import sys
from datetime import date
from pathlib import Path

import django
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Templates (file ke andar hi, locmem loader se load hote hain)
# ---------------------------------------------------------------------------
TEMPLATES = {
    "base.html": """{% load static %}<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{% block title %}{{ school.name }}{% endblock %}</title>
<meta name="description" content="{% block description %}{{ school.tagline }}{% endblock %}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
<style>
:root{--navy:#0b1f4b;--royal:#1e4fd8;--light:#e8f0fe;--gold:#c9a227;--text:#1d2433}
html{scroll-behavior:smooth;scroll-padding-top:90px}
body{font-family:Inter,system-ui,sans-serif;color:var(--text)}
h1,h2,h3,h4,h5{font-family:"Playfair Display",serif;color:var(--navy)}
.topbar{background:var(--light);color:var(--navy);font-size:.9rem;padding:.4rem 0;border:0;margin:0}
.nav-theme{background:var(--navy);border:0;margin:0;box-shadow:none}
.nav-theme .navbar-nav .nav-link{color:#fff;font-weight:500;padding:.6rem .85rem;font-size:.95rem;transition:color .2s}
.nav-theme .navbar-nav .nav-link:hover,.nav-theme .navbar-nav .nav-link.active{color:var(--gold)}
main{margin:0;padding:0;border:0}
.btn-gold{background:var(--gold);color:var(--navy);font-weight:600;border:0}
.btn-gold:hover{background:#b38f1f;color:#fff}
.btn-royal{background:var(--royal);color:#fff;font-weight:600;border:0}
.btn-royal:hover{background:var(--navy);color:#fff}
.hero{position:relative;min-height:80vh;display:flex;align-items:center;background:linear-gradient(135deg,var(--navy),var(--royal));color:#fff;overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.35}
.hero .content{position:relative;padding:5rem 0}
.hero h1{color:#fff}
.page-head{background:var(--light);padding:3rem 0}
.section{padding:4rem 0}
.section-title{font-size:2rem;margin-bottom:.5rem}
.card-soft{background:#fff;border-radius:16px;box-shadow:0 8px 24px rgba(11,31,75,.08);transition:transform .25s,box-shadow .25s;height:100%}
.card-soft:hover{transform:translateY(-4px);box-shadow:0 14px 32px rgba(11,31,75,.15)}
.stat{background:#fff;border-radius:16px;padding:1.4rem;text-align:center;box-shadow:0 8px 24px rgba(11,31,75,.1)}
.stat b{display:block;font-family:"Playfair Display",serif;font-size:2rem;color:var(--royal)}
.icon{font-size:1.7rem;color:var(--royal)}
.gallery-img{width:100%;height:200px;object-fit:cover;border-radius:12px;transition:transform .3s}
.gallery-img:hover{transform:scale(1.03)}
.map{width:100%;height:320px;border:0;border-radius:16px}
.footer{background:var(--navy);color:#cfd8ea}
.footer a{color:#cfd8ea;text-decoration:none}
.footer a:hover{color:var(--gold)}
@media (max-width:768px){.hero{min-height:65vh}}
</style>
</head>
<body>

<div class="topbar">
  <div class="container d-flex flex-wrap justify-content-between gap-2">
    <span><i class="fa-solid fa-phone me-1"></i>{{ school.phone }}</span>
    <span><i class="fa-solid fa-envelope me-1"></i>{{ school.email }}</span>
    <span><i class="fa-regular fa-clock me-1"></i>{{ school.working_hours }}</span>
  </div>
</div>

<nav class="navbar navbar-expand-lg navbar-dark sticky-top nav-theme py-2">
  <div class="container">
    <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-center" id="mainNav">
      <ul class="navbar-nav align-items-lg-center flex-wrap justify-content-center">
        <li class="nav-item"><a class="nav-link" href="{% url 'home' %}">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'about' %}">About</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'academics' %}">Academics</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'infrastructure' %}">Infrastructure</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'admissions' %}">Admissions</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'achievements' %}">Achievements</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'news' %}">News &amp; Events</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'gallery' %}">Gallery</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'disclosure' %}">Disclosure</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'contact' %}">Contact</a></li>
        <li class="nav-item ms-lg-2 my-1"><a class="btn btn-gold btn-sm px-3" href="{% url 'apply' %}">Apply Now</a></li>
      </ul>
    </div>
  </div>
</nav>

<main>
  {% if messages %}
  <div class="container mt-3">
    {% for message in messages %}
      <div class="alert alert-{% if message.tags == 'error' %}danger{% else %}{{ message.tags }}{% endif %} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    {% endfor %}
  </div>
  {% endif %}
  {% block content %}{% endblock %}
</main>

<footer class="footer">
  <div class="container py-5">
    <div class="row g-4">
      <div class="col-md-4">
        <h5 class="text-white">{{ school.name }}</h5>
        <p class="small">{{ school.address }}</p>
        {% if school.affiliation_no %}<p class="small mb-0">CBSE Affiliation No.: {{ school.affiliation_no }}</p>{% endif %}
      </div>
      <div class="col-md-4">
        <h6 class="text-white">Quick Links</h6>
        <ul class="list-unstyled small">
          <li><a href="{% url 'enquiry' %}">Admission Enquiry</a></li>
          <li><a href="{% url 'apply' %}">Online Application</a></li>
          <li><a href="{% url 'disclosure' %}">Mandatory Public Disclosure</a></li>
          <li><a href="{% url 'contact' %}">Contact Us</a></li>
        </ul>
      </div>
      <div class="col-md-4 small">
        <h6 class="text-white">Contact</h6>
        <p class="mb-1"><i class="fa-solid fa-phone me-2"></i>{{ school.phone }}</p>
        <p><i class="fa-solid fa-envelope me-2"></i>{{ school.email }}</p>
      </div>
    </div>
    <hr class="border-secondary">
    <p class="small text-center mb-0">&copy; {% now "Y" %} {{ school.name }}. All rights reserved.</p>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""",

    "pagination.html": """{% if page.has_other_pages %}
<nav class="mt-4">
  <ul class="pagination justify-content-center">
    {% if page.has_previous %}<li class="page-item"><a class="page-link" href="?page={{ page.previous_page_number }}">Previous</a></li>{% endif %}
    <li class="page-item active"><span class="page-link">{{ page.number }} / {{ page.paginator.num_pages }}</span></li>
    {% if page.has_next %}<li class="page-item"><a class="page-link" href="?page={{ page.next_page_number }}">Next</a></li>{% endif %}
  </ul>
</nav>
{% endif %}
""",

    "form_fields.html": """{% if form.non_field_errors %}<div class="alert alert-danger">{{ form.non_field_errors }}</div>{% endif %}
<div class="row g-3">
  {% for field in form %}
    <div class="col-md-6">
      <label class="form-label" for="{{ field.id_for_label }}">{{ field.label }}{% if field.field.required %} <span class="text-danger">*</span>{% endif %}</label>
      {{ field }}
      {% for error in field.errors %}<div class="invalid-feedback d-block">{{ error }}</div>{% endfor %}
      {% if field.help_text %}<div class="form-text">{{ field.help_text }}</div>{% endif %}
    </div>
  {% endfor %}
</div>
""",

    "home.html": """{% extends "base.html" %}
{% block content %}
<section class="hero">
  {% if school.hero_image %}<img src="{{ school.hero_image.url }}" alt="{{ school.name }} campus">{% endif %}
  <div class="container content text-white">
    {% if school.admissions_open %}<span class="badge bg-warning text-dark mb-3">Admissions Open</span>{% endif %}
    <h1 class="display-4 fw-bold">{{ school.name }}</h1>
    <p class="lead">{{ school.tagline }}</p>
    <div class="d-flex flex-wrap gap-2">
      <a href="{% url 'apply' %}" class="btn btn-gold btn-lg">Apply Now</a>
      <a href="#about" class="btn btn-outline-light btn-lg">Explore School</a>
    </div>
  </div>
</section>

<section class="container" style="margin-top:-3rem;position:relative">
  <div class="row g-3">
    <div class="col-6 col-md-3"><div class="stat"><b>{{ school.years_of_excellence }}+ Years</b>Est. 2009 in Jhotwara</div></div>
    <div class="col-6 col-md-3"><div class="stat"><b>Pre-K to 12th</b>Science, Commerce &amp; Arts</div></div>
    <div class="col-6 col-md-3"><div class="stat"><b>92%</b>Parent Recommendation</div></div>
    <div class="col-6 col-md-3"><div class="stat"><b>10m Range</b>Shooting &amp; Sports Academy</div></div>
  </div>
</section>

<section id="about" class="section container">
  <div class="text-center mb-5">
    <h2 class="section-title">About Our School</h2>
    <p class="text-muted mx-auto" style="max-width:760px">{{ school.about_intro }}</p>
    <a href="{% url 'about' %}" class="btn btn-royal">Read more</a>
  </div>
  <div class="row g-4">
    <div class="col-md-6 col-lg-3">
      <div class="card-soft p-4 border-top border-4" style="border-color:var(--navy)!important">
        <i class="fa-solid fa-graduation-cap icon mb-3"></i>
        <h5>Senior Secondary Streams</h5>
        <p class="small text-muted mb-0">Science (PCM/PCB), Commerce, and Arts streams with modern physics, chemistry, biology, and IT laboratories.</p>
      </div>
    </div>
    <div class="col-md-6 col-lg-3">
      <div class="card-soft p-4 border-top border-4" style="border-color:var(--royal)!important">
        <i class="fa-solid fa-shield-halved icon mb-3"></i>
        <h5>Sainik / Military Prep</h5>
        <p class="small text-muted mb-0">Structured discipline, obstacle courses, leadership drills, and specialized entrance coaching for Sainik &amp; military schools.</p>
      </div>
    </div>
    <div class="col-md-6 col-lg-3">
      <div class="card-soft p-4 border-top border-4" style="border-color:var(--gold)!important">
        <i class="fa-solid fa-crosshairs icon mb-3"></i>
        <h5>10m Shooting &amp; Sports</h5>
        <p class="small text-muted mb-0">Dedicated indoor 10-meter air pistol/rifle shooting range, basketball courts, cricket academy, and indoor games.</p>
      </div>
    </div>
    <div class="col-md-6 col-lg-3">
      <div class="card-soft p-4 border-top border-4" style="border-color:var(--royal)!important">
        <i class="fa-solid fa-heart-circle-check icon mb-3"></i>
        <h5>92% Recommended &amp; Affordable</h5>
        <p class="small text-muted mb-0">Peaceful residential location off Kalwar Road, acclaimed for disciplined atmosphere, character building, and affordable fees.</p>
      </div>
    </div>
  </div>
</section>

<section class="section container pt-0">
  <h2 class="section-title text-center mb-4">Academic Programs</h2>
  <div class="row g-4">
    {% for p in programs %}
    <div class="col-md-6 col-lg-3"><div class="card-soft p-4">
      <i class="fa-solid {{ p.icon }} icon mb-3"></i>
      <h5>{{ p.title }}</h5>
      <p class="small text-muted mb-0">{{ p.description }}</p>
    </div></div>
    {% empty %}<p class="text-muted">Academic programs jald add honge.</p>
    {% endfor %}
  </div>
</section>

{% if school.principal_message %}
<section class="section" style="background:var(--light)">
  <div class="container row align-items-center g-4">
    <div class="col-md-8">
      <h2 class="section-title">Principal's Message</h2>
      <p class="lead">{{ school.principal_message|linebreaksbr }}</p>
      <p class="fw-semibold mb-0">{{ school.principal_name }}</p>
    </div>
  </div>
</section>
{% endif %}

<section class="section container">
  <h2 class="section-title text-center mb-4">Infrastructure Highlights</h2>
  <div class="row g-4">
    {% for f in facilities %}
    <div class="col-md-6 col-lg-4"><div class="card-soft p-4">
      <i class="fa-solid {{ f.icon }} icon mb-3"></i>
      <h5>{{ f.title }}</h5>
      <p class="small text-muted mb-0">{{ f.description }}</p>
    </div></div>
    {% endfor %}
  </div>
  <div class="text-center mt-4"><a href="{% url 'infrastructure' %}" class="btn btn-royal">All facilities</a></div>
</section>

<section class="section container pt-0">
  <h2 class="section-title text-center mb-4">Student Achievements</h2>
  <div class="row g-4">
    {% for a in achievements %}
    <div class="col-md-4"><div class="card-soft p-4">
      <span class="badge bg-light text-primary mb-2">{{ a.get_category_display }} · {{ a.year }}</span>
      <h5>{{ a.title }}</h5>
      <p class="small text-muted mb-0">{% if a.student_name %}{{ a.student_name }} — {% endif %}{{ a.description }}</p>
    </div></div>
    {% empty %}<p class="text-muted">Achievements jald add honge.</p>
    {% endfor %}
  </div>
</section>

<section class="section container pt-0">
  <h2 class="section-title text-center mb-4">News &amp; Events</h2>
  <div class="row g-4">
    {% for n in news %}
    <div class="col-md-4"><div class="card-soft p-4">
      <small class="text-muted">{{ n.date|date:"d M Y" }}</small>
      <h5 class="mt-1">{{ n.title }}</h5>
      <p class="small text-muted mb-0">{{ n.body|truncatewords:25 }}</p>
    </div></div>
    {% endfor %}
    {% for e in events %}
    <div class="col-md-4"><div class="card-soft p-4 border-start border-4" style="border-color:var(--gold)!important">
      <small class="text-muted">Upcoming · {{ e.event_date|date:"d M Y" }}</small>
      <h5 class="mt-1">{{ e.title }}</h5>
      <p class="small text-muted mb-0">{{ e.venue }}</p>
    </div></div>
    {% endfor %}
  </div>
  <div class="text-center mt-4"><a href="{% url 'news' %}" class="btn btn-royal">All news &amp; events</a></div>
</section>

<section class="section container pt-0">
  <h2 class="section-title text-center mb-4">Campus Gallery</h2>
  <div class="row g-3">
    {% for g in gallery %}
    <div class="col-6 col-md-4"><a href="{{ g.image.url }}" target="_blank" rel="noopener"><img class="gallery-img" src="{{ g.image.url }}" alt="{{ g.alt_text|default:g.caption }}"></a></div>
    {% empty %}<p class="text-muted">Gallery jald add hogi.</p>
    {% endfor %}
  </div>
  <div class="text-center mt-4"><a href="{% url 'gallery' %}" class="btn btn-royal">Full gallery</a></div>
</section>

<section class="section container pt-0">
  <h2 class="section-title text-center mb-4">What Parents Say</h2>
  <div class="row g-4">
    {% for t in testimonials %}
    <div class="col-md-4"><div class="card-soft p-4">
      <p class="fst-italic">"{{ t.message }}"</p>
      <p class="fw-semibold mb-0">{{ t.author_name }}</p>
      <p class="small text-muted mb-0">{{ t.relation }}</p>
    </div></div>
    {% empty %}<p class="text-muted">Testimonials jald add honge.</p>
    {% endfor %}
  </div>
</section>
{% endblock %}
""",

    "about.html": """{% extends "base.html" %}
{% block title %}About Us | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">About Us</h1><p class="mb-0">{{ school.about_intro }}</p></div></section>
<section class="section container">
  <div class="row g-4">
    <div class="col-md-6"><div class="card-soft p-4 h-auto"><h3 class="h4"><i class="fa-solid fa-landmark icon me-2" style="font-size:1.3rem"></i>History &amp; Establishment</h3><p class="mb-0">{{ school.history|linebreaksbr }}</p></div></div>
    <div class="col-md-6"><div class="card-soft p-4 h-auto"><h3 class="h4"><i class="fa-solid fa-eye icon me-2" style="font-size:1.3rem"></i>Vision</h3><p class="mb-0">{{ school.vision|linebreaksbr }}</p></div></div>
    <div class="col-md-6"><div class="card-soft p-4 h-auto"><h3 class="h4"><i class="fa-solid fa-bullseye icon me-2" style="font-size:1.3rem"></i>Mission</h3><p class="mb-0">{{ school.mission|linebreaksbr }}</p></div></div>
    <div class="col-md-6"><div class="card-soft p-4 h-auto"><h3 class="h4"><i class="fa-solid fa-seedling icon me-2" style="font-size:1.3rem"></i>Philosophy</h3><p class="mb-0">{{ school.philosophy|linebreaksbr }}</p></div></div>
  </div>
</section>
{% if school.principal_message %}
<section class="section" style="background:var(--light)"><div class="container">
  <h2 class="section-title">Principal's Message</h2>
  <p class="lead">{{ school.principal_message|linebreaksbr }}</p>
  <p class="fw-semibold mb-0">{{ school.principal_name }}</p>
</div></section>
{% endif %}
{% endblock %}
""",

    "academics.html": """{% extends "base.html" %}
{% block title %}Academics | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Academics</h1><p class="mb-0">Pre-Primary se Senior Secondary tak ki classes, subjects aur gatividhiyan.</p></div></section>
<section class="section container">
  {% for label, items in groups %}
    <h2 class="section-title mt-4">{{ label }}</h2>
    <div class="row g-4 mb-4">
      {% for p in items %}
      <div class="col-md-6 col-lg-4"><div class="card-soft p-4">
        <i class="fa-solid {{ p.icon }} icon mb-3"></i>
        <h5>{{ p.title }}</h5>
        <p class="small text-muted mb-0">{{ p.description }}</p>
      </div></div>
      {% empty %}<p class="text-muted">Jald add hoga.</p>
      {% endfor %}
    </div>
  {% endfor %}
</section>
{% endblock %}
""",

    "infrastructure.html": """{% extends "base.html" %}
{% block title %}Infrastructure | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Infrastructure</h1><p class="mb-0">Smart classrooms, labs, library, sports aur suraksha.</p></div></section>
<section class="section container">
  <div class="row g-4">
    {% for f in facilities %}
    <div class="col-md-6 col-lg-4"><div class="card-soft p-4">
      <i class="fa-solid {{ f.icon }} icon mb-3"></i>
      <h5>{{ f.title }}</h5>
      <p class="small text-muted mb-0">{{ f.description }}</p>
    </div></div>
    {% empty %}<p class="text-muted">Facilities ki jaankari jald add hogi.</p>
    {% endfor %}
  </div>
</section>
{% endblock %}
""",

    "admissions.html": """{% extends "base.html" %}
{% block title %}Admissions | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container">
  <h1 class="section-title">Admissions</h1>
  {% if school.admissions_open %}<span class="badge bg-warning text-dark mb-2">Admissions Open</span>{% endif %}
  <p class="mb-3">Apne bachche ke liye admission ki prakriya, patrata aur zaruri documents yahan dekhein.</p>
  <a href="{% url 'enquiry' %}" class="btn btn-royal me-2">Admission Enquiry</a>
  <a href="{% url 'apply' %}" class="btn btn-gold">Apply Online</a>
</div></section>
<section class="section container">
  <div class="row g-4">
    <div class="col-md-4"><div class="card-soft p-4 h-auto"><h3 class="h5">Admission Procedure</h3><p class="mb-0">{{ school.admission_procedure|linebreaksbr }}</p></div></div>
    <div class="col-md-4"><div class="card-soft p-4 h-auto"><h3 class="h5">Eligibility Criteria</h3><p class="mb-0">{{ school.eligibility|linebreaksbr }}</p></div></div>
    <div class="col-md-4"><div class="card-soft p-4 h-auto"><h3 class="h5">Required Documents</h3><p class="mb-0">{{ school.documents_required|linebreaksbr }}</p></div></div>
  </div>
</section>
{% endblock %}
""",

    "form_page.html": """{% extends "base.html" %}
{% block title %}{{ title }} | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container">
  <h1 class="section-title">{{ title }}</h1>
  <p class="mb-0">{{ intro }}</p>
</div></section>
<section class="section container">
  <div class="row justify-content-center"><div class="col-lg-8">
    <div class="card-soft p-4 p-md-5 h-auto">
      <form method="post" enctype="multipart/form-data" novalidate>
        {% csrf_token %}
        {% include "form_fields.html" %}
        <button type="submit" class="btn btn-royal btn-lg mt-4">{{ submit_label }}</button>
      </form>
    </div>
  </div></div>
</section>
{% endblock %}
""",

    "confirmation.html": """{% extends "base.html" %}
{% block title %}Application Submitted | {{ school.name }}{% endblock %}
{% block content %}
<section class="section container">
  <div class="row justify-content-center"><div class="col-lg-7">
    <div class="card-soft p-5 text-center h-auto">
      <i class="fa-solid fa-circle-check text-success" style="font-size:3.5rem"></i>
      <h1 class="section-title mt-3">Application Submitted</h1>
      <p>Aapki application mil gayi hai. Yeh reference number surakshit rakhein:</p>
      <p class="fs-3 fw-bold" style="color:var(--royal);letter-spacing:2px">{{ application.reference }}</p>
      <p class="small text-muted">Student: {{ application.student_name }} · Class: {{ application.class_applying }} · Status: {{ application.get_status_display }}</p>
      <a href="{% url 'home' %}" class="btn btn-royal mt-3">Back to Home</a>
    </div>
  </div></div>
</section>
{% endblock %}
""",

    "achievements.html": """{% extends "base.html" %}
{% block title %}Achievements | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Achievements</h1><p class="mb-0">Academic, CBSE board, sports, awards aur competitions.</p></div></section>
<section class="section container">
  <div class="mb-4 d-flex flex-wrap gap-2">
    <a href="?" class="btn btn-sm {% if not current %}btn-royal{% else %}btn-outline-primary{% endif %}">All</a>
    {% for key, label in categories %}
      <a href="?cat={{ key }}" class="btn btn-sm {% if current == key %}btn-royal{% else %}btn-outline-primary{% endif %}">{{ label }}</a>
    {% endfor %}
  </div>
  <div class="row g-4">
    {% for a in page.object_list %}
    <div class="col-md-6 col-lg-4"><div class="card-soft p-4">
      <span class="badge bg-light text-primary mb-2">{{ a.get_category_display }} · {{ a.year }}</span>
      <h5>{{ a.title }}</h5>
      <p class="small text-muted mb-0">{% if a.student_name %}{{ a.student_name }} — {% endif %}{{ a.description }}</p>
    </div></div>
    {% empty %}<p class="text-muted">Is category me abhi koi achievement nahi hai.</p>
    {% endfor %}
  </div>
  {% include "pagination.html" %}
</section>
{% endblock %}
""",

    "news.html": """{% extends "base.html" %}
{% block title %}News & Events | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">News &amp; Events</h1><p class="mb-0">Latest school news aur aane wale events.</p></div></section>
<section class="section container">
  <div class="row g-4">
    <div class="col-lg-8">
      <div class="row g-4">
        {% for item in page.object_list %}
        <div class="col-md-6"><article class="card-soft overflow-hidden">
          {% if item.image %}<img src="{{ item.image.url }}" alt="{{ item.title }}" style="width:100%;height:200px;object-fit:cover">{% endif %}
          <div class="p-4">
            <span class="badge bg-light text-primary mb-2">{{ item.get_kind_display }} · {{ item.date|date:"d M Y" }}</span>
            <h3 class="h5">{{ item.title }}</h3>
            <p class="small text-muted mb-0">{{ item.body|truncatewords:30 }}</p>
          </div>
        </article></div>
        {% empty %}<p class="text-muted">Abhi koi news nahi hai.</p>
        {% endfor %}
      </div>
      {% include "pagination.html" %}
    </div>
    <aside class="col-lg-4">
      <div class="card-soft p-4 h-auto">
        <h3 class="h5">Upcoming Events</h3>
        {% for e in upcoming %}
          <div class="mb-3"><strong>{{ e.event_date|date:"d M Y" }}</strong><br>{{ e.title }}{% if e.venue %} · {{ e.venue }}{% endif %}</div>
        {% empty %}<p class="small text-muted">Koi upcoming event nahi hai.</p>
        {% endfor %}
      </div>
    </aside>
  </div>
</section>
{% endblock %}
""",

    "gallery.html": """{% extends "base.html" %}
{% block title %}Gallery | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Gallery</h1><p class="mb-0">Events aur campus ki jhalkiyan.</p></div></section>
<section class="section container">
  <div class="mb-4 d-flex flex-wrap gap-2">
    <a href="?" class="btn btn-sm {% if not current %}btn-royal{% else %}btn-outline-primary{% endif %}">All</a>
    {% for key, label in categories %}
      <a href="?cat={{ key }}" class="btn btn-sm {% if current == key %}btn-royal{% else %}btn-outline-primary{% endif %}">{{ label }}</a>
    {% endfor %}
  </div>
  <div class="row g-3">
    {% for g in page.object_list %}
    <div class="col-6 col-md-4 col-lg-3">
      <a href="{{ g.image.url }}" target="_blank" rel="noopener" title="{{ g.caption }}">
        <img class="gallery-img" src="{{ g.image.url }}" alt="{{ g.alt_text|default:g.caption }}">
      </a>
    </div>
    {% empty %}<p class="text-muted">Is category me abhi photos nahi hain.</p>
    {% endfor %}
  </div>
  {% include "pagination.html" %}
</section>
{% endblock %}
""",

    "disclosure.html": """{% extends "base.html" %}
{% block title %}Mandatory Public Disclosure | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Mandatory Public Disclosure</h1><p class="mb-0">CBSE affiliation, recognition, infrastructure, results, fee structure aur committee ke documents.</p></div></section>
<section class="section container">
  {% for label, docs in groups %}
    {% if docs %}
    <h2 class="h4 mt-4">{{ label }}</h2>
    <ul class="list-group mb-4">
      {% for d in docs %}
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <span>{{ d.title }} <small class="text-muted">({{ d.published_on|date:"d M Y" }})</small></span>
        <a href="{{ d.file.url }}" target="_blank" rel="noopener" class="btn btn-sm btn-royal">PDF</a>
      </li>
      {% endfor %}
    </ul>
    {% endif %}
  {% empty %}<p class="text-muted">Documents jald upload honge.</p>
  {% endfor %}
</section>
{% endblock %}
""",

    "contact.html": """{% extends "base.html" %}
{% block title %}Contact Us | {{ school.name }}{% endblock %}
{% block content %}
<section class="page-head"><div class="container"><h1 class="section-title">Contact Us</h1><p class="mb-0">Koi sawal ho to message bhejiye. Hum jaldi sampark karenge.</p></div></section>
<section class="section container">
  <div class="row g-4">
    <div class="col-lg-7">
      <div class="card-soft p-4 p-md-5 h-auto">
        <form method="post" novalidate>
          {% csrf_token %}
          {% include "form_fields.html" %}
          <button type="submit" class="btn btn-royal btn-lg mt-4">Send message</button>
        </form>
      </div>
    </div>
    <div class="col-lg-5">
      <div class="card-soft p-4 h-auto mb-4">
        <h3 class="h5">School Address</h3>
        <p><i class="fa-solid fa-location-dot me-2"></i>{{ school.address }}</p>
        <p><i class="fa-solid fa-phone me-2"></i>{{ school.phone }}</p>
        <p><i class="fa-solid fa-envelope me-2"></i>{{ school.email }}</p>
        <p class="mb-0"><i class="fa-regular fa-clock me-2"></i>{{ school.working_hours }}</p>
      </div>
      {% if school.map_embed_url %}
      <iframe class="map" src="{{ school.map_embed_url }}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="School location on Google Maps"></iframe>
      {% endif %}
    </div>
  </div>
</section>
{% endblock %}
""",
}

# ---------------------------------------------------------------------------
# Django settings (single-file mode)
# ---------------------------------------------------------------------------
if not hasattr(sys.modules["__main__"], "__file__"):
    sys.modules["__main__"].__file__ = str(BASE_DIR / "school_site.py")

import importlib.util
from django.apps import AppConfig

class SchoolSiteConfig(AppConfig):
    name = __name__
    label = "__main__"
    path = str(BASE_DIR)

sys.modules[__name__].SchoolSiteConfig = SchoolSiteConfig

DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in ("true", "1", "yes")
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-change-me")
ALLOWED_HOSTS = [h.strip() for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,*").split(",") if h.strip()]
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()]

if os.environ.get("RENDER"):
    if "https://*.onrender.com" not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append("https://*.onrender.com")
    render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if render_host:
        if render_host not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(render_host)
        origin = f"https://{render_host}"
        if origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)

has_whitenoise = bool(importlib.util.find_spec("whitenoise"))

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    CSRF_TRUSTED_ORIGINS=CSRF_TRUSTED_ORIGINS,
    SESSION_COOKIE_SECURE=not DEBUG,
    CSRF_COOKIE_SECURE=not DEBUG,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        *(["whitenoise.runserver_nostatic"] if has_whitenoise else []),
        "django.contrib.staticfiles",
        f"{__name__}.SchoolSiteConfig",
    ],
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        *(["whitenoise.middleware.WhiteNoiseMiddleware"] if has_whitenoise else []),
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "loaders": [
                ("django.template.loaders.locmem.Loader", TEMPLATES),
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "school.sqlite3"}},
    LANGUAGE_CODE="en-in",
    TIME_ZONE="Asia/Kolkata",
    USE_TZ=True,
    STATIC_URL="/static/",
    STATIC_ROOT=BASE_DIR / "staticfiles",
    MEDIA_URL="/media/",
    MEDIA_ROOT=BASE_DIR / "media",
    DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
)
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# ---------------------------------------------------------------------------
# Ab Django ready hai: baaki imports
# ---------------------------------------------------------------------------
from django import forms  # noqa: E402
from django.conf.urls.static import static  # noqa: E402
from django.contrib import admin, messages  # noqa: E402
from django.core.exceptions import ValidationError  # noqa: E402
from django.core.management import call_command, execute_from_command_line  # noqa: E402
from django.core.paginator import Paginator  # noqa: E402
from django.db import models  # noqa: E402
from django.http import HttpResponse  # noqa: E402
from django.shortcuts import get_object_or_404, redirect, render  # noqa: E402
from django.urls import path, reverse  # noqa: E402


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------
def validate_phone(value):
    if not re.fullmatch(r"[6-9]\d{9}", value or ""):
        raise ValidationError("Valid 10-digit Indian mobile number daalein.")


def validate_upload(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in (".pdf", ".jpg", ".jpeg", ".png"):
        raise ValidationError("Sirf PDF, JPG ya PNG files allowed hain.")
    if file.size > 2 * 1024 * 1024:
        raise ValidationError("File 2 MB se badi nahi honi chahiye.")


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = "__main__"


class SchoolInfo(BaseModel):
    """Singleton (pk=1). Site ka saara editable content yahin hai."""

    name = models.CharField(max_length=200, default="Sample Public School")
    tagline = models.CharField(max_length=255, blank=True)
    affiliation_no = models.CharField("CBSE affiliation no.", max_length=50, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    working_hours = models.CharField(max_length=200, blank=True)
    map_embed_url = models.URLField("Google Maps embed URL", blank=True)
    logo = models.ImageField(upload_to="site/", blank=True)
    hero_image = models.ImageField(upload_to="site/", blank=True)
    admissions_open = models.BooleanField(default=True)

    about_intro = models.TextField(blank=True)
    history = models.TextField("History & establishment", blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    philosophy = models.TextField(blank=True)

    principal_name = models.CharField(max_length=120, blank=True)
    principal_message = models.TextField(blank=True)

    admission_procedure = models.TextField(blank=True)
    eligibility = models.TextField(blank=True)
    documents_required = models.TextField(blank=True)

    students_count = models.PositiveIntegerField(default=0)
    teachers_count = models.PositiveIntegerField(default=0)
    years_of_excellence = models.PositiveIntegerField(default=0)
    board_pass_pct = models.DecimalField("Board pass %", max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = "School information"
        verbose_name_plural = "School information"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        return cls.objects.get_or_create(pk=1)[0]

    def __str__(self):
        return self.name


class Program(BaseModel):
    class Level(models.TextChoices):
        PRE_PRIMARY = "pre-primary", "Pre-Primary"
        PRIMARY = "primary", "Primary"
        MIDDLE = "middle", "Middle School"
        SECONDARY = "secondary", "Secondary"
        SENIOR = "senior", "Senior Secondary"

    title = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=Level.choices)
    description = models.TextField("Classes, subjects & methodology")
    icon = models.CharField("Font Awesome class", max_length=50, default="fa-book-open")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Facility(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField("Font Awesome class", max_length=50, default="fa-building")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.title


class Achievement(BaseModel):
    class Category(models.TextChoices):
        ACADEMIC = "academic", "Academic"
        BOARD = "board", "CBSE Board Result"
        SPORTS = "sports", "Sports"
        AWARD = "award", "Student Award"
        COMPETITION = "competition", "Competition"

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=Category.choices)
    student_name = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(default=date.today().year)

    class Meta:
        ordering = ["-year", "-id"]

    def __str__(self):
        return self.title


class NewsEvent(BaseModel):
    class Kind(models.TextChoices):
        NEWS = "news", "News"
        EVENT = "event", "Event"

    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.NEWS)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField("Published on", default=date.today)
    event_date = models.DateField("Event date", null=True, blank=True)
    venue = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="news/", blank=True)

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "News / Event"

    def __str__(self):
        return self.title


class GalleryImage(BaseModel):
    class Category(models.TextChoices):
        EVENTS = "events", "Events"
        SPORTS = "sports", "Sports"
        CLASSROOMS = "classrooms", "Classrooms"
        CULTURAL = "cultural", "Cultural"
        CAMPUS = "campus", "Campus"

    category = models.CharField(max_length=20, choices=Category.choices)
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField("Alt text (SEO)", max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.caption or f"Image {self.pk}"


class Testimonial(BaseModel):
    author_name = models.CharField(max_length=120)
    relation = models.CharField("Relation / role", max_length=120, blank=True)
    message = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.author_name


class Disclosure(BaseModel):
    class Category(models.TextChoices):
        AFFILIATION = "affiliation", "CBSE Affiliation"
        RECOGNITION = "recognition", "School Recognition"
        INFRASTRUCTURE = "infrastructure", "Infrastructure"
        RESULTS = "results", "Academic Results"
        FEES = "fees", "Fee Structure"
        COMMITTEE = "committee", "School Management Committee"
        OTHER = "other", "Other Mandatory Documents"

    category = models.CharField(max_length=20, choices=Category.choices)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="disclosures/", validators=[validate_upload])
    published_on = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title


CLASS_CHOICES = [("Nursery", "Nursery"), ("LKG", "LKG"), ("UKG", "UKG")] + [
    (f"Class {n}", f"Class {n}") for n in range(1, 13)
]
# Approximate minimum age (saal). Exact cut-off rule baad me refine ho sakta hai.
MIN_AGE = {"Nursery": 3, "LKG": 4, "UKG": 5, **{f"Class {n}": 5 + n for n in range(1, 13)}}


def new_reference():
    return "APP" + os.urandom(4).hex().upper()


class AdmissionEnquiry(BaseModel):
    parent_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=10, validators=[validate_phone])
    email = models.EmailField(blank=True)
    student_name = models.CharField(max_length=120, blank=True)
    class_interested = models.CharField(max_length=20, choices=CLASS_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.parent_name} - {self.class_interested}"


class AdmissionApplication(BaseModel):
    class Status(models.TextChoices):
        RECEIVED = "received", "Received"
        UNDER_REVIEW = "under-review", "Under Review"
        SHORTLISTED = "shortlisted", "Shortlisted"
        ADMITTED = "admitted", "Admitted"
        REJECTED = "rejected", "Rejected"

    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHER = "other", "Other"

    reference = models.CharField(max_length=20, unique=True, default=new_reference, editable=False)
    student_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    class_applying = models.CharField(max_length=20, choices=CLASS_CHOICES)
    father_name = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=10, validators=[validate_phone])
    email = models.EmailField()
    address = models.TextField()
    previous_school = models.CharField(max_length=200, blank=True)
    birth_certificate = models.FileField(upload_to="applications/%Y/%m/", validators=[validate_upload])
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.RECEIVED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.reference} - {self.student_name}"


class ContactMessage(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, validators=[validate_phone])
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


from django.apps import apps
if apps.is_installed("__main__"):
    apps.get_app_config("__main__").models_module = sys.modules[__name__]


# ---------------------------------------------------------------------------
# Forms (saari validation yahin)
# ---------------------------------------------------------------------------
class StyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            widget.attrs["class"] = "form-select" if isinstance(widget, forms.Select) else "form-control"
            if isinstance(widget, forms.Textarea):
                widget.attrs["rows"] = 4


class EnquiryForm(StyledForm):
    class Meta:
        model = AdmissionEnquiry
        fields = ["parent_name", "phone", "email", "student_name", "class_interested", "message"]


class ApplicationForm(StyledForm):
    class Meta:
        model = AdmissionApplication
        fields = [
            "student_name", "date_of_birth", "gender", "class_applying",
            "father_name", "mother_name", "phone", "email", "address",
            "previous_school", "birth_certificate",
        ]
        widgets = {"date_of_birth": forms.DateInput(attrs={"type": "date"})}
        help_texts = {"birth_certificate": "PDF/JPG/PNG, max 2 MB"}

    def clean(self):
        cleaned = super().clean()
        dob = cleaned.get("date_of_birth")
        cls = cleaned.get("class_applying")
        if dob:
            if dob > date.today():
                self.add_error("date_of_birth", "Date of birth future mein nahi ho sakti.")
            elif cls in MIN_AGE:
                age = (date.today() - dob).days // 365
                if age < MIN_AGE[cls]:
                    self.add_error("date_of_birth", f"{cls} ke liye kam se kam {MIN_AGE[cls]} saal ki umar chahiye.")
        return cleaned


class ContactForm(StyledForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------
def ctx(**extra):
    return {"school": SchoolInfo.load(), **extra}


def home(request):
    return render(request, "home.html", ctx(
        programs=Program.objects.all()[:8],
        facilities=Facility.objects.all()[:8],
        achievements=Achievement.objects.all()[:6],
        news=NewsEvent.objects.filter(kind=NewsEvent.Kind.NEWS)[:3],
        events=NewsEvent.objects.filter(kind=NewsEvent.Kind.EVENT, event_date__gte=date.today())[:3],
        gallery=GalleryImage.objects.all()[:6],
        testimonials=Testimonial.objects.all()[:6],
    ))


def about(request):
    return render(request, "about.html", ctx())


def academics(request):
    programs = list(Program.objects.all())
    groups = [(label, [p for p in programs if p.level == key]) for key, label in Program.Level.choices if any(p.level == key for p in programs)]
    return render(request, "academics.html", ctx(groups=groups))


def infrastructure(request):
    return render(request, "infrastructure.html", ctx(facilities=Facility.objects.all()))


def admissions(request):
    return render(request, "admissions.html", ctx())


def enquiry(request):
    form = EnquiryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Aapki enquiry save ho gayi hai. Admission team aapse sampark karegi.")
        return redirect("enquiry")
    return render(request, "form_page.html", ctx(
        form=form,
        title="Admission Enquiry",
        intro="Apne bachche ke admission ke baare me jaankari ke liye form bhariye.",
        submit_label="Send enquiry",
    ))


def apply(request):
    form = ApplicationForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        application = form.save()
        return redirect("confirmation", ref=application.reference)
    return render(request, "form_page.html", ctx(
        form=form,
        title="Online Admission Application",
        intro="Sabhi details dhyan se bhariye. Birth certificate PDF/JPG/PNG (max 2 MB) me upload karein.",
        submit_label="Submit application",
    ))


def confirmation(request, ref):
    application = get_object_or_404(AdmissionApplication, reference=ref)
    return render(request, "confirmation.html", ctx(application=application))


def achievements(request):
    cat = request.GET.get("cat", "")
    qs = Achievement.objects.all()
    if cat:
        qs = qs.filter(category=cat)
    page = Paginator(qs, 12).get_page(request.GET.get("page"))
    return render(request, "achievements.html", ctx(
        page=page, categories=Achievement.Category.choices, current=cat))


def news(request):
    page = Paginator(NewsEvent.objects.all(), 9).get_page(request.GET.get("page"))
    upcoming = NewsEvent.objects.filter(kind=NewsEvent.Kind.EVENT, event_date__gte=date.today())[:6]
    return render(request, "news.html", ctx(page=page, upcoming=upcoming))


def gallery(request):
    cat = request.GET.get("cat", "")
    qs = GalleryImage.objects.all()
    if cat:
        qs = qs.filter(category=cat)
    page = Paginator(qs, 12).get_page(request.GET.get("page"))
    return render(request, "gallery.html", ctx(
        page=page, categories=GalleryImage.Category.choices, current=cat))


def disclosure(request):
    groups = [
        (label, Disclosure.objects.filter(category=key, is_public=True))
        for key, label in Disclosure.Category.choices
    ]
    return render(request, "disclosure.html", ctx(groups=groups))


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Aapka message mil gaya hai. Hum jaldi contact karenge.")
        return redirect("contact")
    return render(request, "contact.html", ctx(form=form))


def sitemap_xml(request):
    names = ["home", "about", "academics", "infrastructure", "admissions", "enquiry",
             "apply", "achievements", "news", "gallery", "disclosure", "contact"]
    base = request.build_absolute_uri("/").rstrip("/")
    urls = "".join(f"<url><loc>{base}{reverse(n)}</loc></url>" for n in names)
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
    return HttpResponse(xml, content_type="application/xml")


def robots_txt(request):
    text = f"User-agent: *\nDisallow: /admin/\nSitemap: {request.build_absolute_uri('/sitemap.xml')}\n"
    return HttpResponse(text, content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("academics/", academics, name="academics"),
    path("infrastructure/", infrastructure, name="infrastructure"),
    path("admissions/", admissions, name="admissions"),
    path("admissions/enquiry/", enquiry, name="enquiry"),
    path("admissions/apply/", apply, name="apply"),
    path("admissions/confirmation/<str:ref>/", confirmation, name="confirmation"),
    path("achievements/", achievements, name="achievements"),
    path("news-events/", news, name="news"),
    path("gallery/", gallery, name="gallery"),
    path("disclosure/", disclosure, name="disclosure"),
    path("contact/", contact, name="contact"),
    path("sitemap.xml", sitemap_xml, name="sitemap"),
    path("robots.txt", robots_txt, name="robots"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    from django.views.static import serve
    urlpatterns += [
        path(f"{settings.MEDIA_URL.lstrip('/')}<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
    ]


# ---------------------------------------------------------------------------
# Admin panel
# ---------------------------------------------------------------------------
admin.site.site_header = "School Administration"
admin.site.site_title = "School Admin"


@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SchoolInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "order"]
    list_editable = ["order"]
    list_filter = ["level"]
    search_fields = ["title", "description"]


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    list_editable = ["order"]
    search_fields = ["title", "description"]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "student_name", "year"]
    list_filter = ["category", "year"]
    search_fields = ["title", "student_name", "description"]


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ["title", "kind", "date", "event_date", "venue"]
    list_filter = ["kind", "date"]
    search_fields = ["title", "body", "venue"]
    date_hierarchy = "date"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "category", "created_at"]
    list_filter = ["category"]
    search_fields = ["caption", "alt_text"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["author_name", "relation", "order"]
    list_editable = ["order"]
    search_fields = ["author_name", "message"]


@admin.register(Disclosure)
class DisclosureAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "published_on", "is_public"]
    list_editable = ["is_public"]
    list_filter = ["category", "is_public"]
    search_fields = ["title"]


@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ["parent_name", "phone", "class_interested", "created_at"]
    list_filter = ["class_interested", "created_at"]
    search_fields = ["parent_name", "phone", "student_name", "email"]
    date_hierarchy = "created_at"
    list_per_page = 25


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ["reference", "student_name", "class_applying", "phone", "status", "created_at"]
    list_editable = ["status"]
    list_filter = ["status", "class_applying", "gender"]
    search_fields = ["reference", "student_name", "father_name", "phone", "email"]
    readonly_fields = ["reference", "created_at"]
    date_hierarchy = "created_at"
    list_per_page = 25


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "email", "is_read", "created_at"]
    list_editable = ["is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "subject", "message"]
    date_hierarchy = "created_at"
    list_per_page = 25


# ---------------------------------------------------------------------------
# Demo data (sirf pehli baar, agar database khali ho)
# ---------------------------------------------------------------------------
def seed_demo():
    if Program.objects.exists():
        return
    SchoolInfo.objects.update_or_create(
        pk=1,
        defaults=dict(
            name="Shri Kalyan Radhey Academy (SKR School)",
            tagline="Co-educational Senior Secondary School | Jhotwara, Jaipur (Est. 2009) — Character, Discipline & Sports Excellence",
            affiliation_no="RJ-JPR-2009-XXXX",
            address="Off Kalwar Road, Jhotwara, Jaipur, Rajasthan 302012",
            phone="0141-2345678 / +91 9414000000",
            email="info@skracademy.edu.in",
            working_hours="Mon - Sat: 7:30 AM - 2:30 PM (Sports Academy: 3:00 PM - 6:00 PM)",
            about_intro="Shri Kalyan Radhey Academy (also known as SKR School or Shri Kalyan Radhey Sr. Sec. School) is a premier co-educational senior secondary school in Jhotwara, Jaipur, established around 2009. We offer comprehensive classes from Pre-Primary/Nursery through Class 12 across Science, Commerce, and Arts streams with a strong emphasis on character building, strict discipline, activity-based learning, specialized Sainik/military school preparation, and elite sports academies.",
            history="Established around 2009 in a quiet residential area off Kalwar Road, Jhotwara, Jaipur, Shri Kalyan Radhey Academy has grown into a distinguished institution over 17 years of educational excellence. Renowned for its disciplined environment, high academic standards, professional sports training (including a 10-meter shooting range), and very affordable fee structure, SKR School holds a 92% recommendation rate among parents.",
            vision="To empower every student through holistic education, robust character building, and academic excellence, preparing future leaders for national service, defence, sports, and diverse professional careers.",
            mission="1. Academic Rigor: Deliver exceptional education across Science, Commerce, and Arts with activity-based learning.\n2. Discipline & Values: Emphasize character building, leadership, and specialized Sainik/military training.\n3. Sports Academy: Provide professional coaching in 10-meter air pistol/rifle shooting, basketball, and cricket.\n4. Affordability: Maintain transparent and affordable fees in a peaceful residential setting off Kalwar Road.",
            philosophy="Education is the foundation of character. We blend academic diligence with activity-based learning, physical fitness, marksmanship, and patriotic discipline.",
            principal_name="Principal & Academic Director",
            principal_message="Welcome to Shri Kalyan Radhey Academy (SKR School), Jhotwara, Jaipur.\n\nSince our inception in 2009, we have dedicated ourselves to providing a disciplined, nurturing, and high-achieving environment where children develop character and competence. From foundational pre-primary schooling to Class 12 Science, Commerce, and Arts, alongside our dedicated 10-meter shooting range, basketball and cricket academies, and Sainik school entrance coaching, we prepare students for excellence in board exams, defence services, and higher education.\n\nWith a 92% parent recommendation rate, we remain committed to keeping world-class holistic education genuinely affordable.",
            admission_procedure="1. Enquiry: Fill out the online admission enquiry form or visit our campus off Kalwar Road, Jhotwara, Jaipur.\n2. Application: Submit the application form with required documents (birth certificate, marksheet, photos).\n3. Interaction & Assessment: Age-appropriate assessment and stream counselling (Science / Commerce / Arts).\n4. Special Wings Enrollment: Optional enrollment in Sainik/Military school coaching or Sports Academy (Shooting / Basketball / Cricket).\n5. Confirmation: Complete admission with our affordable and transparent fee schedule.",
            eligibility="• Pre-Primary: Nursery (3+ years), LKG (4+ years), UKG (5+ years)\n• Primary & Middle (Classes 1-8): Age-appropriate eligibility with transfer certificate from recognized school\n• Senior Secondary (Classes 11 & 12):\n  - Science Stream: Physics, Chemistry, Mathematics / Biology\n  - Commerce Stream: Accountancy, Business Studies, Economics, Applied Maths/IP\n  - Arts Stream: History, Political Science, Geography, Economics, Literature\n• Sainik School / Defence Preparation Batch: Open to students from Class 4 onwards.",
            documents_required="1. Student Birth Certificate\n2. Transfer Certificate (TC) from previous school\n3. Previous year progress report / marksheet\n4. Passport-size photographs (Student & Parents)\n5. Aadhaar Card copies\n6. Jaipur residential address proof",
            students_count=1500,
            teachers_count=65,
            years_of_excellence=17,
            board_pass_pct=98.60,
        ),
    )
    Program.objects.bulk_create([
        Program(title="Pre-Primary & Nursery Foundation", level="pre-primary", icon="fa-shapes", order=1,
                description="Nursery, LKG, and UKG programs focusing on activity-based learning, sensory exploration, language development, and foundational numeracy in a caring environment."),
        Program(title="Primary School (Classes 1 - 5)", level="primary", icon="fa-pencil", order=2,
                description="Comprehensive foundation in Hindi, English, Mathematics, Environmental Studies (EVS), and Computer literacy, enriched with moral values, physical education, and arts."),
        Program(title="Middle School (Classes 6 - 8)", level="middle", icon="fa-flask", order=3,
                description="Deep conceptual understanding of Sciences, Mathematics, Social Studies, and Information Technology with strong emphasis on discipline and analytical thinking."),
        Program(title="Secondary School (Classes 9 - 10)", level="secondary", icon="fa-graduation-cap", order=4,
                description="Thorough preparation for CBSE Secondary School Examination with intensive focus on Science, Mathematics, Social Sciences, Hindi, and English."),
        Program(title="Senior Secondary — Science Stream (PCM / PCB)", level="senior", icon="fa-atom", order=5,
                description="Rigorous curriculum in Physics, Chemistry, Mathematics, Biology, and Computer Science. Practical lab sessions and competitive foundation for JEE, NEET, and NDA."),
        Program(title="Senior Secondary — Commerce Stream", level="senior", icon="fa-chart-line", order=6,
                description="Accountancy, Business Studies, Economics, and Applied Mathematics / IP, preparing students for CA Foundation, CUET, financial management, and business careers."),
        Program(title="Senior Secondary — Arts & Humanities Stream", level="senior", icon="fa-book-open-reader", order=7,
                description="In-depth study of History, Political Science, Geography, Economics, and Literature, tailored for Civil Services (UPSC), law, journalism, and academic excellence."),
        Program(title="Sainik & Military School Preparation Wing", level="middle", icon="fa-shield-halved", order=8,
                description="Specialized preparation wing emphasizing character building, strict discipline, physical fitness, obstacle drills, and entrance exam training for Sainik Schools, RIMC, and defence careers."),
    ])
    Facility.objects.bulk_create([
        Facility(title="10-Meter Shooting Range & Academy", icon="fa-crosshairs", order=1,
                 description="Dedicated indoor 10-meter shooting academy with certified targets, air pistols, and precision air rifles coached by expert marksmen for state & national competitions."),
        Facility(title="Sports Academy (Basketball & Cricket)", icon="fa-basketball", order=2,
                 description="Professional sports training programs in basketball, cricket with practice net pitches, track athletics, and coaching for indoor and outdoor games."),
        Facility(title="Advanced Science Laboratories", icon="fa-flask-vial", order=3,
                 description="Modern, fully-equipped separate practical laboratories for Physics, Chemistry, and Biology to foster hands-on experiential scientific inquiry."),
        Facility(title="Computer & Digital Learning Lab", icon="fa-desktop", order=4,
                 description="High-tech computer lab with high-speed internet, modern workstations, programming curriculum, and digital literacy instruction."),
        Facility(title="Library & Reading Hall", icon="fa-book", order=5,
                 description="Extensive collection of textbooks, competitive exam guides (Sainik School, NDA, Olympiads), periodicals, reference materials, and quiet reading zones."),
        Facility(title="Safe Transport Network", icon="fa-bus", order=6,
                 description="GPS-monitored bus and van transport routes covering Kalwar Road, Jhotwara, Hathoj, Niwaru, and surrounding residential colonies of Jaipur with safety staff."),
        Facility(title="Cultural Arts & Student Clubs", icon="fa-masks-theater", order=7,
                 description="Dedicated spaces and auditoriums for cultural programs, Indian & Western music, classical dance, theatre drama, and diverse student hobby clubs."),
    ])
    Achievement.objects.bulk_create([
        Achievement(title="92% Parent Recommendation Rating", category="award", year=date.today().year,
                    description="Holds a 92% recommendation across parent reviews in Jaipur for its disciplined setting, caring faculty, and affordable fee structure.", student_name="Parent Reviews & Community Feedback"),
        Achievement(title="10-Meter Shooting Academy Accolades", category="sports", year=date.today().year,
                    description="Multiple Gold and Silver medals in Rajasthan State and District 10-meter Air Pistol & Air Rifle shooting championships.", student_name="SKR Shooting Academy Team"),
        Achievement(title="Sainik School Entrance Selections", category="competition", year=date.today().year,
                    description="Multiple student selections in All India Sainik Schools Entrance Examination (AISSEE) through our dedicated military preparation wing.", student_name="Sainik School Preparation Wing"),
        Achievement(title="Senior Secondary Board Result 98.6%", category="board", year=date.today().year,
                    description="Outstanding performance with top marks and multiple subject distinctions across Science, Commerce, and Arts streams.", student_name="Senior Secondary Class 12 Batch"),
        Achievement(title="Inter-School Basketball Champions", category="sports", year=date.today().year,
                    description="First place in the Jaipur District Inter-School Basketball Tournament and Cricket series.", student_name="SKR Sports Academy Squad"),
    ])
    NewsEvent.objects.create(
        kind="news",
        title="Admissions Open 2027-28 — Pre-Primary to Class 12",
        body="Admissions are now open for Session 2027-28 for Nursery through Class 12 (Science, Commerce, Arts) and our specialized Sainik School preparation batch. Visit our Kalwar Road campus or submit the online enquiry form."
    )
    NewsEvent.objects.create(
        kind="event",
        title="Annual Sports Academy & 10m Shooting Championship",
        event_date=date(2027, 1, 20),
        venue="SKR Sports Complex & Shooting Range, Kalwar Road, Jhotwara",
        body="Annual sports meet featuring basketball tournaments, cricket championship finals, and 10-meter air rifle/pistol shooting competitions."
    )
    NewsEvent.objects.create(
        kind="event",
        title="Annual Cultural Evening — Music, Dance & Drama",
        event_date=date(2027, 2, 15),
        venue="School Auditorium, Jhotwara, Jaipur",
        body="A grand showcase of student cultural talents including classical dance, musical orchestra, theatre plays, and student club exhibits."
    )
    Testimonial.objects.bulk_create([
        Testimonial(author_name="Parent Review (Facebook Verified)", relation="Parent, Jhotwara, Jaipur",
                    message="Shri Kalyan Radhey Academy is set in a peaceful residential area off Kalwar Road. We truly appreciate the disciplined setting, focus on character building, and very affordable fees. The 92% recommendation rate is genuinely deserved!", order=1),
        Testimonial(author_name="Rameshwar Choudhary", relation="Parent, Class 11 (Science Stream)",
                    message="Finding a school in Jhotwara with a dedicated 10-meter shooting range, basketball academy, and strong Science, Commerce, and Arts faculty with reasonable fees is rare. SKR School has exceeded all our expectations.", order=2),
        Testimonial(author_name="Kavita Rathore", relation="Parent, Middle School Wing",
                    message="The emphasis on military and Sainik school preparation along with activity-based learning has transformed my son's discipline, physical fitness, and academic focus. Outstanding mentorship!", order=3),
    ])
    Disclosure.objects.bulk_create([
        Disclosure(title="School General Information & Location Details", category="affiliation", is_public=True),
        Disclosure(title="Academic Streams & Curriculum Norms (Science, Commerce, Arts)", category="results", is_public=True),
        Disclosure(title="Campus Amenities, Laboratories & Sports Academy Facilities", category="infrastructure", is_public=True),
        Disclosure(title="Affordable Fee Structure & Parent Advisory Norms", category="fees", is_public=True),
    ])


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1:
        call_command("migrate", run_syncdb=True)
        seed_demo()
        sys.argv.append("runserver")
    elif sys.argv[1] == "runserver":
        if os.environ.get("RUN_MAIN") != "true":
            call_command("migrate", run_syncdb=True)
            seed_demo()
    elif sys.argv[1] == "createsuperuser":
        call_command("migrate", run_syncdb=True)
    elif sys.argv[1] == "migrate" and "--run-syncdb" not in sys.argv:
        sys.argv.append("--run-syncdb")

    execute_from_command_line(sys.argv)
