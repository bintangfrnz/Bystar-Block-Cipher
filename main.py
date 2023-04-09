# Bintang Fajarianto
# NIM 13519138

# March 5, 2023

import time
from enum import Enum

from src.constant import TEST_DIRECTORY, RESULT_DIRECTORY, KEY
from src.file import *
import src.operation as op
 
class OperationMode(Enum):
  ECB = "ECB"
  CBC = "CBC"
  Counter = "Counter"

list_files = get_all_files(TEST_DIRECTORY)

all_result = ""
for file in list_files:
  all_result += f"Plain text location: {file}\n\n"
  data = read_file(file)

  filename = file.split('/')[1]
  for mode in OperationMode:
    if mode.name == "ECB":
      all_result += f"Mode: {mode.name}\n"
      cipher = op.ECB(KEY)

      # encryption
      start_timer = time.time()
      encrypted = cipher.encrypt(data)
      end_timer = time.time()
      encrypt_time = end_timer - start_timer
      all_result += f"  - Encryption time: {encrypt_time} second\n"

      # Save Encrypted Result
      result_file = os.path.join(RESULT_DIRECTORY, f"encrypted_{filename}")
      save_file(result_file, encrypted)

      # decryption
      start_timer = time.time()
      decrypted = cipher.decrypt(encrypted)
      end_timer = time.time()
      decrypt_time = end_timer - start_timer
      all_result += f"  - Decryption time: {decrypt_time} second\n"

      # Save Decrypted Result
      result_file = os.path.join(RESULT_DIRECTORY, f"decrypted_{filename}")
      save_file(result_file, decrypted)

    elif mode.name == "CBC":
      all_result += f"Mode: {mode.name}\n"
      cipher = op.CBC(KEY)

      # encryption
      start_timer = time.time()
      encrypted = cipher.encrypt(data)
      end_timer = time.time()
      encrypt_time = end_timer - start_timer
      all_result += f"  - Encryption time: {encrypt_time} second\n"


      # decryption
      start_timer = time.time()
      decrypted = cipher.decrypt(encrypted)
      end_timer = time.time()
      decrypt_time = end_timer - start_timer
      all_result += f"  - Decryption time: {decrypt_time} second\n"

    elif mode.name == "Counter":
      all_result += f"Mode: {mode.name}\n"
      cipher = op.Counter(KEY)

      # encryption
      start_timer = time.time()
      encrypted = cipher.encrypt(data)
      end_timer = time.time()
      encrypt_time = end_timer - start_timer
      all_result += f"  - Encryption time: {encrypt_time} second\n"

      # decryption
      start_timer = time.time()
      decrypted = cipher.decrypt(encrypted)
      end_timer = time.time()
      decrypt_time = end_timer - start_timer
      all_result += f"  - Decryption time: {decrypt_time} second\n"
  
  all_result += "\n----------\n"

# Save Result
all_result_file = os.path.join(RESULT_DIRECTORY, "result.txt")
save_file(all_result_file, all_result)
