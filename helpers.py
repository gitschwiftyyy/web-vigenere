def shiftnums(rotphrase):
  shifts = []
  for i in range(len(rotphrase)):
    if ord(rotphrase[i]) > 64 and ord(rotphrase[i]) < 91:
      shift = ord(rotphrase[i]) - 65
    elif ord(rotphrase[i]) > 96 and ord(rotphrase[i]) < 123:
      shift = ord(rotphrase[i]) - 97
    elif ord(rotphrase[i]) > 47 and ord(rotphrase[i]) < 58:
      shift = int(rotphrase[i])
    else:
      return False
    shifts.append(shift)
  return shifts
