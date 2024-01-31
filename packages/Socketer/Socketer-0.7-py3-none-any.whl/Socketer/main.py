import socket

servers = []

def hello():
  print("Hello from Socketer")
def create_server(id,servername,port,mainfolder,mainhtmlcode,mainpythoncode):
  server = id[servername,port,mainfolder,mainhtmlcode,mainpythoncode]
  servers.append(server)
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server_address = ('localhost', port)
  server_socket.bind(server_address)
  return server_socket
def run_server(id,server_socket,connecters):
  servers[id].append(server_socket)
  server_socket.listen(connecters)

  client_socket, client_address = server_socket.accept()
  print('Connection from', client_address)

  # Receive and print messages
  while True:
      data = client_socket.recv(4096)
      print('Received:', data.decode('utf-8'))
      index = open(""+servers[id][mainfolder]+"/"+servers[id][mainpythoncode]+"".format(data.decode('utf-8')),'r')
      indexdata = index.read()
      index.close()
      client_socket.send(indexdata.encode('utf-8'))
def stop_server(id):
   servers[id][server_socket].close()
def sent(id,message):
   servers[id][server_socket].send(message.encode('utf-8'))
def server_list():
   print(servers)
