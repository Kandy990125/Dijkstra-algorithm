# -*- coding: utf-8 -*-
import sys
# i = sys.maxint
class Dijkstra:
    def __init__(self, n):
        # 结点为1-n
        self.n = n
        self.cost = []
        self.v = 0
        self.D = []

    def set_nodes_cost(self):
        '''初始化二维数组'''
        i = 0
        while i < self.n:
            j = 0
            temp = []
            while j < self.n:
                temp.append(0)
                j = j + 1
            self.cost.append(temp)
            i = i + 1
        # print cost
        '''输入各个节点之间的代价，如果输入MAX的话，自动将代价置为系统中的int最大值'''
        print "请输入结点的代价(不相邻的结点代价请输入MAX)"
        i = 0
        while i < self.n-1:
            j = i + 1
            while j < self.n:
                input_value = raw_input("cost(%d,%d):" % (i, j))
                if input_value == "MAX":
                    self.cost[j][i] = self.cost[i][j] = sys.maxint
                else:
                    self.cost[j][i] = self.cost[i][j] = int(input_value)
                j = j + 1
            i = i + 1
        # for item in self.cost:
        #             print item, len(item)

    def set_origin(self):
        '''输入源点'''
        self.v = input("请输入源点序号(0~%d):"%(self.n-1))

    def set_D(self):
        i = 0
        while i < self.n:
            self.D.append(0)
            i = i + 1
        T = []
        T.append(self.v)
        i = 0
        while i < self.n:
            # print self.v, i
            self.D[i] = self.cost[self.v][i]
            i = i + 1
        while len(T) != self.n:
            D_min = sys.maxint
            i = 0
            for item in self.D:
                if (i not in T) and item < D_min:
                    min_num = i
                    D_min = item
                i = i + 1
            T.append(min_num)

            i = 0
            while i < self.n:
                if (i not in T) and self.cost[min_num][i] < sys.maxint:
                    self.D[i] = min(self.D[i], self.D[min_num] + self.cost[min_num][i])
                i = i + 1
        return self.D

if __name__ == "__main__":
    n = input("请输入结点的个数:")
    Dijkstra = Dijkstra(n)
    Dijkstra.set_origin()
    Dijkstra.set_nodes_cost()
    i = 0
    result = Dijkstra.set_D()
    while i < len(result):
        print "min(%d,%d):%d" % (Dijkstra.v, i, result[i])
        i = i + 1