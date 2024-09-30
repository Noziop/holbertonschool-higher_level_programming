#!/usr/bin/python3
'''module for network serialization'''

import json
import socket
import time
import threading

server_ready = threading.Event()

def start_server(host='localhost', port=12345):
    '''function to start a server'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}")
    server_ready.set()  # Signale que le serveur est prêt

    try:
        server.settimeout(10)  # Timeout de 10 secondes
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        if data:
            received_dict = json.loads(data.decode())
            print("Received Dictionary from Client:")
            print(received_dict)
        conn.close()
    except socket.timeout:
        print("Debug: Server timed out waiting for connection")
    except Exception as e:
        print(f"Debug: An error occurred in server: {e}")
    finally:
        server.close()

def send_data(data, host='localhost', port=12345):
    '''function to send data to a server'''
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.send(json.dumps(data).encode())
        time.sleep(0.1)  # Petit délai pour s'assurer que les données sont traitées
        client.close()
        print("Data sent successfully")
    except Exception as e:
        print(f"Debug: An error occurred in send_data: {e}")
