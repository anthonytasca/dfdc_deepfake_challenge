import os
import argparse
import numpy as np
from matplotlib import pyplot as plt
import csv

def parse_args():
    parser = argparse.ArgumentParser(
        description="Plot results from csv")
    parser.add_argument("--csv-files", nargs='+', help="paths to csv files", required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    labelObj = {}

    with open('validation_labels.csv', newline='') as labels:
        reader = csv.reader(labels, delimiter=',')
        for filename, label in reader:
            labelObj[filename] = label

    precision = []
    recall = []

    csv_files = args.csv_files[0].split(',')
    print(csv_files)
    for csv_file in csv_files:
        false_positives = 0
        false_negatives = 0
        true_positives = 0
        true_negatives = 0
        with open(csv_file, newline='') as submission:
            reader = csv.reader(submission, delimiter=',')
            for filename, label in reader:
                if filename[-4:] == '.mp4':
                    if int(labelObj[filename][0]) == 1:
                        if round(float(label)) == 1:
                            true_positives = true_positives + 1
                        else:
                            false_negatives = false_negatives + 1
                    else:
                        if round(float(label)) == 1:
                            false_positives = false_positives + 1
                        else:
                            true_negatives = true_negatives + 1
        precision.append(true_positives/(true_positives+false_positives))
        recall.append(true_positives/(true_positives+false_negatives))

    print(precision)
    print(recall)

    fig, ax = plt.subplots()
    x = np.arange(len(csv_files))
    ax.set_title('Validation set performance by model')
    ax.set_xticks(x)
    ax.set_xticklabels(map(lambda x: os.path.basename(x).split('_')[-1], csv_files))
    ax.legend()
    width = 0.35
    rects1 = ax.bar(x - width/2, precision, width, label='Precision')
    rects2 = ax.bar(x + width/2, recall, width, label='Recall')
    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    for rect in rects2:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
