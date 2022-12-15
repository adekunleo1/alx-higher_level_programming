#!/bin/bash
# Script that sends a POST request from a JSON file and displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
