# Polychroma 
The weirdest background changer that ever was.

## What is it?
Polychroma is a web application background changer I wrote in 4 hours.

"I'm sorry, did you say **web application** *background changer*?"

Oh no, you heard me right. This is a piece of software which runs on a server and serves a single webpage which contains a background that changes in random order with some nice transitions between them, and a very primitive clock. 

## Why on earth.
Well, necessity is the mother of invention, no?

Polychroma exists because I have a big TV in my room. It's relatively infrequent that I end up using it for anything you'd normally use it for, so to put it to use, I use it as a clock. Previously, this was Windows running on an old laptop with Wallpaper Engine. That old laptop has since died however, and so I decided to swap it out for an old SFF computer I had. It works fine, but didn't have Windows, and buying a Windows license for what amounts to a fancy clock seemed.....dumb. So I threw Linux on it instead, but Wallpaper Engine isn't compatible with Linux. I've used other wallpaper changers but had issues finding one that exactly suited my needs. Having to remotely connect to it is kind of annoying to add or remove backgrounds, so really I wanted something I could access from anywhere.

And thus, Polychroma was born.

Because of this single purpose, Polychroma is very primative. At the end of the day, it's a Django application working with HTMX to swap Jinja templates in and out. There are very few options for customization, only allowing one to add or remove backgrounds, add or remove a clock, and even the clock itself has to be manually positioned with CSS units. It's far from user friendly, but I wrote this for me, and me alone. I doubt that anyone out there could possibly find it useful. That said, I only stand where I am now due to the kindness of strangers on the internet who took it upon themselves to share what they wrote with others. So for those with curious minds, I'm making this available to look at too...even if it is kind of dumb.

## Installation
Polychroma runs in a `pipenv` virtual environment. It can be installed by installing the dependencies in the Pipfile. Once installed, rename `polychroma/settings.py.example` to `polychroma/settings.py`. The configure the file the same way you would a Django site. Once configured, you can add a superuser through `manage.py` in the same way as with a Django site. Finally, running `python ./` starts the web application.