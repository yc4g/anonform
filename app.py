#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, session, \
abort, url_for
#from lxml import html 
from twilio.rest import Client

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = "ACf211000f1e2bdf7ad833b9eaf541dc75"
# Your Auth Token from twilio.com/console
auth_token  = "5a6ab79b242b9d4fdc8a3ea22d3f4a7a"
client = Client(account_sid, auth_token)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms")
def sms():
	
	message = client.messages.create(
	    to="+19292849804",
	    from_="+15005550006",
	    body="This is the ship that made the Kessel Run in fourteen parsecs?")
	return "Message Sent!" + message.sid



'''
@app.route("scrap")
def scrap():
	page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
	tree = html.fromstring(page.content)
	#This will create a list of buyers:
	buyers = tree.xpath('//div[@title="buyer-name"]/text()')
	#This will create a list of prices
	prices = tree.xpath('//span[@class="item-price"]/text()')
	print 'Buyers: ', buyers
	print 'Prices: ', prices


'''

if __name__ == "__main__":
    # Change the host and port name if you want. The default config is port 
    # 5000 on localhost, which you can access by pointing your browser to
    # `localhost:5000`, `127.0.0.1:5000`, or `0.0.0.0:5000`.
    app.run(host='0.0.0.0', port=5000)
