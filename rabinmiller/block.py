# Autorka programu: Natalia Niewiadowska, grupa 2

from PIL import Image
import hashlib
import random
import os


image = Image.open("plain.bmp").convert("L")
image_data = image.tobytes()
size = image.size
block_size = 8

keys = []
if os.path.exists("key.txt"):
  with open("key.txt", "r") as key_file:
    key = key_file.read().encode()
    keys = [key for _ in range(size[0] * size[1])]
else:
  for _ in range(size[0] * size[1]):
    key = hashlib.md5(str(random.random()).encode("UTF-8")).digest()
    keys.append(key)

# ECB
ecb_data = []
for i in range(0, len(image_data), block_size):
  block = image_data[i:i+block_size]
  encrypted_block = bytes(b ^ k for b, k in zip(block, key))
  ecb_data.extend(encrypted_block)

# CBC
cbc_data = []
iv = random.getrandbits(8) 
prev_encrypted_block = iv.to_bytes(block_size, "big")

for y in range(size[1]):      # height
  for x in range(size[0]):    # width
    pp = y * size[0] + x
    op = image_data[pp]
    key_index = pp % len(keys)

    xor_result = op ^ prev_encrypted_block[x % block_size]
    pta = xor_result ^ keys[key_index][x % block_size]
    cbc_data.append(pta)
    prev_encrypted_block = pta.to_bytes(block_size, "big")

# saving
def save(data, path):
  new_data = bytes(data)

  output_image = image.copy()
  output_image.frombytes(new_data)
  output_image.save(path)


save(ecb_data, "ecb_crypto.bmp")
save(cbc_data, "cbc_crypto.bmp")
print("ECB and CBC mode encryption saved in ecb_crypto.bmp and cbc_crypto.bmp.")