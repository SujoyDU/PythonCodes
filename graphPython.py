class Vertex:
    def __init__(self,nodeID):
        self.nodeID = nodeID
        self.connectedTo = {}

    def addConnectedNode(self,node,weight=0):
        self.connectedTo[node] = weight

    def getNodeID(self):
        return self.nodeID

    def getConnectedNodes(self):
        return self.connectedTo.keys()
    
    def getWeight(self,node):
        return self.connectedTo[node]
    
    def __str__(self):
        return str(self.nodeID)+" is connected to nodes "+str(list(self.getConnectedNodes()))
    
    # def __iter__(self):
    #     return iter(self.connectedTo.values())

class Graph:
    def __init__(self):
        self.numberOfVertex = 0
        self.vertexList = {}

    def addVertex(self,vertex):
        newVertex = Vertex(vertex)
        self.vertexList[vertex] = newVertex
        self.numberOfVertex +=1
    
    def addEdge(self,vertex1,vertex2,cost=0):
        if vertex1 not in self.vertexList:
            self.addVertex(vertex1)
        if vertex2 not in self.vertexList:
            self.addVertex(vertex2)
        
        self.vertexList[vertex1].addConnectedNode(self.vertexList[vertex2],cost)
        self.vertexList[vertex2].addConnectedNode(self.vertexList[vertex1],cost)

    def getVertexList(self):
        return self.vertexList.keys()

    def getConnectedList(self,vertex):
        return self.vertexList[vertex]
    
    def __iter__(self):
        return iter(self.vertexList.values())


if __name__ == ('__main__'):
    node = Vertex(5)
    node.addConnectedNode(6)
    node.addConnectedNode(7)
    print(node)

    graph = Graph()
    graph.addEdge(0,1)
    graph.addEdge(0,2)
    graph.addEdge(2,3)

    # print(graph.getVertexList())
    # for edges in graph:
    #     for nodes in edges.getConnectedNodes():
    #         print(edges)
    #         print (nodes)
        

    for v in graph:
        for w in v.getConnectedNodes():
            print("( %s , %s )" % (v.getNodeID(), w.getNodeID()))