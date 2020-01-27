class DGraph:
    def __init__(self, vertex):
        self.v = vertex
        self.adjacentMatrix = [[0 for i in range(self.v)] for j in range(self.v)]

    def AddDirectedEdges(self, src, dest, cost):
        if src == dest:
            print("Source and destination are same")
        else:
            self.adjacentMatrix[src][dest] = cost

    def GetDirectedNeighbours(self, source):
        lst = []
        for i in range(len(self.adjacentMatrix[source])):
            if self.adjacentMatrix[source][i] > 0:
                lst.append(i)
        return lst
    
    def DijkstraShortestPath(self,source,dest):
        dct = {}
        for i in range(len(self.adjacentMatrix)):
            temp = {}
            x = self.GetDirectedNeighbours(i)
            for j in x:
                temp[j] = self.adjacentMatrix[i][j]
            dct[i] = temp
        
        begin = source
        end = dest
        shrt_dst = {}
        pred = {}
        uNodes = dct
        infinity = 9999999
        path = []
        for node in uNodes:
            shrt_dst[node] = infinity
        shrt_dst[begin] = 0

        while uNodes:
            minNode = None
            for node in uNodes:
                if minNode is None:
                    minNode = node
                elif shrt_dst[node] < shrt_dst[minNode]:
                    minNode = node

            for childNode, weight in dct[minNode].items():
                if weight + shrt_dst[minNode] < shrt_dst[childNode]:
                    shrt_dst[childNode] = weight + shrt_dst[minNode]
                    pred[childNode] = minNode
            uNodes.pop(minNode)

        currentNode = end
        while currentNode != begin:
            try:
                path.insert(0,currentNode)
                currentNode = pred[currentNode]
            except KeyError:
                print('Path not reachable')
                break
        path.insert(0,begin)
        if shrt_dst[end] != infinity:
            print('Shortest distance is ' + str(shrt_dst[end]))
            print('And the path is ' + str(path))

g = DGraph(5)
g.AddDirectedEdges(0, 1, 3)
g.AddDirectedEdges(0, 2, 5)
g.AddDirectedEdges(1, 4, 12)
g.AddDirectedEdges(1, 3, 10)
g.AddDirectedEdges(2, 1, 6)
g.AddDirectedEdges(2, 3, 8)
g.AddDirectedEdges(3, 4, 5)

g.DijkstraShortestPath(0,4)





