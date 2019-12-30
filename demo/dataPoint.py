from .filter import startsWithAuthor

def getDataPoint(line):
    splitMessage = line.split(': ') # splitMessage = ['Loki', 'Why do you have 2 numbers, Banner?']
    author = splitMessage[0] # author = 'Loki'
    message = ' '.join(splitMessage[1:]) # message = 'Why do you have 2 numbers, Banner?'
    return author, message