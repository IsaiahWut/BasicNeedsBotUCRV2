# 🕒 Scheduled Web Scraper

This project is a Python web scraper that runs automatically every day at 11:17 AM, using GitHub Actions as the scheduler.
It includes built-in logic to ensure it only runs twice per week (Sunday → Sunday) to avoid overloading the target website.


## 🚀 Features

    ⏰ Automated Scheduling — Runs daily at 11:17 AM via GitHub Actions cron jobs.
    
    🧠 Weekly Run Limit — The scraper will only run a maximum of 2 times per week.
    
    ☁️ Cloud-Based — Runs on GitHub’s cloud runner, so your local machine doesn’t need to be on.
    
    📝 Logging — Keeps a record of past runs in a JSON file for easy tracking.
    
    🕵️ Web Scraping — Extracts and processes data from your target website automatically.


## 📦 Project Structure
``` 
    .
    ├── scraper.py              # Main script that performs the scraping task
    ├── run_tracker.json        # Keeps track of run timestamps for weekly limit
    ├── .github/
    │   └── workflows/
    │       └── schedule.yml    # GitHub Actions workflow file for scheduling
    └── README.md               # Project documentation
```

