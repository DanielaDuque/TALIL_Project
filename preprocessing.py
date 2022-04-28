from ast import For
from re import T
import sys
from random import randint
def readDictDecoupage():
	sentences = {}
	number_sentence = 0
	sentences[number_sentence] = ""
	filepath = './atis.train'
	with open(filepath, "r") as fp:
		line = fp.readline()
		cnt = 1
		while line:
			if line == '\t\n':
				number_sentence+=1
				sentences[number_sentence] = ""
				line = fp.readline()
        			continue
			sentences[number_sentence]+=line
			print("Line {}: {}".format(cnt, line.strip()))
			line = fp.readline()
			cnt += 1
	print(number_sentence)
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
			f.write(sentence)

def main():
	sentences = readDictDecoupage()
	for i in range(1):
		train, test = decoupage(sentences)
		print()
		createFile('./decoupage.train', train)
		createFile('./decoupage.test', test)
		



if __name__ == "__main__":
    sys.exit(main())
