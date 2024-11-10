---
date: 2024-11-10
title: "Rate Yildiz"
tags:
  - university
math: false
description: Find the best teacher for you
---

After so long, it's finally here, with a stitched-together design and a search that doesn't work for Turkish letters

## The Website

You can find it at [rateyildiz.com](https://rateyildiz.com), I did a quick research over which domain registrar is the best and after asking around I figured Porkbun was the best option, I like services that are good at doing one thing well.

The server setup is minimal, just a Python script running the whole thing, there is too much redundant stuff in the deployment and development scripts so I have to clean them up soon, in fact I have to clean up the whole thing, I bet I can take the line count down to around 70% or less, or at least I will make it more elegant.

## The Server

The whole thing is opensource, if you prefer reading code check it out on the [Github repo](https://github.com/thesusian/rateyildiz.com)

My main goal with this project was to get something out there as soon as possible, this is my first public project so I didn't want to get stuck in the loop of "this is not good enough", I wanted to make it so fast that I wouldn't have time to think about it.

The application is simply a FastAPI server with Jinja templates, that simple. I had some experince with Flask before and I remeber seeing a post on X on how FastAPI uses 80% less ram than Flask so I chose it. Also the fact that it's asyncronus by default was a huge plus.

## The Code

This accedentally turned into an expirement of how good Claude is at writing code, it it's surprizingly good, specially with a small code base where I could feed everything in with less than 20K tokens, it felt like having a really fast co-programmer, I was mostly just corinating the project while Claude was doing all the work. What motivated this too is the generous free trial that [Zed](https://zed.dev/) gives you, I don't know how long it lasts but at this point I'm afraid to ask, it has been working for so long that I don't want to ask.

## Conclusion

Thanks for reading this very detailed and thoughtful post I wrote while half asleep. Go rate some teachers.
