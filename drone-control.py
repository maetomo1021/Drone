import socket
# ソケットはTCP通信行う上で必要となる
import time


serversocket = socket.socket(socket.AF_INET,socket.SOCK)
serversocket.bind(("localhost",8080))
serversocket = listen(1)
# listen()はストリーム・ソケットのみに対応しています
# クライアントの接続待機

(clientsocket,address) = serversocket.accept()
# クライアントの接続を許可する

msg = clientsocket.send(b"hello client")
clientsocket.close()


