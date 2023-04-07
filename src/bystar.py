# Bintang Fajarianto
# NIM 13519138

# March 5, 2023

import random

from constant import *
from utils import *

class Bystar:
  def format_key(self, bits: list[int]):
    if len(bits) == BLOCK_SIZE:
      return bits
    elif len(bits) < BLOCK_SIZE:
      return bits + [0] * (BLOCK_SIZE - len(bits))
    else:
      return bits[:BLOCK_SIZE]
    
  def generate_different_keys(self, bit_rep: list[int], iter: int) -> list[int]:
    # Generate new permutation table
    copy_table = PERMUTATION_TABLE.copy()
    random.seed(iter)
    random.shuffle(copy_table)

    # Permutation
    c_key = self.permutate(bit_rep, copy_table)

    # Split key to four parts
    c_key = bits_to_int(c_key)
    quarter = [c_key[i:i+4] for i in range(0, len(c_key), 4)]

    # XOR 1st ^ 3rd and 2nd ^ 4th
    first_half = [quarter[0][i] ^ quarter[2][i] for i in range(len(quarter))]
    last_half = [quarter[1][i] ^ quarter[3][i] for i in range(len(quarter))]

    # Shift left the first half
    # Shift right the last half
    # by current iteration modulo total iteration
    c_key = shift_right(first_half, iter % ITERATION) + shift_left(last_half, iter % ITERATION)

    return int_to_bits(c_key)
    
  def generate_internal_key(self, key: str) -> list:
    bit_rep = self.format_key(string_to_bits(key))
    return [self.generate_different_keys(bit_rep, idx) for idx in range(ITERATION)]
  
  def encrypt(self, bit_rep: list[int], internal_keys: list[list[int]]) -> str:
    # Permutation
    c_list = self.permutate(bit_rep, IP_MATRIX)

    # Convert bit rep to list[int]
    c_list = bits_to_int(c_list)

    # Split current bit rep
    left, right = c_list[: len(c_list) // 2], c_list[len(c_list) // 2:]

    # Feitsel Network
    for idx in range(ITERATION - 1, -1, -1):
      # rotation
      pass

    # Convert list[int] to bit rep
    c_list = int_to_bits(left + right)

    # Permutation
    c_list = self.permutate(c_list, INVERSE_IP_MATRIX)

    return c_list
  
  def decrypt(self, bit_rep: list[int], internal_keys: list[list[int]]) -> str:
    # Permutation
    c_list = self.permutate(bit_rep, IP_MATRIX)

    # Convert bit rep to list[int]
    c_list = bits_to_int(c_list)

    # Split current bit rep
    left, right = c_list[: len(c_list) // 2], c_list[len(c_list) // 2:]

    # Feitsel Network
    for idx in range(ITERATION - 1, -1, -1):
      # rotation
      pass

    # Convert list[int] to bit rep
    c_list = int_to_bits(left + right)

    # Permutation
    c_list = self.permutate(c_list, INVERSE_IP_MATRIX)

    return c_list
  
  def rotation(self):
    return
  
  def permutate(self, bit_rep: list[int], table: list[int]) -> list[int]:
    result = [0] * BLOCK_SIZE
    for idx, bit in enumerate(bit_rep):
      result[table[idx] - 1] = bit
    return result

# cipher = Bystar()
# cipher.encrypt(string_to_bits("abcdefghijklmnop"), cipher.generate_internal_key(KEY))
