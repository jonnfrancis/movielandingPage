# **BingPot** - A Movie landing Page

## Project Overview

**Project Name:** Bingpot

**Project Active:** 2020 - 2021

**Client:** Self

# What is BingPot?
![BingPot logo](movie/static/movie/img/logo1.png)

BingPot is a movie landing page that I came up with. I am not sure why but I thought it would be funny so I just decided to lean into it while I was thinking up the name for my site. This webpage is created using python in the backend and html, CSS and Javascript in the front end. it is also responsive with other devices including phones and tablets.

# What makes BingPot different?
## Distinctiveness and Complexity
What makes Bingpot a one in a million webpage is the balanced use of all the libraries I brought on  board mainly: 
* Jquery 3.4.1
* Bootstrap
* owl Carousel

This are just a few of the many dynamic online css and javascript libraries I decided to use. but that is not all that makes BingPot complex. it has a good finish with a good combination of colors but not so much that it becomes overbearing. the colours combine "just right". Also with the help of the following libraries I ensured that the smooth icons and the well shaped fonts joined together and left the website looking like a masterpiece.
* Bootstrap
* Boxicons

After seeing all this I am sure you want to know more about this site. I know ;) don't worry about it because I am about to break down everything for you. Now my webpage is based solely on movies, shows and anime. I needed to have access to all these so I looked for an api that had access to all these. That was when I bumped into the OMDB api and placed a few api calls in my javascript and connected it to my search input field.

I was having some trouble at the beginning and decided I need a debugger so I used this:

`$ python -m pip install django-debug-toolbar`

but after finishing my project I removed it from the project.

In total, I have:
1. 7  templates
2. 1 style sheet
3. 1 script file

I will be going through all of these files contents, why I made the decisions I made, and how the contents contribute to the overall greatness of the page.
### Style sheet(styles.css)
This file contains all the styles for the entire webpage that I used. Everything from position to background of elements are contained in this file. also the responsive for different devices is contained here. 
### Script file(script.js)
This javascript files conains a lot from the api calls to the omdb website to carousel that are present in the index.html file. it also contain settings for the trailer toggle in page.html
### index.html
This is the first page you will see once you open the site. It is where all the magic happens. once you open it you will be greeted by a neat carousel that shows a bunch of random movies and their information. this page is the page containing a lot of information. it is the site's main page. 
### layout.html
Contains the layout for the entire webpage. mainly the navbar and the search bar. once you click on the search bar you can search for any movie and it will make an api call and return with all the movies with the title you just typed.
### page.html
Once you click onto any movie in the site, you will be directed based on its id to this page where there is a trailer and going deeper into the movies themselves. from actors to the director.
### wait.html
This is only in the pages that haven't been made yet. though rarely there are some pages that couldnt be made. not yet anyway.
### actors.html, categories.html and directors.html
These are pretty much the same page with different contents it shows a list of either actors, categories or directors.
