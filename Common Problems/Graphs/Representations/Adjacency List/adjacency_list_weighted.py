class WeightedGraph:
   def __init__(self, directed=True):
       self.directed = directed
       self.adjacent_list = {}
       self.reveresed_list = {}

   def create_vertex(self, vertex):
       if vertex in self.adjacent_list:
           return False
       self.adjacent_list[vertex] = {}
       self.reveresed_list[vertex] = {}
       return True
  
   def create_edge(self,u,v,weight):
       if u not in self.adjacent_list:
           self.create_vertex(u)
          
       if v not in self.adjacent_list:
           self.create_vertex(v)

       self.adjacent_list[u][v] = weight
       self.reveresed_list[v][u] = weight

       if not self.directed:
           self.adjacent_list[v][u] = weight
           self.reveresed_list[u][v] = weight

       return True
  
   def remove_edge(self,u, v):
       if u not in self.adjacent_list or v not in self.adjacent_list:
           return False
      
       self.adjacent_list[u].pop(v, None)
       self.reveresed_list[v].pop(u, None)

       if not self.directed:
           self.adjacent_list[v].pop(u, None)
           self.reveresed_list[u].pop(v, None)

       return True
      

   def remove_vertex(self, vertex):
       if vertex not in self.adjacent_list:
           return False
      
       # removing outgoing self.reversed list
       for neighbour in self.adjacent_list[vertex]:
           self.reveresed_list[neighbour].pop(vertex, None)

       # removing incoming nodes from adjacent list
       for neighbour in self.reveresed_list[vertex]:
           self.adjacent_list[neighbour].pop(vertex, None)

       del self.adjacent_list[vertex]
       del self.reveresed_list[vertex]

       return True
  
   def get_weight(self,u,v):
       return self.adjacent_list.get(u,{}).get(v)
  
   def display(self):
       return {key:dict(val) for key, val in self.adjacent_list.items()}
  

g = WeightedGraph()
g.create_vertex("a")
g.create_vertex("b")
g.create_vertex("c")
g.create_vertex("d")
g.create_edge("d", "a",1)
g.create_edge("a", "b",5)
g.create_edge("a", "c",3)
g.create_edge("b", "c", 2)
print("----WEIGHT BETWEEN A & C------\n",g.get_weight("a","c"))
print("----OUR GRAPH------\n",g.display())
g.remove_vertex("a")
print("----OUR GRAPH AFTER REMOVING A------\n",g.display())