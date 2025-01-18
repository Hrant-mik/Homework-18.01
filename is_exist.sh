#!/bin/bash

is_exist() {
    if [ -f "$1" ]; then
        echo "File is exist"
    else
        echo "File does not exist"
    fi
}

echo "Enter filename"
read filename
is_exist "$filename"

