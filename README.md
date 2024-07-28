# DVRParams-decoder

# Argus Surveillance DVR 4.0 - Weak Password Encryption Exploit

## Description

This script exploits the weak password encryption mechanism used by Argus Surveillance DVR 4.0. The software uses a simplistic and insecure encoding scheme that can be easily reversed. This script takes an encoded string and decodes it to reveal the original password or other encoded data.

## Requirements

- Python 3.x

## Usage

Clone the repository and navigate to the directory containing the script. Use the following command to run the script:

```sh
python DVRParams-decoder.py -e "<encoded_string>"
