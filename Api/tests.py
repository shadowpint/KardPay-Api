from django.test import TestCase

# Create your tests here.
import string
import random
def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
print id_generator()