import imaplib

msrver = imaplib.IMAP4_SSL('imap.gmail.com:993')

msrver.login('nesac128@gmail.com', 'Tiresias41812')

stat, cnd = msrver.select('Inbox')