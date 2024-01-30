import runpod
import os
from dotenv import load_dotenv, find_dotenv


def load_runpod_token():
  _ = load_dotenv(find_dotenv())
  RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY", "add-here-if-not-set-in-env-file")
  assert not RUNPOD_API_KEY.startswith("add-here"), "This doesn't look like a valid Runpod API Key"

  runpod.api_key = RUNPOD_API_KEY 
  print("RUNPOD_API_KEY: " + runpod.api_key[0:6], "\n")
  return RUNPOD_API_KEY

def runpod_info(api_key):
  runpod.api_key = api_key 
  print("GPUs: ")
  for gpu in runpod.get_gpus():
      detail = runpod.get_gpu(gpu["id"])
      print(detail)
