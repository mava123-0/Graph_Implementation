#Reading a GML File and printing the Adjacency List,Adjacency Matrix
#Calculating the number of Vertices and Edges
#and printing the Topological Sort of the Graph
#using iGraph

def topologicalSortUtil( graph,v, visited, stack,vert_list):
        visited[int(v)] = True
        print(v, end=", ")
        for (i) in (g.get_adjlist()[v]):
            if visited[int(i)] == False:
                topologicalSortUtil(graph, i, visited, stack, vert_list)
        # print(int(v))
        stack.append(int(v))
 
def topologicalSort(g,v,n):
    visited = [False]*n
    stack = []
    for i in range(n):
        if visited[i] == False:
            topologicalSortUtil(g,i, visited, stack, vert_list)
 
    while (len(stack) > 0):
        stack.pop()
        pass #print(stack.pop(), end = ", ")

if __name__=='__main__':
    from igraph import *
    g=Graph.Read_GML("nodes.gml")
    #Eliminate any duplicate edges from the graph
    g.simplify(multiple=True,loops=True)
    n=g.vcount() 
    m=g.ecount()
    print("\n")
    print("Adjacency List: ")
    edj_list= g.get_edgelist()
    a=0
    b=0
    while(a<m):
        vert=edj_list[a][b]
        if(vert!=edj_list[a-1][0]):
            print("")
            print(vert,end=" ")
        print(" -> ",edj_list[a][1],end=" ")
        a=a+1

    #Adjacency Matrix
    adj_matrix=[[0 for i in range(n)] for i in range(n)]
    print("\n")
    print("Adjacency Matrix: ")
    a=0
    while(a<m):
        adj_matrix[edj_list[a][0]][edj_list[a][1]]=1
        a+=1

    for i in range(n):
        for j in range(n):
            print(adj_matrix[i][j],end=" ")
        print("")

    #Calculating Edges from the Adjacency Matrix
    edj_no=0
    for i in range(n):
        for j in range(n):
            if(adj_matrix[i][j]==1):
                edj_no+=1

    print("\n")
    print("No of Vertices: ",n)
    print("No of Edges: ",edj_no)

    # topological sort(g)
    print("\n")
    print("Topological Sort: ")
    vert_list=g.vs()
    # print(vert_list[2])
    topologicalSort(g,vert_list,n)
    print("\n")
    # print(edj_list)