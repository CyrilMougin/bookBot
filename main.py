
def sort_on(dict):
    return dict["num"]
    

def dic_to_listDic(dict):
    list = []
    for key in dict:
        list.append({'letter': key, 'count': dict[key]})
    return list

def count(text):
    splittedText = text.split()
    return len(splittedText)

def letterCounter(text):
    lowerText = text.lower()
    letterDic = {}
    for letter in lowerText:
        if letter in letterDic:
            letterDic[letter] += 1
        else:
            letterDic[letter] = 1
    return letterDic

def sort_on(dict):
    return dict["letter"]

def openFile(filePath):
     with open(filePath) as f:
        fileContents = f.read()
        return fileContents
     


def printReport(filePath):
    completeText = openFile(filePath)
    wordsCount = count(completeText)
    letterCountDic = letterCounter(completeText)
    
    listLetterCount = dic_to_listDic(letterCountDic)
    listLetterCount.sort(reverse=False, key=sort_on)
    
    print(f"--begin report of {filePath}-- ")
    print(f"{wordsCount} words found in the document")
    print()
    for dic in listLetterCount:
        if dic["letter"].isalpha():
            print(f"The '{dic["letter"]}' character was found {dic["count"]} times")
    print("--End report--")



def main():
   filePath = "books/frankenstein.txt"
   printReport(filePath)
   
   




main()