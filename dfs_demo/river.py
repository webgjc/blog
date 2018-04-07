class River():
    def __init__(self):
        self.ship = 1 #1--左岸，-1--右岸
        self.left = [3,3] #和尚，妖怪
        self.right = [0,0] #和尚，妖怪
        #状态改变只有这五种和取反后的五种
        self.change = [ [-1, -1],
                        [-2, 0],
                        [0, -2],
                        [-1, 0],
                        [0, -1]]
        #保存上一个状态，直接排除一样的来回
        self.lastState = -1
        #如果遍历是一棵树，保存的则根到某个枝条
        self.lineHis = [[3, 3, 0, 0, 1]]
    #改变状态
    def move(self,n):
        self.left = [self.left[i]+self.ship*self.change[n][i] for i in range(2)]
        self.right = [self.right[i]-self.ship*self.change[n][i] for i in range(2)]
        self.ship = -self.ship
        self.lastState = n
    #获取下一步可移动点，比如只有一个怪兽在左岸，就要排除两个妖怪过河的方案，这个剪枝很重要。
    def getState(self):
        states = []
        if self.ship == 1:
            state = self.left
        else:
            state = self.right
        for i in range(len(self.change)):
            if min(state[0]+self.change[i][0],state[1]+self.change[i][1])>=0:
                states.append(i)
        return states
    #主算法部分，断掉妖怪大于和尚的分支。
    #在遍历中，最重要的一步就是在这条支线上，如果这一种状态之前出现过，就不要继续深入。
    def dfs(self):
        if self.left==[0,0] and self.right==[3,3]:
            print(self.lineHis)
            return 
        elif (self.left[1]>self.left[0] and self.left[0]!=0) or (self.right[1]>self.right[0] and self.right[0]!=0):
            return
        else:
            states = self.getState()
            for i in states:
                if i != self.lastState:
                    self.move(i)
                    self.lineHis.append(self.left+self.right+[self.ship])
                    if self.lineHis[-1] not in self.lineHis[0:-1]:
                        self.dfs()
                    self.move(i)
                    self.lineHis.pop()
        
if __name__ == "__main__":
    s = River()
    s.dfs()