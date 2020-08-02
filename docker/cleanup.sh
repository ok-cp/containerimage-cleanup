#!/bin/sh
cat <(crontab -l) <(echo "$CRON_TIME" 'python3 /container-cleanup.py >> /container-cleanup.log 2>&1') | crontab -
crontab -l