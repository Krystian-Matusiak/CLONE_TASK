# Publisher-Subscriber IMU Data Exchange

This project shows a simple use of publisher-subscriber model for exchanging IMU data. The publisher sends IMU data that is velocity, acceleration, and magnetometer readings in X, Y, and Z directions as this format is common for this sensor. These data will be sent over a Unix socket.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Publisher](#publisher)
  - [Flags](#publisher-flags)
- [Subscriber](#subscriber)
  - [Flags](#subscriber-flags)
- [Example Commands](#example-commands)

## Requirements

- Python 3.6 or later
- Required Python libraries: `argparse`, `logging`, `socket`, `time`

## Usage

This project includes two main scripts: `publisher.py` and `subscriber.py`.

## Publisher

The publisher sends IMU data at a specified frequency.

### Flags

- `--socket-path`: Path to the Unix socket (required).
- `--log-level`: Logging level (default: `INFO`).
- `--frequency`: Frequency of sending data in times per second (required).

### Example Command

```bash
python publisher.py --socket-path /tmp/imu_socket --log-level INFO --frequency 1
```

## Subscriber

The subscriber receives IMU data from the publisher.


### Flags

- `--socket-path`: Path to the Unix socket (required).
- `--log-level`: Logging level (default: `INFO`).
- `--timeout-ms`: Timeout for receiving data in milliseconds (required).

### Example commands 

```bash
python subscriber.py --socket-path /tmp/imu_socket --log-level INFO --timeout-ms 12000
```