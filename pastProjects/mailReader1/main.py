# this tells the numberof unread emails and details about them
import poplib
import email
from email import parser
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('aviralji4@gmail.com')
pop_conn.pass_('up32ad4885')
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
messages = [b"\n".join(mssg[1]) for mssg in messages]
messages = [email.message_from_bytes(mssg) for mssg in messages]
print(str(len(messages)) + " New EMails... in Inbox.")
for message in messages:
    print("Recieved on - " + message['Date'])
    print("From - " + message['From'])
    print("Subject - " + message['Subject'])
pop_conn.quit()
