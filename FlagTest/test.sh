#!/bin/sh

KOUT=/home/ethan/ARM-Linux/out

echo "\033[32m Start Test... \033[0m"

cd $KOUT
rm mm/memory.o -f
cc_cmd=$@
$cc_cmd > /dev/null 2>&1
reset
fdump mm/memory.o zap_page_range
