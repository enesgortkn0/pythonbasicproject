#SUBPROCESS TERMİNAL ÜZERİNDE YAZMAK İSTEDİKLERİNİ TEK KOD ÜZERİNDEN YAPMANI SAĞLAR
#OPTPARSE TERMİNAL ÜZERİNDEN İNPUT ALMAYA YARAR
import optparse
import subprocess

parse_object = optparse.OptionParser()

#-İ DEN SONRA AYZDIĞIMIZ DEĞER İNTERFACE KEYİ ÜZERİNE VALUE OLARAK KAYDEDİLİR
parse_object.add_option("-i","--interface",dest="interface",help="Enter interface!")
parse_object.add_option("-m","--mac",dest="mac_address",help="Enter mac address!")

#BURDAKİ DEĞERLER TUPLE OLARAK DÖNDÜRÜLÜR VE USER_İNPUTSA ALINIR
(user_inputs,arguments) = parse_object.parse_args()
#KODA VERDİĞİMİZ -İ VE -M DEĞERLERİNİ BURDA DEĞİŞKENE KAYDEDERİZ
interface = user_inputs.interface
mac_addr = user_inputs.mac_address

# VE ARTIK BURADA DA KOMUTLARI TERMİNALEDE ÇALIŞTIRIRIZ
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_addr])
subprocess.call(["ifconfig",interface,"up"])
subprocess.call(["ifconfig"])