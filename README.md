# Fact-Checking-Engine-COPAAL
[Project Overview](#project-overview)  | [Installation](#installation) | [How_to_run](#how to run)  | [Techniques](#techniques) | [Contribution](#contribution)

## Project Overview
Fact checker - A Fact Checking Engine  based on Wikipedia corpus , developed using COPAAL approach.

This project aims to validate the veracity of a given triple (s, p, o) using a knowledge graph G and a maximum path length k. It begins by initializing the necessary variables and performing path discovery. Paths are discovered by generating query templates and executing queries to obtain relevant information. Path scoring is then performed by calculating co-occurrence counts and NPMI (Normalized Pointwise Mutual Information) scores. Finally, the veracity of the triple is calculated based on the scores obtained. The algorithm returns a veracity score [0,1] for the input triple.

## Installation

- pip install -r requirements.txt
- You will need Jupyter Notebook

## Techniques
COPAAL (Corroborative Fact Validation) 
An algorithm that aims to validate facts by utilizing information from a knowledge graph and analyzing the co-occurrence and distribution of related entities.

## Contribution:

| Name                  | Matriculation Number |
| --------------------- | -------------------- |
| Amal Nimmy Lal   |   6987112            |
| Aryman Deshwal   |  4011205           |
