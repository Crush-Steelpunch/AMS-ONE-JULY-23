import string, random

passvar = ''
for i in range(32):
    passvar = passvar + random.choice(string.ascii_letters+string.punctuation)

print(passvar)