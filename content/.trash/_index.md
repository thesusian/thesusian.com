---
title: Social
draft: true
---
> social: a living document where I post pictures and updates

## 2025-01-27

I would like to say it was finals, but it was mostly just me. Will try to get back on track. I archived all of the weekly posts as they add so little value, if you are that interested you can see them in the commit history I guess.

Anyway, now go watch this masterpiece of a film.

![Eternal Sunshine of the Spotless Mind](/media/eternal_sunshine.jpg)
*Eternal Sunshine of the Spotless Mind*

----
## 2024-12-14

When watching movies, I notice myself noticing and judging the acting, based on how I assume the director intended. But this time I was seeing something genuine, something real, and beautiful. The director in the subject.

![Close Up](/media/closeup.jpg)

Been a while

----
## 2024-11-15

I want to redesign this whole thing, maybe after exams...

----
## 2024-11-10

Turns out you can use timers and interrupts, I might write a whole post on the `PIC16F887`, but that's for future me to worry about.

Instead of a weekly post this week I will be writing the post about Rate Yildiz, I think I will stick to a "one post a week" till the end of the year, or unitl I start taking this website seriously.

----
## 2024-11-03

There must be a more elegant way to do this

```asm
DELAY_1K
      MOVLW   	D'250'
      MOVWF   	TIMER
LOOP_1K
      NOP
      DECFSZ	TIMER, 1
      GOTO 	LOOP_1K
      RETURN

DELAY_250K
      MOVLW   	D'250'
      MOVWF   	TIMER1
LOOP_250K
      NOP
      CALL	DELAY_1K
      DECFSZ	TIMER1, 1
      GOTO 	LOOP_250K
      RETURN

DELAY_3M
      MOVLW   	D'12'
      MOVWF   	TIMER2
LOOP_3M
      NOP
      CALL	DELAY_250K
      DECFSZ	TIMER, 1
      GOTO 	LOOP_3M
      RETURN
```

----
## 2024-11-02

Rate Yildiz is now [live on Github](https://github.com/thesusian/rateyildiz.com). I will be making it open-source, mainly because I want free labor. I wanted to upload it on the server today but I can't buy the domain for some reason.

----
## 2024-10-27

My bad, no update for you this week...

![in the midst of "it's so over", I found there was, withing me, an invincible "we're so back".](/media/back.png)

----
### 2024-10-20

Picked up Disco Elysium again. How can anyone write such an interdependent game, AND record amazing voice lines for almost every interaction!!

----
### 2024-10-17

I upload these weekly, I should do this more frequently tbh.

> Malkovich. Malkovich Malkovich Malkovich, Malkovich. Malkovich? Malkovich, Malkovich Malkovich. Malkovich! Malkovich? Malkovich Malkovich Malkovich. Malkovich, Malkovich, Malkovich, Malkovich... Malkovich. Malkovich Malkovich, Malkovich. Malkovich? Malkovich, Malkovich Malkovich. Malkovich!

![a screenshot from "Being John Malkovich"](/media/beingjm.jpg)

It was a good movie.

----
### 2024-10-15

Started reading "Notes on the Synthesis of Form", I already read the first two chapters and wrote some notes on it a while ago, now it's a full read.

![a nice image](/media/cleanphoto.jpg)

----
### 2024-10-14

![sunset on the seaside](/media/seaside.jpg)

----
### 2024-10-11

Finally, something good to watch.

{{<youtube h0jT60MBsvc>}}

----
### 2024-10-10

Accidentally stumbled upon [Galeri Eyüpsultan](https://www.instagram.com/galerieyupsultan), a pleasant surprise. They had some abstract art on display.

Check it out, it's free.

![Abstract art at Galeri Eyupsultan](/media/galerieyupsultan.png)

Also, I just finished the PKD's book, it was really good, really really good. I might write something about it.

----
### 2024-10-07

I lied, these are not daily, but who cares.

Started reading PKD's "Flow My Tears, The Policeman Said" since I had it already downloaded on my phone, seems pretty good so far, and it's a nice way to pass time in the metro.

We also have a new project running, a model elevator using the `PIC 16F788` with a remote, for the remote I will be trying to use an `NE555` IC and three push buttons.

Messing around with circuits in Proteus is quite fun.

![A circuit in Proteus](/media/proteus.png)

----
### 2024-10-05

This is inspired by [sizeof.cat](https://sizeof.cat/notes), in fact, me making a website at all is somewhat thanks to him too.

Here are some nice pics I took recently.

![building](/media/airport.jpg)

![airport](/media/building.jpg)
