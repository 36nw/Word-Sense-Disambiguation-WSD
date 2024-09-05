
# scorer.py

# Import libraries
import sys
import nltk
import pandas as pd
import scipy
from nltk.metrics import ConfusionMatrix

def main():
    logger.info("Starting the scorer.py script")

    output_file = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/my-line-answers.txt"
    key_file = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/line-answers.txt"

    with open(output_file) as file:
        f1 = [line.rstrip('\n') for line in file]
        var1 = [i.split(':"', 1) for i in f1]
        predicted = {}

    for a in range(1, len(var1)):
        key = var1[a][0]
        value = var1[a][1]
        predicted[key] = value

    predicted_list = []
    for v in predicted:
        predicted_list.append(predicted[v])

    with open(key_file) as myf1:
        f2 = [line.rstrip('\n') for line in myf1]
        var2 = [i.split(':"', 1) for i in f2]
        observed = {}

    for a in range(1, len(var2)):
        key = var2[a][0]
        value = var2[a][1]
        observed[key] = value

    observed_list = []
    for v in observed:
        observed_list.append(observed[v])

    cm = ConfusionMatrix(observed_list, predicted_list)
    x = 0
    for i in range(len(predicted_list)):
        if predicted_list[i] == observed_list[i]:
            x += 1
    accuracy = (x / len(predicted_list) * 100)

    print('Accuracy of the classifier is:', accuracy, '\n\n''Confusion Matrix: ', str(cm))

    logger.info("Finished running the scorer.py script")

if __name__ == '__main__':
    main()
