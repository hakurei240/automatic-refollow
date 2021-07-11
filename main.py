from apscheduler.schedulers.blocking import BlockingScheduler
import refollow

twische = BlockingScheduler()
count = 0

@twische.scheduled_job('interval',minutes=60)
def timed_job():
  refollow.ref()
  global count
  if count == 12:
    refollow.bot_tweet()
    count = 0
  else:
    count = count + 1
  
if __name__ == "__main__":
  twische.start()
  
