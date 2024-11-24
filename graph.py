class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
    """edges is a dict mapping node to list of its children"""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result[:-1] #Omit last newline    

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDest(), edge.getSrc())
        Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'NY', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('NY'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def formatPath(path):
    toPrint = ""
    for node in path:
       toPrint += str(node) + '->'
    s = toPrint[:-2] #Remove last -> chars
    return s

#Depth-first Search
def DFS(graph, startNode, endNode, path, shortest, toPrint = False):
    path = path + [startNode]
    if toPrint:
        print('Current DFS path:', formatPath(path))
    if startNode == endNode:
        return path
    for node in graph.childrenOf(startNode):
        if node not in path: #avoid loops
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, endNode, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

#Breadth-first Search
def BFS(graph, startNode, endNode, toPrint = False):
    initPath = [startNode]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        if toPrint:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(formatPath(p))
        #Get+Remove oldest element in queue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', formatPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == endNode:
            return tmpPath #shortest anwser
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                pathQueue.append(tmpPath + [nextNode])
    return None

def shortestPath(graph, start, end, toPrint = False):
    return BFS(graph, start, end, toPrint)
    #return DFS(graph, start, end, [], None, toPrint)

def testShortestPath(src, dest):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(src), g.getNode(dest), toPrint = True)
    if sp != None:
        print('Shortest path from', src, 'to', dest, 'is', formatPath(sp))
    else:
        print('No way from', src, 'to', dest)
    
#testShortestPath('Chicago', 'Boston')
testShortestPath('Boston', 'Phoenix')
