from FWObject import FWObject
class Utils:
    @staticmethod
    def getCondition(strCondition):
        condition = FWObject(False)
        for rule in strCondition.split(" and "):
            rule = rule.strip()
            key = rule[rule.index(".") + 1: rule.index(" ")]
            value = Utils.getConcreteValue(rule)
            if key == "prevWord2":
                condition.context[4] = value
            elif key == "prevTag2":
                condition.context[5] = value
            elif key == "prevWord1":
                condition.context[2] = value
            elif key == "prevTag1":
                condition.context[3] = value
            elif key == "word":
                condition.context[1] = value
            elif key == "tag":
                condition.context[0] = value
            elif key == "nextWord1":
                condition.context[6] = value
            elif key == "nextTag1":
                condition.context[7] = value
            elif key == "nextWord2":
                condition.context[8] = value
            elif key == "nextTag2":
                condition.context[9] = value
        return condition

    @staticmethod
    def getObject(wordtags, size, index):
        object_ = FWObject(True)
        if index > 1:
            object_.context[4] = wordtags[index - 2].word
            object_.context[5] = wordtags[index - 2].tag
        if index > 0:
            object_.context[2] = wordtags[index - 1].word
            object_.context[3] = wordtags[index - 1].tag
        currentWord = wordtags[index].word
        currentTag = wordtags[index].tag
        object_.context[1] = currentWord
        object_.context[0] = currentTag
        if index < size - 1:
            object_.context[6] = wordtags[index + 1].word
            object_.context[7] = wordtags[index + 1].tag
        if index < size - 2:
            object_.context[8] = wordtags[index + 2].word
            object_.context[9] = wordtags[index + 2].tag

        return object_

    @staticmethod
    def getConcreteValue(string):
        if "\"\"" in string:
            if "Word" in string:
                return "<W>"
            else:
                return "<T>"
        conclusion = string[string.index("\"") + 1: len(string) - 1]
        return conclusion

    NORMALIZER = {
        "òa": "oà",
        "óa": "oá",
        "ỏa": "oả",
        "õa": "oã",
        "ọa": "oạ",
        "òe": "oè",
        "óe": "oé",
        "ỏe": "oẻ",
        "õe": "oẽ",
        "ọe": "oẹ",
        "ùy": "uỳ",
        "úy": "uý",
        "ủy": "uỷ",
        "ũy": "uỹ",
        "ụy": "uỵ",
        "Ủy": "Uỷ"
    }
    NORMALIZER_KEYS = list(NORMALIZER.keys())

