from Node import Node
from FWObject import FWObject
from Vocabulary import Vocabulary
from Utils import Utils
from WordTag import WordTag
import re
from Tokenizer import Tokenizer
class WordSegmenter:

    def __init__(self):
        try:
            modelPath = "wordsegmenter.rdr"
            self.constructTreeFromRulesFile(modelPath)
        except:
            pass

    def constructTreeFromRulesFile(self, rulesFilePath):
        self.root = Node(FWObject(False), "NN", None, None, None, 0)
        
        currentNode = self.root
        currentDepth = 0
        with open(rulesFilePath, 'r') as f:
            for _, line in enumerate(f.readlines()):
                if _ == 0:
                    continue
                depth = 0
                for i in range(7):
                    if line[i] == '\t':
                        depth += 1
                    else:
                        break
                line = line.strip()
                if len(line) == 0:
                    continue
                if "cc:" in line:
                    continue
                condition = Utils.getCondition(line.split(" : ")[0].strip())
                conclusion = Utils.getConcreteValue(line.split(" : ")[1].strip())
                node = Node(condition, conclusion, None, None, None, depth)
                if depth > currentDepth:
                    currentNode.exceptNode = node
                elif depth == currentDepth:
                    currentNode.ifnotNode = node
                else:
                    while currentNode.depth != depth:
                        currentNode = currentNode.fatherNode
                    currentNode.ifnotNode = node
                node.fatherNode = currentNode
                currentNode = node
                currentDepth = depth

    def findFiredNode(self, object_):
        currentN = self.root
        firedN = None
        while True:
            if currentN.satisfy(object_):
                firedN = currentN
                if currentN.exceptNode is None:
                    break
                else:
                    currentN = currentN.exceptNode
            else:
                if currentN.ifnotNode is None:
                    break
                else:
                    currentN = currentN.ifnotNode
        return firedN

    @staticmethod
    def split_(pattern, s):
        return [x for x in re.split(pattern, s) if x != ""]

    def getInitialSegmentation(self, sentence):
        wordtags = []
        for regex in Utils.NORMALIZER_KEYS:
            if regex in sentence:
                sentence = sentence.replace(regex, Utils.NORMALIZER[regex])
        tokens = WordSegmenter.split_("\\s+", sentence)
        lowerTokens = WordSegmenter.split_("\\s+", sentence.lower())
        senLength = len(tokens)
        i = 0
        while i < senLength:
            token = tokens[i]
            if all(c.isalpha() for c in token):
                if token[0].islower() and i + 1 < senLength:
                    if tokens[i + 1][0].isupper():
                        wordtags.append(WordTag(token, "B"))
                        i += 1
                        continue
                isSingleSyllabel = True
                for j in range(min(i + 4, senLength), i + 1, -1):
                    word = " ".join(lowerTokens[i: j])
                    if word in Vocabulary.VN_DICT or word in Vocabulary.VN_LOCATIONS or word in Vocabulary.COUNTRY_L_NAME:
                        wordtags.append(WordTag(token, "B"))
                        for k in range(i + 1, j):
                            wordtags.append(WordTag(tokens[k], "I"))
                        i = j - 1
                        isSingleSyllabel = False
                        break
                if isSingleSyllabel:
                    lowercasedToken = lowerTokens[i]
                    if lowercasedToken in Vocabulary.VN_FIRST_SENT_WORDS or \
                            token[0].islower() or \
                            token[0].islower() or all(c.isupper() for c in token) or \
                            lowercasedToken in Vocabulary.COUNTRY_S_NAME or \
                            lowercasedToken in Vocabulary.WORLD_COMPANY:
                        wordtags.append(WordTag(token, "B"))
                        i += 1
                        continue
                    ilower = i + 1
                    for ilower in range(i + 1, min(i + 4, senLength)):
                        ntoken = tokens[ilower]
                        if ntoken[0].islower() or \
                                (not all(c.isalpha() for c in ntoken)) or \
                                ntoken == "LBKT" or ntoken == "RBKT":
                            break
                    if ilower > i + 1:
                        isNotMiddleName = True
                        if lowercasedToken in Vocabulary.VN_MIDDLE_NAMES and i >= 1:
                            prevT = tokens[i - 1]
                            if prevT[0].isupper():
                                if prevT.lower() in Vocabulary.VN_FAMILY_NAMES:
                                    wordtags.append(WordTag(token, "I"))
                                    isNotMiddleName = False
                        if isNotMiddleName:
                            wordtags.append(WordTag(token, "B"))
                        for k in range(i + 1, ilower):
                            wordtags.append(WordTag(tokens[k], "I"))
                        i = ilower - 1
                    else:
                        wordtags.append(WordTag(token, "B"))
            else:
                wordtags.append(WordTag(token, "B"))
            i += 1
        return wordtags

    def segmentTokenizedString(self, line):
        try:
            sb = ""
            line = line.strip()
            if len(line) == 0:
                return "\n"
            wordtags = self.getInitialSegmentation(line)
            
            size = len(wordtags)
            for i in range(size):
                object_ = Utils.getObject(wordtags, size, i)
                firedNode = self.findFiredNode(object_)
                if firedNode is not None and firedNode.depth > 0:
                    if firedNode.conclusion == "B":
                        sb = sb + " " + wordtags[i].form
                    else:
                        sb = sb + "_" + wordtags[i].form
                else:
                    if wordtags[i].tag == "B":
                        sb = sb + " " + wordtags[i].form
                    else:
                        sb = sb + "_" + wordtags[i].form
            return sb.strip()
        except:
            pass
    
    def tokenize(self, s):
        rawSentences = Tokenizer.joinSentences(Tokenizer.tokenize(s))
        result = [self.segmentTokenizedString(rawSentence).split() for rawSentence in rawSentences if len(rawSentence.strip()) > 0]
        return result




