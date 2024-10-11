# Code Completion Analysis

This repo contains the results of an analysis of code completion with the Fill-in-the-Middle objective.

Link to the analysis:
<a href="https://colab.research.google.com/github/julia-lukasiewicz-pater/code-completion-analysis/blob/main/code_completion_analysis.ipynb" target="_blank" style="border:none; background:none; padding:0;"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> 

## Structure of the repo:

- `scripts/`: Includes the script used to preprocess a dataset
- `data/`: Includes zip files with raw and preprocessed datasets
- `code_completion_metrics - metrics.zip`: csv file containing the results of the analysis
- `code_completion_analysis.ipynb`: analysis
- `requirements.txt`: packages needed to run the script

## Structure of the dataset:

The dataset consists of 45 short Python programs that I developed in the past. Each program solves a problem from the online course Data Structures and Algorithms from Profound Academy. The files are organized into categories based on whether they include a function and/or a comment that describes the problem being solved. The content of each processed file has been divided into three sections: prefix, middle, and suffix. The middle section begins at the line that represents 60% of the total line count.
