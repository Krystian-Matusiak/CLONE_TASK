#!/usr/bin/env python3

import socket
import argparse
import logging
import time
import random
import json

def setup_logging(log_level):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def generate_imu_data():    
    imu_data = {
        "vel": [random.randint(0, 65535) for _ in range(3)],
        "acc": [random.randint(0, 65535) for _ in range(3)],
        "mag": [random.randint(0, 65535) for _ in range(3)]
    }
    return imu_data


def main(socket_path, log_level, frequency):
    setup_logging(log_level)
    logger = logging.getLogger('Publisher')
    interval = 1.0 / frequency

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
            time.sleep(interval)
            
    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        logger.info('Closing socket')
        sock.close()
        logger.info('Socket closed')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Publisher')
    parser.add_argument('--socket-path', type=str, required=True, help='Path to socket')
    parser.add_argument('--log-level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='Logging level')
    parser.add_argument('--frequency', type=int, required=True, help='Frequency of sending data (times per second)')

    args = parser.parse_args()
    main(args.socket_path, args.log_level, args.frequency)
