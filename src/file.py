# Bintang Fajarianto
# NIM 13519138

# March 5, 2023

import os

def read_file(path: str) -> str:
  # read the whole file
  with open(path, 'r') as f:
    data = f.read()
  
  # close file
  f.close()

  return data

def save_file(path: str, data: str):
  # save the data to path
  with open(path, 'w') as f:
    f.write(data)
  
  # close file
  f.close()

def get_all_files(directory: str) -> list[str]:
  return [os.path.join(directory, filename) for filename in os.listdir(directory)]
