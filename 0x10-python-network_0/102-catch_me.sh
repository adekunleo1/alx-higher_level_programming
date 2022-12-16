#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a message "You got me!"
curl -sL http://0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: You got me!"
