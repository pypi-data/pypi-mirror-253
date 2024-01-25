import marisa_trie
import re
import os 
import pathlib

class LexToPlus():
    def __init__(self):
        dir = "resource/"
        current_directory = pathlib.Path(__file__).parent
        # current_directory = os.getcwd()
        print(current_directory)
        full_path = os.path.join(current_directory, dir)
        # print(full_path)
        text_file = open(full_path + "full.lex.config", "r")
        fs = text_file.read().splitlines()

        dicts = []
        self.types = []
        for f in fs:
            if len(f) == 0:
                continue
            
            fdict = open(full_path + f, "r")
            dicts.extend(fdict.read().splitlines())

        
        dicts = list(filter(None, dicts))
         
        print("numbers of word:", len(dicts))

        self.trie = marisa_trie.Trie(dicts)
        self.tokenList = []
        
    # def __init__(self,path):
    #     dir = path
    #     text_file = open(dir + "full.lex.config", "r")
    #     fs = text_file.read().splitlines()

    #     dicts = []
    #     self.types = []
    #     for f in fs:
    #         if len(f) == 0:
    #             continue
           
    #         fdict = open(dir + f, "r")
    #         dicts.extend(fdict.read().splitlines())

            
    #     dicts = list(filter(None, dicts))
        
    #     print("numbers of word:", len(dicts))

    #     self.trie = marisa_trie.Trie(dicts)
    #     self.tokenList = []

    def __parseWordInstance__(self, text):
        res = self.trie.prefixes(text)

        if len(res) != 0:
            token = max(res, key=len)
            self.tokenList.append(token)
            self.types.append(1)
            return len(token)
        elif re.search('[ก-ํ]+', text[0]) != None:
            self.tokenList.append(text[0])
            self.types.append(0)
            return 1
        else:
            return 0

    def __wordInstanceBasic__(self, text) -> object:

        pos = 0
        while (pos < len(text)):
            prevPos = pos
            pos = prevPos + self.__parseWordInstance__(text[pos:])

            if (prevPos == pos):
                ch = text[pos]
                # English
                if re.search('[a-zA-Z]+', ch) != None:
                    while re.search('[a-zA-Z]+', ch) != None:

                        pos += 1
                        if pos == len(text):
                            break
                        
                        ch = text[pos]


                    
                    self.tokenList.append(text[prevPos:pos])
                    self.types.append(2)

                elif re.search('[0-9๐-๙]+', ch) != None:
                    ch = text[pos]
                    while pos < len(text) and re.search('[0-9๐-๙,.:]+', ch) != None:
                        pos += 1

                        if pos == len(text):
                            break
                        ch = text[pos]

                    
                    self.tokenList.append(text[prevPos:pos])
                    self.types.append(3)
                else:
                    ch = text[pos]
                    self.tokenList.append(text[pos])
                    self.types.append(4)
                    pos += 1

    def getTypes(self):
        return self.types[:]

    def __unknownMerge__(self):
        if len(self.tokenList) == 0:
            return
        prevWord = self.tokenList[0]
        i = 1

        while i < len(self.tokenList):

            curWord = self.tokenList[i]
            if (len(curWord) == 0):
                i+=1
                continue
            if re.search('[่้๊๋ะัาำิีึืุูๅ็์ํ]+', curWord[0]) != None:
                self.tokenList[i - 1:i + 1] = [''.join(self.tokenList[i - 1:i + 1])]
                self.types[i - 1:i + 1] = [0]
            elif re.search('[เแโไใ]+', prevWord[-1]) != None:
                self.tokenList[i - 1:i + 1] = [''.join(self.tokenList[i - 1:i + 1])]
                self.types[i - 1:i + 1] = [0]
            elif len(curWord)>1 and curWord[1]=='์':
                self.tokenList[i - 1:i + 1] = [''.join(self.tokenList[i - 1:i + 1])]
                self.types[i - 1:i + 1] = [0]
            elif len(curWord) > 2 and curWord[2] == '์':
                self.tokenList[i - 1:i + 1] = [''.join(self.tokenList[i - 1:i + 1])]
                self.types[i - 1:i + 1] = [0]
            elif self.types[i-1]==0 and self.types[i]==0:
                self.tokenList[i - 1:i + 1] = [''.join(self.tokenList[i - 1:i + 1])]
                self.types[i - 1:i + 1] = [0]

            i += 1
            prevWord = curWord;

    def wordInstance(self, text):
        self.tokenList[:] = []
        self.types[:] = []

        self.__wordInstanceBasic__(text)
        self.__unknownMerge__()
        self.__unknownMerge__()
        self.__unknownMerge__()

        return self.tokenList[:]


        
