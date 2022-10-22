
class Node:
    def __init__(self, inCondition, inConclusion, inFatherNode, inExceptNode, inIfnotNode, inDepth):
        self.condition = inCondition
        self.conclusion = inConclusion
        self.fatherNode = inFatherNode
        self.exceptNode = inExceptNode
        self.ifnotNode = inIfnotNode
        self.depth = inDepth
    def countNodes(self):
        count = 1
        if self.exceptNode is not None:
            count += self.exceptNode.countNodes()
        if self.ifnotNode is not None:
            count += self.ifnotNode.countNodes()
        return count
    def satisfy(self, object_):
        check = True
        for i in range(10):
            key = self.condition.context[i]
            if key is not None:
                if not (key == object_.context[i]):
                    check = False
                    break
        return check
