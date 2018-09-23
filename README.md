# nlp-18-gudlucsam ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

NLP-18-GUDLUCSAM is a Python program for peforming sentiment analysis. This project repo is for my natural language processing class at Ashesi. [link-to-github-repo](https://github.com/gudlucsam/nlp-18-gudlucsam)

## Installation

### Requirements
* Linux or Windows
* Python 3 and up

### Setup
* clone this repo to have it locally

## Usage

### Running on Jupyter notebook

* Open Jupyter notebook in your clone directory.
* Navigate to: project1-naive-bayes/my-naive-bayes/my_naive_bayes.ipynb

```
mdl.naive_bayes_classifier("path-to-doc") # provide document to perform the sentiment analysis on. # uses "../sentiment-labelled-sentences/newdoc.txt" by default.
```

### Running On Command-line

* Navigate to: project1-naive-bayes/my-naive-bayes/my_naive_bayes.py on cmd

```
# run this to ensure everything is working
python my_naive_bayes.py "../sentiment-labelled-sentences/newdoc.txt" 

python my_naive_bayes.py -h # provides help on how to run this on the command-line

--outfile "path-to-output-file"
--accuracy "path-to-labelled-testdata" # to compute accuracy with this testdata
```

### Other Command-line Argument

* --outfile "path-to-output-file" : writes computed labels to this output-file. defaults to "../sentiment-labelled-sentences/result.txt"
* --accuracy "path-to-labelled-testdata" : to compute accuracy with this testdata. calculates accuracy with 30% of training dataset as default testdata.

## Development

* No external python package or module was used.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
