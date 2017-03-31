from helpers import shiftnums

def encrypt(string, rot):
  newstring = ""
  shiftidx = 0
  shifts = shiftnums(rot)
  for i in range(len(string)):
        chrnumber = ord(string[i])
        chrnumber = int(chrnumber)
        if chrnumber > 64 and chrnumber < 91:
            chrnumber = chrnumber + shifts[shiftidx]
            shiftidx += 1
            if shiftidx == len(shifts):
              shiftidx = 0
            if chrnumber > 90:
                chrnumber =  chrnumber % 90
                chrnumber = chrnumber + 64
        elif chrnumber > 96 and chrnumber < 123:
            chrnumber = chrnumber + shifts[shiftidx]
            shiftidx += 1
            if shiftidx == len(shifts):
              shiftidx = 0
            if chrnumber > 122:
                chrnumber = chrnumber % 122
                chrnumber = chrnumber + 96
        newchr = chr(chrnumber)
        newstring = newstring + newchr
  
  return newstring

def decrypt(string,rot):
  newstring = ""
  shiftidx = 0
  shifts = shiftnums(rot)
  for i in range(len(string)):
        chrnumber = ord(string[i])
        chrnumber = int(chrnumber)
        if chrnumber > 64 and chrnumber < 91:
            chrnumber = chrnumber - shifts[shiftidx]
            shiftidx += 1
            if shiftidx == len(shifts):
              shiftidx = 0
            if chrnumber < 65:
                chrnumber =  65 % chrnumber
                chrnumber = 91 - chrnumber
        elif chrnumber > 96 and chrnumber < 123:
            chrnumber = chrnumber - shifts[shiftidx]
            shiftidx += 1
            if shiftidx == len(shifts):
              shiftidx = 0
            if chrnumber < 97:
                chrnumber = 97 % chrnumber
                chrnumber = 123 - chrnumber
        newchr = chr(chrnumber)
        newstring = newstring + newchr
  
  return newstring

def main():
  switch = "y"
  while switch == "y" or switch == "Y":
    string = input("Enter text: ")
    rot = input("Encryption Phrase: ")
    print(encrypt(string, rot))
    switch = input("Continue? [y/n]: ")

if __name__ == "__main__":
  main()

  
  
  
  
  
  
  
  