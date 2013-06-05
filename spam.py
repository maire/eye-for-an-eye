import requests,string,random
from random import randint
from threading import Thread

#url = 'http://nikolas-davila.com/roca/56433.php'

def randomString():
  return ''.join(random.sample(string.ascii_lowercase, randint(5,20)))

def hammer():
  while True:
    print 'debug'
    pw = randomString()
    em = '{0}@{1}.com'.format(randomString(), randomString())
    req = requests.post(url, files={'step': 'confirmation', 'rt': '', 'rp': '', 'emailu': em, 'passu': pw}, allow_redirects=False)
    if 'sendmail' in req.text:
      print 'sendmail error!'

threads = []

for x in range(1, 10):
  threads[x] = Thread(target = hammer)

for thread in threads:
  thread.start()

thread[0].join()