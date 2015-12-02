#!/bin/bash
chromium --app=https://www.youtube.com/ & sleep 10 && terminator --command='echo "Enter duration to watch (format is any combination of: _h _m _s):" && read duration && sleep "$duration" && killall -SIGKILL chromium'
exit
