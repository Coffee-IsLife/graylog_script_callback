#!/usr/bin/env python2
### argv_parser to read values from gralog-backlog  -  Needs to be located in graylog-script-dir

from __future__ import print_function
import json
import sys
import subprocess

logfile = "/tmp/script-notification.log"
graylog_scriptdir= "/usr/share/graylog-server/scripts/"

# Main function
if __name__ == "__main__":

    # Print out all input arguments.
    action = sys.argv[1]
    f = open(logfile, "a")
    f.write("Action: " + action + "\n")
    for i in sys.argv[2:]:
      f.write("Arguments: " + i + "\n")
    f.close
    # Turn stdin.readlines() array into a string
    std_in_string = ''.join(sys.stdin.readlines())


    # Load JSON
    event_data = json.loads(std_in_string)

    # Extract Message Backlog field from JSON.
    f = open(logfile, "a")
    f.write("\nBacklog:\n")
    arg_string=""
    for message in event_data["backlog"]:
      ###  You need to define the Fields in which you get the Values from graylog-backlog-message - With these values you can call a custom script to do whatever action you like
        try:
          f.write("custom once to: " + message["fields"]["to"] + "\n")
          my_to = message["fields"]["to"]
          arg_string+='-t \'' + my_to + '\' '
        except:
          pass
        try:
          f.write("custom once From: " + message["fields"]["From"] + "\n")
          my_ES_From = message["fields"]["From"]
          arg_string+='-f \'' + my_ES_From + '\' '
        except:
          pass
        try:
          f.write("custom once from: " + message["fields"]["from"] + "\n")
          my_from = message["fields"]["from"]
          arg_string+='-f \'' + my_from + '\' '
        except:
          pass
        try:
          f.write("custom once MailAction: " + message["fields"]["MailAction"] + "\n")
          my_mailaction = message["fields"]["MailAction"]
          arg_string+='-m \'' + my_mailaction + '\' '
        except:
          pass
        try:
          f.write("custom once Reason: " + message["fields"]["reason"] + "\n")
          my_ES_reason = message["fields"]["reason"]
          arg_string+='-r \'' + my_ES_reason + '\' '
        except:
          pass
        try:
          f.write("custom once Return: " + message["fields"]["ReturnMessage"] + "\n")
          my_returnmessage = message["fields"]["ReturnMessage"]
          arg_string+='-r \'' + my_returnmessage + '\' '
        except:
          pass
        try:
          f.write("custom once blocked: " + message["fields"]["BlockedFile"] + "\n")
          my_blocked_file = message["fields"]["BlockedFile"].replace('"', '')
          arg_string+='-b \'' + my_blocked_file + '\' '
        except:
          pass
        try:
          f.write("custom once Time: " + message["timestamp"] + "\n")
          my_time = message["timestamp"]
          arg_string+='-z \'' + my_time + '\' '
        except:
          pass
        try:
          f.write("custom once To: " + message["fields"]["To"] + "\n")
          my_ES_To = message["fields"]["To"]
          arg_string+='-t \'' + my_ES_To + '\' '
        except:
          pass
        try:
          f.write("custom once ConnectIP: " + message["fields"]["connectingip"] + "\n")
          my_ES_connectionIP = message["fields"]["connectingip"]
          arg_string+='-c \'' + my_ES_connectionIP + '\' '
        except:
          pass
        f.close

    if action == "mail_to_user":
      f = open(logfile, "a")
      f.write("Start action: " + action + "\n")
      #script = '/usr/share/graylog-server/scripts/' + action + '.sh ' + ' -a \'' + action + '\' -t \'' + my_to + '\' -f \'' + my_from + '\' -m \'' + my_mailaction + '\' -r \'' + my_returnmessage + '\' -z \'' + my_time + '\' -b \'' + my_blocked_file + '\''
      script = graylog_scriptdir + action + '.sh ' + arg_string
      f.write("cmd_line: " + script + "\n")
      rc = subprocess.Popen(script, shell=True)
      f.write("============================================" + "\n")
      f.close
    if action == "mail_to_user_batv":
      f = open(logfile, "a")
      f.write("Start action: " + action + "\n")
      script = graylog_scriptdir + action + '.sh ' + arg_string
      f.write("cmd_line: " + script + "\n")
      rc = subprocess.Popen(script, shell=True)
      f.write("============================================" + "\n")
      f.close

    # Return an exit value. Zero is success, non-zero indicates failure.
    exit(0)
