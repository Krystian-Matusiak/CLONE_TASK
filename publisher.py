#!/usr/bin/env python3

import socket
import time
import json


def main():
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # TODO: add socket path
        sock.connect(socket_path)
        
        while True:
            # TODO: implement generating imu data
            imu_data = generate_imu_data()
            message = json.dumps(imu_data)
            sock.sendall(message.encode('utf-8'))
            # TODO: add interval
            time.sleep(interval)
            
    except Exception as e:
        #TODO: implement error handling
        pass
    finally:
        sock.close()

if __name__ == "__main__":
    main()
