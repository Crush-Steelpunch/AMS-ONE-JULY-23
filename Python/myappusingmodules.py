import mymodules
from text_generator import generate

print(mymodules.mrshouty("whisper"))

print(mymodules.add5toanynumber(42.6))

print(mymodules.len())

print(len(['cat']))

print(generate(length_minimal=10, length_maximal=15, int_min_length=9999, int_max_length=9999999))