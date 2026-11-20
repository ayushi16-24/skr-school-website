# Shri Kalyan Radhey Academy (SKR School) — Website

Single-file Django website for Shri Kalyan Radhey Academy (SKR School), Jhotwara, Jaipur.
Features public pages, academic streams (Science, Commerce, Arts), Sainik/Military prep wing, 10m shooting academy, sports facilities, admissions forms, news & events, campus gallery, and admin panel.

## Local Setup & Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start server (automatically syncs database, loads initial data, and runs server):
   ```bash
   python school_site.py
   ```
3. Open in browser:
   - Website: http://127.0.0.1:8000/
   - Admin:   http://127.0.0.1:8000/admin/

4. (Optional) Create admin user:
   ```bash
   python school_site.py createsuperuser
   ```

## Render Deployment

This project includes `render.yaml`, `build.sh`, and `Procfile` configured for Render:

1. Create a repository on GitHub (e.g. `skr-school-website`)
2. Push your code:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
3. In [Render Dashboard](https://dashboard.render.com):
   - Click **New +** -> **Web Service**
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` (or choose **Python 3** environment)
   - Build Command: `./build.sh`
   - Start Command: `gunicorn school_site:application`
