
# decision-list.py

# Import libraries
import re
import sys
from bs4 import BeautifulSoup
import math

# Input files
TRAIN_XML = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/line-train.xml"
TEST_XML = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/line-test.xml"
OUTPUT = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/my-decision-list.txt"
OUTPUT_ANSWERS = r"/Users/mugeyalcin/Desktop/GMU/AIT 526/line-data/my-line-answers.txt"

def feature_set():
    # Define feature functions

    # Example:
    def vote_feature(line):
        return bool(re.search(r'vote', line)), 'phone'
    yield vote_feature

    def growth_feature(line):
        return bool(re.search(r'growth', line)), 'phone'
    yield growth_feature

    # Add more feature functions as needed

def probability(attribute, sense_text, other_text):
    count1 = 0
    count2 = 0

    for line in sense_text:
        if line is not None and attribute(line)[0]:
            count1 += 1

    for line in other_text:
        if line is not None and attribute(line)[0]:
            count2 += 1

    total_count = count1 + count2
    prob1 = count1 / total_count
    prob2 = count2 / total_count

    try:
        ratio = math.log10(prob1 / prob2)
    except ZeroDivisionError:
        ratio = 1

    with open(OUTPUT, 'a+') as output:
        output.write(f'{attribute.__name__}\t{ratio}\t{sense_text[0][1]}\n')

    logger.info(f'Attribute: {attribute.__name__}, Ratio: {ratio}, Sense: {sense_text[0][1]}')

    return ratio

if __name__ == '__main__':
    logger.info("Starting the decision-list.py script")

    with open(TRAIN_XML) as f:
        data = f.read()

    parser = BeautifulSoup(data, 'xml')

    attribute_list = []

    # Create an attribute list by identifying patterns from line-train.xml and associate attributes with sense
    for feature in feature_set():
        attribute_list.append(feature)

    textsense1 = []
    textsense2 = []

    # Read the XML file into training argument
    for instance in parser.find_all('instance'):
        if instance.answer['senseid'] == 'phone':
            for tag in instance.find_all('s'):
                string = tag.string
                textsense1.append(string)
        else:
            for tag in instance.find_all('s'):
                string = tag.string
                textsense2.append(string)

    # Calculate probability for each attribute in the corpus
    for attribute in attribute_list:
        probability(attribute, textsense1, textsense2)

    # Sort the attributes accordingly based on their probability scores and create a decision list
    attribute_list.sort(key=lambda attribute: probability(attribute, textsense1, textsense2))

    phone_count = len(parser.find_all(senseid="phone"))
    product_count = len(parser.find_all(senseid="product"))
    default_sense = 'phone' if phone_count > product_count else 'product'

    with open(TEST_XML) as y:
        data = y.read()

    parser = BeautifulSoup(data, 'xml')

    # Read the XML file into testing argument
    for instance in parser.find_all('instance'):
        context = tuple(
            tag.string for tag in instance.find_all('s')
            if tag.string is not None
        )

        sense = None

        # Read the XML file based on the tag instance and read the context
        # Perform search on a particular attribute in the context
        for line in context:
            for attribute in attribute_list:
                if attribute(line)[0]:
                    sense = attribute(line)[1]
                    break

        # If a particular attribute is matched in the attribute list, assign the associated sense
        # If no match is found, assign the default sense (Phone)
        if sense is None:
            sense = default_sense

        id_num = instance['id']
        with open(OUTPUT_ANSWERS, 'a+') as output_check:
            output_check.write(f'<answer instance="{id_num}" senseid="{sense}"/>\n')

        # Print the output in the same standard as the gold standard file
        print(f'<answer instance="{id_num}" senseid="{sense}"/>')

    logger.info("Finished running the decision-list.py script")
