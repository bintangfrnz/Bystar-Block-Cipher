# Bintang Fajarianto
# NIM 13519138

# March 5, 2023

from abc import ABC, abstractmethod
from bystar import Bystar
from constant import BLOCK_SIZE, KEY, PLAIN_TEXT
from utils import string_to_bits, bits_to_string

# region OperationMode
class OperationMode(ABC):
  def __init__(self, key: str) -> None:
    super().__init__()
    self.bystar = Bystar()
    self.internal_key = self.bystar.generate_internal_key(key)
  
  def execute_per_block(self, text: str):
    bit_rep = string_to_bits(text)

    for idx in range(0, len(bit_rep), BLOCK_SIZE):
      block = bit_rep[idx:idx + BLOCK_SIZE]
      if len(block) < BLOCK_SIZE:
        block += [0] * (BLOCK_SIZE - len(block))
      yield block
  
  @abstractmethod
  def encrypt(self, text: str) -> str:
    pass

  @abstractmethod
  def decrypt(self, text: str) -> str:
    pass
# endregion OperationMode


# region ECB Mode
class ECB(OperationMode):

  def encrypt(self, plain_text: str) -> str:
    result = ""
    for block in super().execute_per_block(plain_text):
      result += self.bystar.encrypt(block, self.internal_key)

    return result
  
  def decrypt(self, cipher_text: str) -> str:
    result = ""
    for block in super().execute_per_block(cipher_text):
      result += self.bystar.decrypt(block, self.internal_key)

    return result
# endregion ECB Mode


# Testing ECB Mode
'''
cipher = ECB(KEY)
encrypted = cipher.encrypt(PLAIN_TEXT)
print(encrypted)
decrypted = cipher.decrypt(encrypted)
print(decrypted)
'''
