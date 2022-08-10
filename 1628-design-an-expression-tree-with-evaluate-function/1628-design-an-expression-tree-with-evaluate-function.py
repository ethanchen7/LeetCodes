import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class NumericNode(Node):
    def __init__(self, _value):
        self.value = _value
    def evaluate(self):
        return self.value
    
class BinaryNode(Node):
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
    def evaluate(self):
        pass

class Add(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class Multiply(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Divide(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate()
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operations = {'+': Add, '-': Minus, '*': Multiply, '/': Divide}
        stk = []
        for token in postfix:
            if token in operations:
                R = stk.pop()
                L = stk.pop()
                stk.append(operations[token](L, R))
            else:
                stk.append(NumericNode(int(token)))
        return stk[0]
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        