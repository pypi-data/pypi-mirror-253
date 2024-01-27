import time

skeleton = '''
##web.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/bots')
def get_bots():
    print('Pinocchio')
'''

def wake():
    x = input("Welcome to my workshop. What can I do for you today")
    time.sleep(5)
    print('hmm..')
    time.sleep(1)
    print("I have to go, but here's a skeleton.")
    #initialize the skeleton as web.py
    with open('web.py', 'w') as f:
        f.write(skeleton)