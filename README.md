# AnalysisAttack
Spring 2023 network security project

## What do we do?
First we encrypt a text by substitution cipher. Then we count the number of letters in some books. Also do it for some combination of letters like '__the__', '__and__', '__th__', '__in__', '__ing__', '__ee__', etc.

Then we do same on cipher text and count letters and all combinations of the cipher text, then we compare two analisyses and find the real value of each cipher letter.

## Summary of files 

### Encrypter
Encrypt the text and give us a cipher text.

### CounterOfBooks
In this file we count the letters and combination by __PyPDF2__ and plot some giagrams to show the percentage and relation of letters and combinations.

### CounterOfCipherText
Do the same as above on cipher text but the point is that we don't know what combinations we should count so we count all of combinations.

### Decrypt
By analisys the cipher text and compare with analisys of books attempt to decrypt the cipher text and exchange the letters by a function.
