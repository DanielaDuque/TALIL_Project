from ast import For
from re import T
import sys
from random import randint
def readDictDecoupage():
	sentences = {}
	number_sentence = 0
	sentences[number_sentence] = []
	filepath = './atis.train'
	with open(filepath, "r") as fp:
		line = fp.readline()
		cnt = 1
		while line:
			if line == '\t\n':
				number_sentence+=1
				sentences[number_sentence] = []
				line = fp.readline()
				continue
			sentences[number_sentence].append(line)
			# print("Line {}: {}".format(cnt, line.strip()))
			line = fp.readline()
			cnt += 1
	# print(number_sentence)
	return sentences

def decoupage(sentences):
	test = []
	max = len(sentences) - 1
	porcentage = int(len(sentences)*0.20)
	for i in range(porcentage):
		num = randint(0,max)
		max -=1
		idx = list(sentences.keys())[num]
		test.append(sentences.pop(idx))
	train = list(sentences.values())
	return train, test

def createFile(filename, sentenceList):
	with open(filename, 'w') as f:
		for sentence in sentenceList:
			f.write('\n'.join(sentence))
			f.write("\n\t\n")

def readFile(path):
	file = []
	with open(path, "r") as fp:
		line = fp.readline()
		while line:
			file.append(line.strip())
			line = fp.readline()
	return file

def replaceMots(arr, list, replaceMot ):
	for sentence in arr.values():
		for idx in range (len(sentence)):
			mot = sentence[idx]
			sentence[idx] = "\t".join(replaceMot if i in list else i for i in mot.split())

def replaceTotal(arr):
	airports = readFile("./list_airports")
	replaceMots(arr, airports, "airportCity")

	months = readFile("./list_months")
	replaceMots(arr, months, "monthsName")

	days = readFile("./list_days")
	replaceMots(arr, days, "daysName")

	return arr

def main():
	sentences = readDictDecoupage()
	sentences = replaceTotal(sentences)
	for i in range(3):
		train, test = decoupage(sentences)
		createFile(f"./data/decoupage{i+1}.train", train)
		createFile(f"./data/decoupage{i+1}.test", test)
		



if __name__ == "__main__":
    sys.exit(main())
