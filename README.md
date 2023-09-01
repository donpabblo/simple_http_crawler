# Prerequisities
Google sheet doGet deployment (es. `https://docs.google.com/spreadsheets/d/1HkGH59EYyf77QOWY48t5Fifqo1ulYdxAYlbCht-SZno/edit#gid=0`)
- Python 3
- Speedify

# Installation
Run Speedify.

Create virtual environment.

```bash
python -m venv venv
```
Activate virtual environment.
```bash
venv\Scripts\activate.bat
```
Install requirements.
```bash
pip install -r requirements.txt
```
# Configuration
Fill the google sheet with urls.

Configure `config.ini`
```bash
[SHEET]
url = google_sheet_deployment_url

[APP]
wait_time = wait_time_between_iterations
rotate_ip = true/false
min_wait = min_wait_time_between_urls
max_wait = max_wait_time_between_urls

[SPEEDIFY]
path = path_to_speedifycli (es. C:\Program Files (x86)\Speedify\speedify_cli.exe)
country = country_for_ip (es. it)
wait_time = wait_time_after_ip_switch
```

# RUN
```bash
python run.py
```
