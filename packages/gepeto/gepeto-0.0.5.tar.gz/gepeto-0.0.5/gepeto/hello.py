import time

web = '''
##web.py
##web.py
from fastapi import FastAPI

app = FastAPI()

@app.post('/message_webhook')
def process_message():
    print('Hey Dad')

@app.post('/send_message')
def send_message():
    print('Hi Pinocchio')
'''

worker = '''
##worker.py
from rq import Queue
from redis import Redis
from hello import process_message
import time

q = Queue(connection=Redis())

while True:
    q.enqueue(process_message)
    time.sleep(1)

'''

def wake():
    x = input("Welcome to my workshop. What can I do for you today")
    time.sleep(.5)
    print('hmm..')
    time.sleep(1)
    print("I have to go, but here's a web and worker outline.")
    print('---web.py and worker.py created---')
    #initialize the skeleton as web.py
    with open('web.py', 'w') as f:
        f.write(web)
    with open('worker.py', 'w') as f:
        f.write(worker)

    