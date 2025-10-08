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

## ⚙️ How It Works

        GitHub Actions Workflow (schedule.yml)
        
        Uses a cron schedule: 17 11 * * * (runs every day at 11:17 AM UTC).
        
        Executes scraper.py automatically in the cloud.
        
        Run Limiting Logic
        
        scraper.py checks run_tracker.json for timestamps of past runs.
        
        If the script has already executed twice in the current Sunday-to-Sunday week, it will skip execution.
        
        Otherwise, it performs the scraping and appends the current timestamp to the tracker file.
        
        Output Handling
        
        The scraped data (and/or logs) can be saved to the repository.

## 🛠️ Setup Instructions

Clone the Repository

```
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
```


Edit the Schedule (Optional)

    To change the run time, open .github/workflows/schedule.yml and update:

```
        schedule:
          - cron: "17 11 * * *"  # minute hour day month weekday
```


(This runs at 11:17 AM UTC — adjust as needed.)

Commit & Push

```
git add .
git commit -m "Set up scheduled scraper with weekly limit"
git push origin main
```


Enable GitHub Actions

Go to your repo → Actions tab → Enable workflows if prompted.
