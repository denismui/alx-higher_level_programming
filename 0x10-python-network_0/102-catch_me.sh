#!/bin/bash
# A script that makes a request to prompt a specific response
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin: You got me!"
