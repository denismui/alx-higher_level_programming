#!/bin/bash
# a Bash script that displays the size of the body of a response
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
