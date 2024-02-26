# graylog_script_callback
Parse values from Graylog-Backlog-Messages to use this information and call a custom script with these values.


Step 1:
Copy the parser-script (argv_parser.py) to your graylog-script directory and edit the script to match your fields in which the values are found.
Edit the actions in parser-script to call your actual action (the mail_to_user.sh is a nice Template for this).

Step 2:
Define a Script-Notification in Graylog with Scriptpath to the argv_parser.py, Script argument is the name of your actual action-script. (in this case: "mail_to_user")

Step 3:
Define an Event in graylog-interface with backlog-messages (most commonly 1 Backlog-message)
In this event use the created Notification (argv_parser.py with argument to action-script)

Step 4:
Test the callback and check graylog-server.log to get information about the called scripts.

Step 5:
Enjoy your custom action with values from backlog-message.



We use this script since many years and everything works great. - Since Graylog-Forum deleted my post (i think they want to implement this feature into enterprise and dont want users to get it without business license) i create this repo.
Open Source and sharing solutions 4ever

Best regards,
Coffee_is_life
