import zlib

data = b"Data to be compressed. Data to be compressed. Data to be compressed."
compressed_data = zlib.compress(data)
print(f"Compressed: {compressed_data}")

decompressed_data = zlib.decompress(compressed_data)
print(f"Decompressed: {decompressed_data.decode()}")
