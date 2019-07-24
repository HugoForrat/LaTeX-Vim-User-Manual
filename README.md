# LaTeX-Vim-User-Manual
A reformatting of the Vim user manual using LaTeX.
This is mainly for people who'd like to read the Vim manual cover to cover.
This was done by downloading the html version of the user manual, as they were the 12 July 2019, and converting these html files to tex files with `pandoc`.
Some additional reformating was then done by myself.
The compilation was done using `pdflatex`.
There are probably some mistakes and inconsistencies, feel free to report them me or to make a pull request.

**You can find a pdf version of the document [here](https://github.com/HugoForrat/LaTeX-Vim-User-Manual/releases/tag/v.1.0).**

I've also added a Python script that you can run to generate a version with page numbers instead of hyperlinks.

You can compile the document yourself by running `pdflatex doc.tex`.
You might have to run this command twice to have all the tables of content working.

## Used packages
- hyperref
- longtable
- etoc
- shlashbox
- fancyvrb
- tabularx

*NB* : The etoc package needs to be version 1.9 or higher.

## Adopted conventions
- The document is an article because the conversion with pandoc created articles. This might not be the best choice but eh.
- The title of each file is a `\section`.
- Each file end with a `\clearpage`.
- Numbered parts of a file are `\subsection`.
- Unnumbered parts of a file are `\subsubsection`.
- In a coherent manner with the previous choices, the table of contents found at the beginning of each section is replaced by `\localtableofcontentswithrelativedepth{+1}`.
- Markers delimited in `*` are `\label`.
- In said markers, in a `\` is found it is replaced by the text `backslash` because the `\` isn't authorized inside of `\label`.
- Generally, there's only one sentence by line.
- URL are in the `\url{}` macro.
- The `Verbatim[samepage=true]` environnment is prefered to the `verbatim` one, *especially* for the "ASCII art" figures.

## Main differences with the html version
- In the original Vim manual, link are presented inbetween `|` symbol. Those links can lead to another part of this manual or to the Vim reference manual. It would have been difficult to link the pdf output to the Vim reference manual so I've decided to prefix those links with `:h`. Typing this command inside of Vim should lead to the correct part of the reference manual.
- Some links to the User Manual were represented by the number corresponding to the subsection they were linked to. They're represented here by the title of the subsection instead.
- One subsection in `usr_01` about 'Jumping around' has been deleted because it didn't make sense in the context of this pdf document.
- A small note was written where said subsection was, explaining the differences between the two ways of reading this manual.
- A few typos have been corrected (like missing punctuation or `'` insted of `"`).

## To-do
- Most if not all ASCII art figures could be replaced with Tikz pictures.
- There are plenty of over/underfull boxes when compiling.
- The pieces of codes are not all indented the same way, maybe this could be corrected.
- Frankly, the indentation of the source files is all over the place.

## Licence
This reformatting is distributed under the term of the _Open Publication License_, just as the Vim User Manual itself.
