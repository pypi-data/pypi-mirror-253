import pyfishhash
import time

data = memoryview(b'the quick brown fox jumps over the lazy dog')

start1 = time.time()
assert pyfishhash.hash(data.tobytes()).hex() == "6f4429716dc009d5d3b9775a4d6a5d58bccd9f73386bf88da7d5afdf5deb50f1"
print(f'Test #1 tooks {time.time() - start1} seconds.')

start2 = time.time()
assert pyfishhash.hash(data.tobytes()).hex() == "6f4429716dc009d5d3b9775a4d6a5d58bccd9f73386bf88da7d5afdf5deb50f1"
print(f'Test #2 tooks {time.time() - start2} seconds.')
