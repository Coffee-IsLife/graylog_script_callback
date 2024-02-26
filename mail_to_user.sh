#!/bin/bash
##actual callback, called from argv_parser
### This script depends on the package "mutt" - but you can use whatever command you need 

###  EDIT REAL NAME in Mail-command
###  EDIT FROM ADDRESS in Mail-Command

while getopts f:t:m:r:b:z:a: option; do
  case "${option}" in
        a) action=${OPTARG};;
        m) mailaction=${OPTARG};;
        t) to=${OPTARG};;
        f) from=${OPTARG};;
        r) returnmsg=${OPTARG};;
        b) blocked_file=${OPTARG};;
        z) my_time="$(date -d "${OPTARG}" +'%d-%m-%Y %H:%M')";;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Unimplemented option: -$OPTARG" >&2; exit 1;;
  esac
done


echo -e "
Title:\t\tMail from $from blocked

When:\t\t${my_time}
From:\t\t${from}
To:\t\t${to}
Attachment:\t\t${blocked_file}

Returnmessage:\t${returnmsg}


Best regards,
IT-Team

" >> /tmp/$$_mailtext.txt

mutt -e 'set content_type="text/plain" charset="utf-8" realname="Noreply" from=noreply@mydomain.com' $to -s"Mail was $mailaction" < /tmp/$$_mailtext.txt

rm -f /tmp/$$_mailtext.txt
