# whatsapp-messager

the legends on stackoverflow and our favourite chatgpt helped me fix the errors in session 3

session 1:
Trying to make an automated whatsapp messenger

session2(only 5 minutes):
I am unable to fix the code :(

session3:
I fixed the code less goooo. db is now connecting but the message is not being sent :(
i think i have to change XPATH

session4:
fixed the XPATH, messages are now being sent. but the problem is they are not being removed from the db. fixing that in the next session....

session5:
everything fixed, code works, database is now being updated


https://github.com/user-attachments/assets/b3b168d1-157c-4fd6-b65d-46daaa409b47



https://github.com/user-attachments/assets/9f2d6a71-a959-4e84-a8d9-8b09e82d1329

This script utilizes microsoft sql server and web whatsapp to send messages autonomously. first, a database is to be created and the name is to be entered into DATABASE variable. connection details are to be put in the other 3 fields. The code will run and check for the table specified, in which the bit sentStatus is NULL, which means the message is yet to be sent, thus it selects all the rows one by one, and sends the message on whatsapp to the receiver, whose phone number is given in the receiver column in our db. The string in messagetxt column is the message which is being sent.

After the message is Sent, the sentStatus bit is sent to 1(0 is also fine). this is done so that the same message is not sent repeatedly when code is re-ran. the script only stops when all the remaining messages are sent, or is interrupted by the programmer. 

how to use:
put all the credentials in, the database name, and create a table named WhatsAppMessages, and insert some rows, and you are ready(you might need to change firefox user setup and XPATH yourself).

I put the updated and the sentdttm columns because i thought that i might make it more, but now i dont want to make it bigger, so they are all NULL.....

