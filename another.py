from prefect import flow

@flow(log_prints=True)
def hello(name: str):
  print(f"Hello {name}!")
