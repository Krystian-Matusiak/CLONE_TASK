#!/usr/bin/env python3

import socket
import argparse
import logging
import json


def setup_logging(log_level):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main(socket_path, log_level, timeout_ms):
    setup_logging(log_level)
    logger = logging.getLogger('Consumer')

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(socket_path)
        sock.listen(1)
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
    parser = argparse.ArgumentParser(description='Consumer')
    parser.add_argument('--socket-path', type=str, required=True, help='Path to the Unix domain socket')
    parser.add_argument('--log-level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='Logging level')
    parser.add_argument('--timeout-ms', type=int, default=100, help='Socket timeout in milliseconds')

    args = parser.parse_args()
    main(args.socket_path, args.log_level, args.timeout_ms)
