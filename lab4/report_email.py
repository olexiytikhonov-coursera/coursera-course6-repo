#!/usr/bin/env python3

import reports
import os
import emails
from datetime import date

def make_processed_body(basepath):

    folder = os.listdir(basepath)
    paragraph = ""

    for file in folder:
        with open(basepath + file, 'r') as f:
            paragraph += "name: " + f.readline().rstrip("\n") + "<br/>"
            paragraph += "weight: " + f.readline().rstrip("\n") + "<br/><br/>"

    return paragraph


if __name__ == "__main__":
    # code that runs only when the file is executed directly

    today = date.today()
    formatted = today.strftime("%B %d, %Y")
    title = "Processed Update on " + formatted
    basedir = os.getcwd() + '/supplier-data/descriptions/'
#    basedir = os.path.expanduser("~") + '/supplier-data/descriptions/'
    paragraph = make_processed_body(os.getcwd() + '/supplier-data/descriptions/')
    attachment = "processed.pdf"
#    attachment = "/tmp/processed.pdf"

    reports.generate_report(attachment, title, paragraph)

    # Send the email
    sender = "automation@example.com"
    receiver = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, attachment)
#    emails.send(message)
