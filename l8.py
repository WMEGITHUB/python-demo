from enum import Enum
from enum import IntEnum, unique

@unique
class VIP(IntEnum):
  YELLOW = 1
  BLACK = 2

print(VIP.BLACK)
print(VIP.BLACK.value)
print(VIP.BLACK.name)
print(VIP(1))

