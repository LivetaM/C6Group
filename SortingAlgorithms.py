#Jonthan Salmon

#This class contains the two sorting algorithms that I am using in the game, both have reverse
#functions attached to them. Bubble sort and Insertion sort are included and are operational within
#my game

class SortAlgorithms():

    def bubbleSort(self, wordList):
    #Function to sort a list into alphabetical/numerical order using Bubble Sort algorithm
        for i in range(4):
            for j in range(4):
                if (wordList[j])[0] > (wordList[j+1])[0]:
                    wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
        return wordList

    def bubbleSortReverse(self, wordList):
    #Function to sort a list into reverse alphabetical/numerical order using Bubble Sort algorithm
        for i in range(4):
            for j in range(4):
                if (wordList[j])[0] < (wordList[j+1])[0]:
                    wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
        return wordList


    def insertionSort(self, wordList):
    #Function to sort a list into alphabetical/numerical order using Insertion Sort algorithm
        for i in range(5):
            comparisonValue = wordList[i]
            while (i > 0) and (wordList[i-1] > comparisonValue):
                wordList[i] = wordList[i-1]
                i -= 1
            wordList[i] = comparisonValue
        return wordList

    def insertionSortReverse(self, wordList):
    #Function to sort a list into reverse alphabetical/numerical order using Insertion Sort algorithm
        for i in range(5):
            comparisonValue = wordList[i]
            while (i > 0) and (wordList[i-1] < comparisonValue):
                wordList[i] = wordList[i-1]
                i -= 1
            wordList[i] = comparisonValue
        return wordList







