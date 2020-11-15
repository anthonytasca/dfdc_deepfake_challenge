import csv

labelObj = {}

with open('validation_labels.csv', newline='') as labels:
    reader = csv.reader(labels, delimiter=',')
    for filename, label in reader:
        labelObj[filename] = label

false_positives = 0
false_negatives = 0
true_positives = 0
true_negatives = 0

with open('submission.csv', newline='') as submission:
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

correct = true_negatives + true_positives
incorrect = false_negatives + false_positives

total = incorrect + correct

print('True Positives = {}'.format(true_positives))
print('False Positives = {}'.format(false_positives))
print('True Negatives = {}'.format(true_negatives))
print('False Negatives = {}'.format(false_negatives))
print('Accuracy: {}/{} = {}'.format(correct, total, correct/total))