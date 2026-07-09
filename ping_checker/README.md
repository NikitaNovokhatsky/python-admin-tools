# Ping Checker

Simple Python utility for checking host availability.

## Description

Ping Checker is a command-line tool that allows system administrators to quickly check whether a host is available over the network.

The tool uses the system ping command and analyzes the result.

## Features

- Check host availability
- Simple command-line interface
- Works with domains and IP addresses
- Fast network diagnostics

## Requirements

- Python 3.x
- Windows/Linux/macOS

## Usage

Run the script:

```bash
python ping_checker.py

Enter a host:

google.com

Example output:

google.com is ONLINE

Example with unavailable host:

192.168.1.250 is OFFLINE

Future improvements
Add command-line arguments
Add logging
Support checking multiple hosts
Export results to CSV