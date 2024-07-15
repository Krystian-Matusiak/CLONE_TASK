#!/usr/bin/env python3

import socket
import logging
import json


def setup_logging(log_level):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    setup_logging(log_level)
    logger = logging.getLogger('Consumer')

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # TODO: add socket path
        sock.bind(socket_path)
        sock.listen(1)
        # TODO: add timeout
        sock.settimeout(timeout_ms / 1000)
        logger.info('Waiting for a connection...')

        try:
            connection, _ = sock.accept()
            logger.info('Connection accepted')

            while True:
                try:
                    data = connection.recv(1024).decode('utf-8')
                    if data:
                        imu_data = json.loads(data)
                        # TODO: implement parsing imu data
                        vel, acc, mag = parse_imu_data(imu_data)
                        logger.info(f'Received IMU data - Velocity: {vel}, Acceleration: {acc}, Magnetometer: {mag}')
                    else:
                        logger.info('No data received, closing connection')
                        break
                except socket.timeout:
                    logger.warning('Socket timeout, retrying...')
                
        except Exception as e:
            logger.error(f'Error occurred: {e}')
        finally:
            if connection:
                logger.info('Closing connection...')
                connection.close()
                logger.info('Closed')

    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        logger.info('Closing socket')
        sock.close()
        logger.info('Socket closed')

if __name__ == "__main__":
    main()
