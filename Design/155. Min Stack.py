"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []        
        

    def push(self, x: int) -> None:
        minimum = x
        if len(self.data) != 0:
            minimum = min(x, self.data[-1][1])
        self.data.append([x,minimum])
        

    def pop(self) -> None:
        return self.data.pop()[0]
        

    def top(self) -> int:
        return self.data[-1][0]
        

    def getMin(self) -> int:
        return self.data[-1][1]
        
# Alternative solution for MinStack that uses a min element list to hold all of the 
# minimum elems encountered so far.
class MinStackWithMinElemList:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0 or self.minstack[-1] >= x:
            self.minstack.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()