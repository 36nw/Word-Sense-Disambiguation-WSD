# Word Sense Disambiguation (WSD)

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Data](#data)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project implements a Word Sense Disambiguation (WSD) system using a decision list approach. The system disambiguates the sense of a word based on its context using feature functions and probability calculations. The implementation is done in Python and leverages libraries such as `nltk`, `BeautifulSoup`, and `pandas`.

## Files

- **`decision-list.py`**: Main script for creating a decision list and performing WSD on test data.
- **`scorer.py`**: Script for evaluating the performance of the WSD system by comparing predictions with gold standard answers.
- **`decision-list-log.txt`**: Log file for recording the decision list processing details.

## Dependencies

- `nltk`
- `BeautifulSoup`
- `pandas`
- `scipy`
- `logging`
- `re`

Install the required Python libraries using pip:

```bash
pip install nltk beautifulsoup4 pandas scipy
```

## Usage

**1. Prepare Input Files**

* Training XML File: line-train.xml
* Testing XML File: line-test.xml
* Gold Standard Answers: line-answers.txt

Ensure these files are placed in the correct directory and update the file paths in the scripts accordingly.

**2. Run Decision List Script**

Execute the decision-list.py script to create the decision list and perform sense disambiguation on the test data:

```bash
python decision-list.py
```
This script will generate two output files:

* my-decision-list.txt: Contains the decision list with attribute probabilities.
* my-line-answers.txt: Contains the predicted senses for each test instance.

**3. Evaluate the Predictions**

Run the scorer.py script to evaluate the predictions:

```bash
python scorer.py
```
The script will print the confusion matrix and the accuracy of the predictions.

## Algorithm

**1. Feature Extraction:** Define feature functions to extract patterns from text and associate them with senses.
**2. Probability Calculation:** Calculate the probability of attributes occurring in different senses and generate a decision list.
**3. Prediction:** Use the decision list to predict senses for test data based on extracted features.
**4. Evaluation:** Compare the predictions with gold standard answers using a confusion matrix.

## Data

The project involves working with XML files containing training and testing data for word sense disambiguation. These XML files should be structured according to the following specifications:

### XML File Structure

- **Training XML**: Contains annotated data with multiple senses for various words. Each entry in the file includes:
  - `instance`: A unique identifier for the word sense instance.
  - `senseid`: The identifier for the sense of the word in the instance.
  - `context`: Contextual information surrounding the word.

- **Testing XML**: Contains data for which senses need to be disambiguated. Each entry includes:
  - `instance`: A unique identifier for the word sense instance.
  - `context`: Contextual information surrounding the word.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

NLTK and BeautifulSoup libraries for text processing.
Original WSD algorithms for reference and implementation guidance.
For any questions or feedback, please open an issue on this repository or contact the author.
