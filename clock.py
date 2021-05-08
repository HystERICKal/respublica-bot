from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from respublica import respublica_bot

# The Procfile in the project basically tells heroku to run this project using this clock

# def job_function():
#     print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(respublica_bot, 'interval', hours=24)

sched.start()