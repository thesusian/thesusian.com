---
date: 2024-01-27
title: Unsplash Profile Scrapper
tags: [programming]
---

[(Github)](https://github.com/thesusian/UnsplashProfileScrapper)

did you ever just sit someday and say "man I wish I could download an entire Unsplash account without rate limits"
well guess what? **Now You Can!**
but in all seriousness, isn't it weird that no one has wrote something like this and released it on Github, I spent an entire **7** minutes trying to find such a thing but I couldn't, so instead of searching for an extra 7 minutes (I would have probably found something) I decided to make my own!

## A Simple wget

yes I'm going to make an entire post out of 100 lines of code in python

so, it all started on the noon of 2022-09-04 Sun, it was a windy day, but I didn't care. "well, all I have to do is download the page and extract the links, right?" haha how foolish was I, but it actually worked at the start, my target profile had 20 pictures (which no that I think about it I could have just downloaded them manually and I would have been done), all I did was download the page and extract all the links, then extract the links with a specific pattern

you see that worked perfectly until I tried to download another profile, one that had more than 20 pics, if you go to an Unsplash profile with more than 20 pics and scroll down, you will find that little small tiny cute <button onclick="alert('yes I do get clicked')">button</button>

## Enter: [Selenium](https://www.selenium.dev/)

did you know that you can control an **Entire Web Browser** from your python code, now that I say it out loud (or write it lol) it seems obvious

so with this selenium thing (btw it's a [chemical element](https://en.wikipedia.org/wiki/Selenium) apparently) you can simulate an entire web browser and do whatever you want with it, you can scroll, input text, press buttons, and may other things that you can do in a browser, so with this beautiful thing's help I was finally able using my professional hacking techniques (I will explain in the next segment) to successfully load and get the links of all the pictures in a given profile

## My Professional Hacking Techniques

so here are the steps to load all the pictures in an Unsplash account

- load the page
- delay (wait for the page to load)
- scroll down and press the "Load more photos" button
- delay (wait for the bottom to do something)
- scroll down a lot (2000px)
- delay (wait for images to load)
- scroll up a bit (if you hit the butom images wont load)
- delay (wait for more images to load)
- repeat the last 4 steps until you load all the images
- download pictures :)

## What did we learn

web scrapping is so much fun, you feel like you are cheating the website by not using their way of accessing stuff, **UNLIMITED POWER**
