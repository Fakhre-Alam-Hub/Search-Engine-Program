''' This program returns the result which matches to the given querry string '''

list = ["This is a good program","Python is the best","How are you","This program written by Fakhre Alam","Python is not a Snake",
"C++ and python is a programming language","India is an Asian country","You are invited","what is python",
"Python is not python snake"]

querry = input("Enter your querry : ")

def matchWord(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")

    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


scores = [matchWord(querry,sentence) for sentence in list]

sortedScores = [sent for sent in sorted(zip(scores,list), reverse = True) if sent[0] != 0]

print(f"{len(sortedScores)} result found\n")
for score, item in sortedScores:
    if score != 0:
        print(f"{item} :  with score of {score}")

print()




'''
Author : Fakhre Alam
'''