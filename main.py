# Bintang Fajarianto
# NIM 13519138

# March 5, 2023

import time
from difflib import SequenceMatcher
from enum import Enum

from src.constant import *
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
      cipher = op.ECB(KEY)
    elif mode.name == "CBC":
      cipher = op.CBC(KEY)
    else:
      cipher = op.Counter(KEY)
    
    all_result += f"Mode: {mode.value}\n"

    # encryption
    start_timer = time.time()
    encrypted = cipher.encrypt(plain_text=data, toHex=True)
    end_timer = time.time()
    encrypt_time = end_timer - start_timer
    all_result += f"  - Encryption time: {encrypt_time} second\n"

    # Save Encrypted Result
    if mode.name == "ECB":
      encryption_file = os.path.join(RESULT_DIRECTORY, f"encrypted_{filename}")
      save_file(encryption_file, encrypted)

    # decryption
    start_timer = time.time()
    decrypted = cipher.decrypt(cipher_text=encrypted, fromHex=True)
    end_timer = time.time()
    decrypt_time = end_timer - start_timer
    all_result += f"  - Decryption time: {decrypt_time} second\n"

    # Save Decrypted Result
    if mode.name == "ECB":
      decryption_file = os.path.join(RESULT_DIRECTORY, f"decrypted_{filename}")
      save_file(decryption_file, decrypted)
  
  all_result += "\n----------\n"

# Save Result
all_result_file = os.path.join(RESULT_DIRECTORY, "encryption_time.txt")
save_file(all_result_file, all_result)


# Avalanche Effect
key1 = "Bystar138Cipherz"
key2 = "*ystar138Cipherz"
key3 = "Byst*r138Cipherz"
key4 = "Bystar13*Cipherz"
key5 = "Bystar138Cip*erz"
keys = [key1, key2, key3, key4, key5]
plain_text1 = "Bintang-13519138"
plain_text2 = "*intang-13519138"
plain_text3 = "Bint*ng-13519138"
plain_text4 = "Bintang-*3519138"
plain_text5 = "Bintang-1351*138"
plain_texts = [plain_text1, plain_text2, plain_text3, plain_text4, plain_text5]

# Comparing different Plain Text
result = f"Key: {key1}\n"
encrypted_list = []
for text in plain_texts:
  cipher = op.ECB(key1)
  result += f"- Plain text: {text}\n"

  cipher_text = cipher.encrypt(text, toHex=True)
  encrypted_list.append(cipher_text)
  result += f"  {cipher_text}\n"

result_file = os.path.join(AVALANCHE_EFFECT_DIRECTORY, f"comparing_plain_text.txt")
save_file(result_file, result)

# Comparing different Key
result = f"Plain text: {plain_text1}\n"
encrypted_list = []
for key in keys:
  cipher = op.ECB(key)
  result += f"- Key: {key}\n"

  cipher_text = cipher.encrypt(plain_text1, toHex=True)
  encrypted_list.append(cipher_text)
  result += f"  {cipher_text}\n"

result_file = os.path.join(AVALANCHE_EFFECT_DIRECTORY, f"comparing_key.txt")
save_file(result_file, result)
