---
title: "Advanced programming in Python"
subtitle: "Lecture 12: Python in Natural Language Processing"
author: "Arianna Masciolini"
theme: "lucid"
logo: "gu.png"
date: "5 December 2023"
institute: "Chalmers/GU CSE (DAT515/DIT515)"
---

## Who
- PhD student in Natural Language Processing (or Computational Linguistics, or Language Technology...)  <!--most of you know me from lab sessions/tutorial classes, but outside of this course...--> at Språkbanken Text, GU
- particularly interested in:
  - computational syntax
  - Computer-Assisted Language Learning <!--so today we're gonna do both!--> \pause
  - Swedish <!--as a learner-->

## What
We are going to build a mini Python application to practice Swedish syntax (adverb placement)<!--and the reason why I chose this is a bit autobiographical, because I often misplace adverbs myself-->, but...

\bigskip

![](fail.jpg)
\footnotesize \centering "We don't have time to build a proper GUI"

## How
With __Part-Of-Speech annotation__ and __dependency parsing__:

![](tree.png)

<!--here I could talk a lot but I will only give you the basics, also because this is not the annotation format I am most used to. The things in the colorful blobs are POS tags, for instance... and the arrows indicate relations between words. They are also labelled, but we don't care-->

## How
With __Part-Of-Speech annotation__ and __dependency parsing__:

![](tree_minimal.png)

<!--actually we can disregard most things. Just remember AB = adverb, in this case referred to or modifying the verb "hinner"-->

## How
<!--so we take away the adverb, highlight the word they are referred to and ask the learner to place them in the correct spot-->
With __Part-Of-Speech annotation__ and __dependency parsing__:

![](wrong.png)

## How
With __Part-Of-Speech annotation__ and __dependency parsing__:

![](correct.png)

## Libraries
<!--one of my favorite things about Python (and one of the reasons it became the lingua franca not only of NLP but of AI and ML in general) is that there is a library for every single thing-->
- [__python-korp__](https://github.com/mikahama/python-korp), a wrapper for the [Korp](https://spraakbanken.gu.se/korp/) API, to retrieve linguistically pre-annotated sentences from large Swedish corpora
- [__Spacy__](https://spacy.io/), a widely used NLP library, to annotate our own sentences

# Let's build something! <!-- - Korp tour (incl. utökade queries) - Korp API - Korp notebook - basic app building - Spacy notebook - Spacy adaptation-->

## In conclusion
2h prototype of a language learning app:

- code: [`github.com/harisont/advpy_nlp`](https://github.com/harisont/advpy_nlp)
- possible extensions:
  - GUI
  - other POS/dependency relations (customizable queries)
  - other languages (with Universal Dependencies)
  - ...

## To learn more
- Korp user manual: [`spraakbanken.gu.se/en/tools/korp/user-manual`](https://spraakbanken.gu.se/en/tools/korp/user-manual)
- Official Spacy website: [`spacy.io`]((https://spacy.io/))
- <!--and last but not least-->Aarne's Computational Syntax course