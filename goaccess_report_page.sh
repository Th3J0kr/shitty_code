#!/bin/bash

goaccess /var/log/apache2/purpleteamsec.com-access.log --load-from-disk --keep-db-files --time-format %H:%M:%S --real-time-html -o /var/www/www.purpleteamsec.com/public_html/goaccess/status.html

