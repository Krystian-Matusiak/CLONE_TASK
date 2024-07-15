#!/usr/bin/env python3

import socket
import logging
import time
import json

def setup_logging(log_level):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main(log_level):
    setup_logging(log_level)
    logger = logging.getLogger('Publisher')

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        logger.info('Connecting to consumer...')
        # TODO: add socket path
        sock.connect(socket_path)
        logger.info('Connected to consumer')
        
        while True:
            # TODO: implement generating imu data
            imu_data = generate_imu_data()
            message = json.dumps(imu_data)
            logger.info(f'Sending IMU data: {message}')
            sock.sendall(message.encode('utf-8'))
            # TODO: add interval
            time.sleep(interval)
            
    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        logger.info('Closing socket')
        sock.close()
        logger.info('Socket closed')

if __name__ == "__main__":
    main()
