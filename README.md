## Overview
I know I said during the tech meeting that both tech teams would be working on
the same project and each do roughly half the work, but I changed my mind.
We're going to have both of the teams do the same project, but it's going to be
a simpler project than originally discussed. Instead of a forum, which would
involve data storage in a database on a server, we're just going to create an
anonymous form that will send a SMS text to a number every time someone submits
the form. This way, everyone will get the same amount of exposure to the
various technologies we'll use. And in the end, we can see whose looks better
;) 

### Stack
When you access a website online, you're pinging a certain URL after you type
it into the URL bar. A DNS resolver checks if the URL resolves to a valid IP
address, which is the way that the server your website's code is on knows that
someone is trying to view that website. The server "serves" the associated web
page content if it is. We're going to be making a local web app (that is, it's
not going to be live on the Internet) so we don't need to deal with web hosting
and domain names and all of that. What we do need to do, however, is host a
server to "serve" the web app files. We'll use Flask to do that. Flask is a
minimal, low-overhead Python framework that helps structure and host web apps.

The frontend is going to be raw HTML/CSS/JavaScript, but we'll use a UI library
to make the form pretty. [Semantic UI](https://semantic-ui.com/) is a
component-based HTML framework that eliminates a lot of the really low-level
raw element creation that web developers used to have to do with their own
hands. You can choose to use this, or the vast variety of other frontend
frameworks there are out there, like [Purecss](https://purecss.io/),
[mui](https://www.muicss.com/), [Bootstrap](http://getbootstrap.com/), etc.

We'll use the [Twilio](https://www.twilio.com/) API to send a SMS every time
the form is properly filled out and submitted. To make things a little more
interesting, we'll also scrape [this
page](http://echenran.pythonanywhere.com/c4gdata) from the Flask server and
randomly attach one of the recipient + message pairs on the page to the text.

## Getting Started

### Installation
Install flask using the Python package manager, pip. You already have pip if
your machine's version of Python is Python 2 >=2.7.9 or Python 3 >=3.4.
Otherwise, install pip using the instructions found
[here](https://pip.pypa.io/en/stable/installing/).
```$ pip install Flask```

### Files

In this repo is a skeleton Flask server, `app.py`, to give you a basic sense
of how things should be laid out. Right now, this repo is empty, but once
everything is set up your directory should end up looking something like this:  
.  
├── .gitignore  
├── README.md  
├── app.py  
├── scrapethatpage.py  
├── funpythonfiles.py  
├── static  
│   ├── somefile.pdf  
│   └── staticfile.js  
│   └── infoinfoinfo.txt  
└── templates  
    ├── index.html  
    └── styles.css  

All the Python server files should be at the root directory. The `static` and
`templates` folders are special folders that Flask will serve for different
purposes, so don't name them anything else. The `static` folder should contain
files that contain pure information and that you don't expect to change (for
example, maybe the scraped messages from [this
link](http://echenran.pythonanywhere.com/c4gdata) that I mentioned earlier
should live here--hint hint). The `templates` folder should contain all your
frontend files.

### Running the app
If the code that launches your server is in `app.py`, you can host it by doing
``python app.py``
or just
``./app.py`` if you have Python in your path (check by running `echo $PATH`)
and don't delete my shebang in the file (it's the first line that says
`#!/usr/bin/env python`). If successful, you should see something like 
```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
Now, go to http://localhost:5000/ or http://0.0.0.0:5000/ or
http://127.0.0.1:5000/ (they're all the same) in your favorite Google Chrome 
browser, and if everything worked out, you should see your server print out 
something like
```
127.0.0.1 - - [02/Oct/2017 01:41:01] "GET / HTTP/1.1" 200 -
```

### You may be wondering
- [How do I scrape that page with the messages?](http://docs.python-guide.org/en/latest/scenarios/scrape/)
- [How do I get all the files in this repo onto my computer?](https://help.github.com/articles/fork-a-repo/)
- [How do I set up my SSH keys so I can push/pull to the remote repo without having to enter my password every damn time?](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Can I see an example of a fully fleshed out Flask app?](https://github.com/pallets/flask/tree/master/examples/flaskr/)
- [How do I navigate code in Vim, the greatest editor known to humankind?](https://vim-adventures.com/)

### Still unsatisfied?
[Email me](mailto:ecr.chen@yale.edu) if you want help / more deets. Have fun!
