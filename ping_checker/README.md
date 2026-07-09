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

## Logging

The application stores execution results in:


logs/ping_checker.log


Example:


2026-07-09 12:30:55 | INFO | google.com is ONLINE

## Usage

Run the script:

```bash
python ping_checker.py google.com

## Multiple hosts checking

You can check multiple hosts from a file.

Example:

```bash
python ping_checker.py --file servers.txt

servers.txt example:

google.com
8.8.8.8
github.com