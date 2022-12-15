#!/bin/bash
# Script that displays only the status code of an HTTP request
curl -s -o /dev/null -w "%{http_code}" "$1"
