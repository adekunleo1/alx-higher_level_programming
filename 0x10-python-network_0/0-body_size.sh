#!/bin/bash
# Script that sends a request to a URL and displays the size of the response body.
curl -Is "$1" | grep Content-Length | cut -d: -f2
