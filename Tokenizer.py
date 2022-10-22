import re
import regex

from StringUtils import StringUtils, VN_abbreviation, is_alphabetic, VN_exception


class Regex:
    ELLIPSIS = "\\.{2,}"
    EMAIL = "([\\w\\d_\\.-]+)@(([\\d\\w-]+)\\.)*([\\d\\w-]+)"
    FULL_DATE = "(0?[1-9]|[12][0-9]|3[01])(\\/|-|\\.)(1[0-2]|(0?[1-9]))((\\/|-|\\.)\\d{4})"
    MONTH = "(1[0-2]|(0?[1-9]))(\\/)\\d{4}"
    DATE = "(0?[1-9]|[12][0-9]|3[01])(\\/)(1[0-2]|(0?[1-9]))"
    TIME = "(\\d\\d:\\d\\d:\\d\\d)|((0?\\d|1\\d|2[0-3])(:|h)(0?\\d|[1-5]\\d)(’|'|p|ph)?)"
    MONEY = "\\p{Sc}\\d+([\\.,]\\d+)*|\\d+([\\.,]\\d+)*\\p{Sc}"
    PHONE_NUMBER = "(\\(?\\+\\d{1,2}\\)?[\\s\\.-]?)?\\d{2,}[\\s\\.-]?\\d{3,}[\\s\\.-]?\\d{3,}"
    URL = "(((https?|ftp):\\/\\/|www\\.)[^\\s/$.?#].[^\\s]*)|(https?:\\/\\/)?(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)"
    NUMBER = "[-+]?\\d+([\\.,]\\d+)*%?\\p{Sc}?"
    PUNCTUATION = ",|\\.|:|\\?|!|;|-|_|\"|'|“|”|\\||\\(|\\)|\\[|\\]|\\{|\\}|âŸ¨|âŸ©|Â«|Â»|\\\\|\\/|\\â€˜|\\â€™|\\â€œ|\\â€�|â€¦|…|‘|’|·"
    SPECIAL_CHAR = "\\~|\\@|\\#|\\^|\\&|\\*|\\+|\\-|\\â€“|<|>|\\|"
    EOS_PUNCTUATION = "(\\.+|\\?|!|…)"
    NUMBERS_EXPRESSION = NUMBER + "([\\+\\-\\*\\/]" + NUMBER + ")*"
    SHORT_NAME = "([\\p{L}]+([\\.\\-][\\p{L}]+)+)|([\\p{L}]+-\\d+)"
    WORD_WITH_HYPHEN = "\\p{L}+-\\p{L}+(-\\p{L}+)*"
    ALLCAP = "[A-Z]+\\.[A-Z]+"

    getRegexList = [
        ELLIPSIS,
        EMAIL,
        URL,
        FULL_DATE,
        MONTH,
        DATE,
        TIME,
        MONEY,
        PHONE_NUMBER,
        SHORT_NAME,
        NUMBERS_EXPRESSION,
        NUMBER,
        WORD_WITH_HYPHEN,
        PUNCTUATION,
        SPECIAL_CHAR,
        ALLCAP,
    ]
    regexIndex = [
        "ELLIPSIS",
        "EMAIL",
        "URL",
        "FULL_DATE",
        "MONTH",
        "DATE",
        "TIME",
        "MONEY",
        "PHONE_NUMBER",
        "SHORT_NAME",
        "NUMBERS_EXPRESSION",
        "NUMBER",
        "WORD_WITH_HYPHEN",
        "PUNCTUATION",
        "SPECIAL_CHAR",
        "ALLCAP",
    ]

    @staticmethod
    def getRegexIndex(regex):
        return Regex.regexIndex.index(regex.upper())


def compile_(x):
    try:
        return re.compile(x)
    except:
        return regex.compile(x)


class Tokenizer:

    @staticmethod
    def split_(pattern, s):
        return [x for x in re.split(pattern, s) if x != ""]

    @staticmethod
    def substring_(s, a, b):
        return s[a:b]

    @staticmethod
    def tokenize(s):
        if s is None or s.strip() == "":
            return []
        temp_tokens = Tokenizer.split_("\\s+", s.strip())
        if len(temp_tokens) == 0:
            return []

        tokens = []
        for token in temp_tokens:
            if len(token) == 1 or not (StringUtils.has_punctuation(token)):
                tokens.append(token)
                continue

            if token.endswith(","):
                tokens.extend(Tokenizer.tokenize(token[0: len(token) - 1]))
                tokens.append(",")
                continue
            if token in VN_abbreviation:
                tokens.append(token)
            if token.endswith(".") and is_alphabetic(token[len(token) - 2]):
                if (len(token) == 2 and token[len(token) - 2].isupper()) or (
                    compile_(Regex.SHORT_NAME).search(token) is not None
                ):
                    tokens.append(token)
                    continue
                tokens.extend(Tokenizer.tokenize(token[0: len(token) - 1] ))
                tokens.append(".")
                continue
            if token in VN_exception:
                tokens.append(token)
                continue

            tokenContainsAbb = False
            for e in VN_abbreviation:
                i = token.find(e)
                if i < 0:
                    continue
                tokenContainsAbb = True
                tokens = Tokenizer.recursive(tokens, token, i, i + len(e))
                break
            if tokenContainsAbb:
                continue
            tokenContainsExp = False
            for e in VN_exception:
                i = token.find(e)
                if i < 0:
                    continue
                tokenContainsExp = True
                tokens = Tokenizer.recursive(tokens, token, i, i + len(e))
                break
            if tokenContainsExp:
                continue
            regexes = Regex.getRegexList
            matching = False
            for regex in regexes:
                if compile_(regex).match(token):
                    tokens.append(token)
                    matching = True
                    break
            if matching:
                continue
            for i in range(len(regexes)):
                pattern = compile_(regexes[i])
                matcher = pattern.search(token)
                if matcher:
                    if i == Regex.getRegexIndex("url"):
                        elements = re.split(r"\.", token)
                        hasURL = True
                        for ele in elements:
                            if len(ele) == 1 and ele[0].isupper():
                                hasURL = False
                                break
                            for j in range(len(ele)):
                                if ord(ele[j]) >= 128:
                                    hasURL = False
                                    break
                        if hasURL:
                            tokens = Tokenizer.recursive(tokens, token, matcher.start(), matcher.end())
                        else:
                            continue
                elif i == Regex.getRegexIndex("month"):
                    start = matcher.start()
                    hasLetter = False
                    for j in range(start):
                        if token[j].isalpha():
                            tokens = Tokenizer.recursive(tokens, token, matcher.start(), matcher.end())
                            hasLetter = True
                            break
                    if not hasLetter:
                        tokens.append(token)
                else:
                    tokens = Tokenizer.recursive(tokens, token, matcher.start(), matcher.end())
                matching = True
                break

            if matching:
                continue
            else:
                tokens.append(token)
        return tokens

    @staticmethod
    def recursive(tokens, token, beginMatch, endMatch):
        if beginMatch > 0:
            tokens.extend(Tokenizer.tokenize(token[0: beginMatch] ))

        tokens.extend(Tokenizer.tokenize(token[beginMatch: endMatch] ))
        if endMatch < len(token):
            tokens.extend(Tokenizer.tokenize(token[:endMatch] ))
        return tokens

    @staticmethod
    def joinSentences(tokens):
        sentences = []
        sentence = []
        for i in range(len(tokens)):
            token = tokens[i]
            nextToken = None
            if i != len(tokens) - 1:
                nextToken = tokens[i + 1]
            beforeToken = None
            if i > 0:
                beforeToken = tokens[i - 1]
            sentence.append(token)
            if i == len(tokens) - 1:
                sentences.append(Tokenizer.joinSentence(sentence))
                return sentences
            if i < len(tokens) - 2 and token == StringConst.COLON:
                if nextToken[0].isdigit() and tokens[i + 2] == StringConst.STOP or tokens[i + 2] == StringConst.COMMA:
                    sentences.append(Tokenizer.joinSentence(sentence))
                    sentence = []
                    continue
            if compile_(Regex.EOS_PUNCTUATION).fullmatch(token):
                if nextToken == '"' or nextToken == "''":
                    count = 0
                    for senToken in sentence:
                        if senToken == '"' or senToken == "''":
                            count += 1
                    if count % 2 == 1:
                        continue
                if (
                    StringUtils.isBrace(nextToken)
                    or nextToken == ""
                    or nextToken[0].islower()
                    or nextToken == StringConst.COMMA
                    or nextToken[0].isdigit()
                ):
                    continue
                if len(sentence) == 2 and token == StringConst.STOP:
                    if beforeToken[0].isdigit():
                        continue
                    if beforeToken[0].islower():
                        continue
                    if beforeToken[0].isupper():
                        if len(beforeToken) == 1:
                            continue
                
                sentences.append(Tokenizer.joinSentence(sentence))
                sentence = []
        return sentences

    @staticmethod
    def joinSentence(tokens):
        sent = ""
        length = len(tokens)
        for i in range(length):
            token = tokens[i]
            if token == "" or token is None or token == StringConst.SPACE:
                continue

            sent = sent + token
            if i < length - 1:
                sent = sent + StringConst.SPACE
        return sent.strip()
    
    @staticmethod
    def sentence_tokenize(s):
        rawSentences = Tokenizer.joinSentences(Tokenizer.tokenize(s))
        return rawSentences


class StringConst:
    BOS = "<s>"
    EOS = "</s>"
    SPACE = " "
    COMMA = ","
    STOP = "."
    COLON = ":"
    UNDERSCORE = "_"
