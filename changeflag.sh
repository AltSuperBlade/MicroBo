#!/bin/bash

function help {
    echo "-n [New Flag Text]                    修改flag信息"
    echo "-r                                    重置flag信息为默认值：flag{flag_test}"
    echo "-h                                    帮助文档"
}

function change_flag {
    newflag=$1

    id=$(docker ps | grep "microbo" | awk '{print $1}')

    docker exec -it "$id" ./flagchange.sh "$newflag"

}

while [ "$1" != "" ];do
    case "$1" in
        "-n")
            change_flag "$2"
            exit 0
            ;;
        "-r")
            change_flag "flag{flag_test}"
            exit 0
            ;;
        "-h")
            help 
            exit 0
            ;;
    esac
done