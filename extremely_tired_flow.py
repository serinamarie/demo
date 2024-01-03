from prefect import flow
from time import sleep

@flow(log_prints=True)
def tired_flow():
    print("I'm so tired...")
    sleep(1)
    for i in range(10):
        print("Sleeping for 24 hours...")
        sleep(90000)
