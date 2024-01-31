from crontab import CronTab
import shutil

cron = CronTab(user=True)
CRON_COMMENT = 'odk-mailer-cron'

def setup():

    job = find()

    if job and job.is_valid():
        #print("Found valid Cron Job.")
        pass
    else:
        clear()
        create()

def find():

    jobExists = False

    genCron = cron.find_comment(CRON_COMMENT)
    for job in genCron:
        jobExists = True

    if jobExists:
        return job

    return None
        
def create():    

    WHICH_ODK = shutil.which("odk-mailer")
    CRON_COMMAND = 'bash -l -c "' +  WHICH_ODK + ' jobs evaluate --force"' # 2>&1 | logger -t mycmd  https://askubuntu.com/a/967798

    job = cron.new(
        #command= '/home/tertek/.cache/pypoetry/virtualenvs/odk-mailer-Dxt_EVX8-py3.10/bin/odk-mailer evaluate --force',
        command = CRON_COMMAND,
        comment= CRON_COMMENT
        )
    # Set to every 15 Minutes
    # testing every minute
    job.minute.every(1)
    
    cron.write()
    #print("Created Cron Job.")

def clear():
    cron.remove_all(comment=CRON_COMMENT)
    #print("Removed Cron Job.")

def enable():
    job = find()
    if job:
        job.enable()

def disable():
    job = find()
    if job:
        job.enable(False)