from os import listdir
from simpler import load

PATH = 'recordings/'

def main():
	X, Y = [], []
	for file in listdir(PATH):
		recording = load(PATH + file)
		X.append(recording['input'])
		Y.append(recording['output'])
	print(len(X), len(Y), X[0].shape, Y[0].shape)

if __name__ == '__main__':
	main()