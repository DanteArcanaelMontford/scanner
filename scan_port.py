import argparse
import socket
from pyfiglet import Figlet
f = Figlet(font='slant')

class SCAN:
  def __init__(self, ip: str) -> None:
    self._ip = ip

  def portscan(self, port: int):
    __socket__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = __socket__.connect_ex((self._ip, port))
    if(connection == 0):
      print(f"|\tPort {port} \t\t\t    [OPEN]    |")
      __socket__.close()
            

def args():
  parser = argparse.ArgumentParser(description='Port Scan.')
  parser.add_argument("-i", "--ip", type=str, help="Enter ip to scan", required=True)
  parser.add_argument("-p", "--port", type=int, nargs='+', help="Usecase: -p 80 or -p 21 22 25")
  arguments = parser.parse_args()
  return [arguments.ip, arguments.port]


def create_line(length):
  print("-----" * length)

def header():
  create_line(11)
  print(f.renderText('PORTSCAN'))
  print("\n\t\t     SCANNING PORTS\n")
  create_line(11)
  print("|\tPORTS\t\t\t\t    STATUS    |")
  create_line(11)

ip = args()[0]
ports = args()[1]
header()
scan = SCAN(ip)


if ports is not None:
  for port in ports:
    scan.portscan(port)  
  create_line(11)
else:
  for port in range(1, 65535):
    scan.portscan(port)
  create_line(12)