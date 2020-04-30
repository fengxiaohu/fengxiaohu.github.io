#Method 1: stack helper synchronize with stack data
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []        



    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.helper)==0 or x<=self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])# To keep the sychronization,we must append the duplicate element  


    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.helper.pop()
            return self.helper.pop()
        


    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Method 2: stack helper do not synchronize with stack data
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []



    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.helper)==0 or x<=self.helper[-1]:
            self.helper.append(x)
        


    def pop(self):
        """
        :rtype: None
        """
        top = self.data.pop()
        if self.helper  and top==self.helper[-1]:# Poping the element Only the data stack's element equals to helper stack's element
            self.helper.pop()
        return top 


    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
