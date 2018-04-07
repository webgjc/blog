class ShuDu():
    #初始化数独长度，数独空点位置
    def __init__(self,state):
        self.STATE = state
        self.N = len(self.STATE[0])
        self.ZERO = [[i,j] for i in range(self.N) for j in range(self.N) if self.STATE[i][j] == 0]
        self.hasAnswer = 0
    #获取空点的可用状态
    def get_state(self,n):
        tmp_state = []
        for i in range(self.N):
            tmp_state.append(self.STATE[self.ZERO[n][0]][i])
            tmp_state.append(self.STATE[i][self.ZERO[n][1]])
        tmp_ny = int(self.ZERO[n][0] / 3)
        tmp_nx = int(self.ZERO[n][1] / 3)
        for i in range(tmp_ny * 3, tmp_ny * 3 + 3):
            for j in range(tmp_nx * 3, tmp_nx * 3 + 3):
                tmp_state.append(self.STATE[i][j])
        '''
        if self.ZERO[n][0] == self.ZERO[n][1]:
            for i in range(self.N):
                tmp_state.append(self.STATE[i][i])
        if self.ZERO[n][0] + self.ZERO[n][1] == 8:
            for i in range(self.N):
                tmp_state.append(self.STATE[i][self.N-1-i])
        '''
        return [i for i in range(1,self.N+1) if i not in list(set(tmp_state))]
    #深度优先搜索部分
    def dfs(self,k=0):
        if "0" not in str(self.STATE):
            self.hasAnswer = 1
            for i in range(self.N):
                print(self.STATE[i])
        if k >= len(self.ZERO) or self.hasAnswer == 1:
            return
        for i in self.get_state(k):
            self.STATE[self.ZERO[k][0]][self.ZERO[k][1]] = i
            self.dfs(k+1)
            self.STATE[self.ZERO[k][0]][self.ZERO[k][1]] = 0

if __name__ == "__main__":
    #据说是最难数独，0代表空的点
    state = [[8,0,0,0,0,0,0,0,0],
             [0,0,3,6,0,0,0,0,0],
             [0,7,0,0,9,0,2,0,0],
             [0,5,0,0,0,7,0,0,0],
             [0,0,0,0,4,5,7,0,0],
             [0,0,0,1,0,0,0,3,0],
             [0,0,1,0,0,0,0,6,8],
             [0,0,8,5,0,0,0,1,0],
             [0,9,0,0,0,0,4,0,0]]
    s = ShuDu(state)
    #秒秒钟解出来
    s.dfs()