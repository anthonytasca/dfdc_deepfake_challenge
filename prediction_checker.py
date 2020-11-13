import csv

labelObj = {}

with open('validation_labels.csv', newline='') as labels:
    reader = csv.reader(labels, delimiter=',')
    for filename, label in reader:
        labelObj[filename] = label

correct = 0
incorrect = 0

with open('submission.csv', newline='') as submission:
    reader = csv.reader(submission, delimiter=',')
    for filename, label in reader:
        if filename[-4:] == '.mp4':
            print('{}={}'.format(labelObj[filename][0], round(float(label))))
            if int(labelObj[filename][0]) == round(float(label)):
                correct = correct + 1
            else:
                incorrect = incorrect + 1

total = incorrect + correct

print('Accuracy: {}/{} = {}'.format(correct, total, correct/total))