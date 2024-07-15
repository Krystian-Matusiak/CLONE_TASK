#!/usr/bin/env python3

import socket
import json

def main():
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # TODO: add socket path
        sock.bind(socket_path)
        sock.listen(1)
        # TODO: add timeout
        sock.settimeout(timeout_ms / 1000)
        
        try:
            connection, _ = sock.accept()
            
            while True:
                try:
                    data = connection.recv(1024).decode('utf-8')
                    if data:
                        imu_data = json.loads(data)
                        # TODO: implement parsing imu data
                        vel, acc, mag = parse_imu_data(imu_data)
                    else:
                        break
                except socket.timeout:
                    pass
                
        except Exception as e:
            # TODO: handle exception
            pass
        finally:
            if connection:
                connection.close()

    except Exception as e:
        # TODO: handle exception
        pass
    finally:
        sock.close()

if __name__ == "__main__":
    main()
