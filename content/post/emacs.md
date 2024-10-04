---
date: 2023-10-03
title: Emacs
tags: [notes]
draft: true
---

I started learning Emacs because I wanted to learn lisp, so here we are

## Navigate files
* `C-v` Page up
* `M-v` Page down
* `C-l` Move page so cursor is in the center
* `C-f` Forward 1 letter
* `C-b` Backward 1 letter
* `M-f` Forward 1 word
* `M-b` Backward 1 word
* `C-n` Next line
* `C-p` Previous line
* `C-a` Start of line
* `C-e` End of line
* `M-a` Start of sentence
* `M-e` End of sentence
* `M-<` Start of file
* `M->` End of file
* `C-d` Delete next character
* `M-<DEL>` Kill previous word, <DEL> being Backspace
* `M-d` Kill next word
* `C-k` Kill from cursor to end of line
* `M-k` Kill from cursor to end of sentence
* `C-<SPC>` Set a marker <SPC> being the spacebar
* `C-w` Kill all text between the marker and the cursor
* `C-y` Yank back killed text
* `M-y` Select which text to yank from killed text GLORIOUS!!
* `C-/` Undo

> Killing text is like cutting, you can yank (paste) it back, deleted text however is not copied, usually commands that remove 1 character do delete text, not kill it

## Meta
* `C-u` Repeat cout
* e.g. this moves forward 8 letters `C-u 8 C-f`
* with `C-l`, `C-u 8 C-l` moves the screen so that 8 lines are above the cursor
* `C-g` Stop running command

## Windows
* `C-x 0` Kill current window
* `C-x 1` Keep only the current window and kill the rest
* `C-x 2` Split horizontally
* `C-x 3` Split vertically

## Slime (idk if specific to it)
* `C-c C-c` runs `slime-compile-defun`
* `C-c C-x` Switch to REPL using the file you just compiled
* `C-c C-l` Load a file
* `C-c C-k` Compile and load compiled file
