import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import scipy as sp
import pylab
import numpy as np
import time

G = nx.DiGraph()

menu = {}
menu['1']="Enter a graph"
menu['2']="Show incidence matrix,size and symmetric"
menu['3']="Show the successors and predecessors of the compenents of the graph"
menu['4']="Eulerien and check a path"
menu['5']="Show if the graph has cycle and test the length of a cycle"
menu['6']="Connectivity"
menu['7']="Dijikstra"
menu['8']="Minimum spanning tree"
menu['9']="Show the graph"
menu['0']="Exit"
while True:
  options=menu.keys()
  for entry in options:
    print(entry, menu[entry])

  time.sleep(0.25)
  selection=input("\nPlease Select:")
  if selection =='1':
      G.clear()
      nbr_nodes = int(input("Enter the number of nodes : "))
      mat =[[0 for i in range(nbr_nodes+1)] for i in range(nbr_nodes+1)]
      for i in range(0,nbr_nodes+1):
          for j in range(0,nbr_nodes+1):
              if(i==0):
                  mat[i][j]=j
                  mat[j][i]=j
              else:
                  if(j!=0):
                      mat[i][j] = 0
      mat[0][0]=0
      nb1 = int(input('Choose a number of edge : '))
      i = 1
      while i <= nb1:
          from1 = int(input("Enter the origin of the edge : "))
          to = int(input("Enter the destination of the edge : "))
          value = int(input("Enter the value of the edge : "))
          mat[from1][to] = value
          if(mat[to][from1] != value):
              mat[to][from1] = -value
          G.add_edge(from1, to, weight=value)
          i = i + 1
      G2 = nx.Graph()
      G2 = G.to_undirected()
      end = input("Enter any caracter to continue : ")
  elif selection == '2':
      print("the incidence matrix with value: ")
      print(nx.incidence_matrix(G, weight='weight').todense())
      print("the incidence matrix oriented : ")
      I = nx.incidence_matrix(G, oriented=True)
      print(I.todense())
      print("the number of vertices : ")
      print(G.number_of_nodes())
      print("the number of edges : ")
      print(G.number_of_edges())
      """for i in range(1,nbr_nodes+1):
          for j in range(1,nbr_nodes+1):
              print(mat[i][j]),
              print()"""
      print(np.matrix(mat))
      cpt = 0
      for i in range(1,nbr_nodes+1):
          for j in range(1,nbr_nodes+1):
              if(mat[i][j] != mat[j][i]):
                  cpt = cpt +1
                  break
          if(cpt != 0):
              break
      if(cpt != 0):
          print("The graph is not symmetric")
      else:
          print("The graph is symmetric")
      print()
      cpt = 0
      for i in range(1,nbr_nodes+1):
          for j in range(1,nbr_nodes+1):
              if((mat[i][j]==0 and i!=j) or mat[i][j]!=mat[j][i]):
                  cpt = cpt +1
                  break
          if(cpt != 0):
              break
      if(cpt != 0):
          print("The graph is not complete")
      else:
          print("The graph is complete")
      end = input("Enter any caracter to continue : ")
  elif selection == '3':
      print("the successor of the element of the graph are : ")
      print(G.succ)

      print("the predecessors of the element of the graph are : ")
      print(G.pred)
      end = input("Enter any caracter to continue : ")
  elif selection == '4':
      if (nx.is_eulerian(G) == True):
          print("the graph is eulerien")
      else:
          print("the graph is not eulerien")
      n1 = int(input("Enter the origin : "))
      n2 = int(input("Enter the destination of the path : "))
      if(nx.has_path(G,n1,n2) == True ):
          print("The path exist : ")
          paths = sorted(nx.all_simple_paths(G, n1, n2))
          print(paths)
      else:
          print("The path does not exist")
      end = input("Enter any caracter to continue : ")
  elif selection == '5':
      if (len(list(nx.simple_cycles(G))) == 0):
          print("the graph has no cycle")
      else:
          print("the graph has : " + str(len(list(nx.simple_cycles(G)))) + " cycle(s) ")
          li = list(nx.simple_cycles(G))
          print(list(nx.simple_cycles(G)))
          i=0
          nb_cycle = int(input("Enter the length of the cycle : "))
          while i < len(li):
              li1 = li[i]
              if(len(li1) == nb_cycle):
                  print(li[i])
              i = i+1
      end = input("Enter any caracter to continue : ")
  elif selection == '6':
      print("Connected compenents")
      Gp = list(nx.connected_components(G2))
      print(Gp)
      print("Strongly connected compenents")
      Gc = list(nx.strongly_connected_components(G))
      print(Gc)
      end = input("Enter any caracter to continue : ")
  elif selection == '7':
      print("Dijikstra : ")
      elt1 = int(input("Enter the origin : "))
      elt2 = int(input("Enter the destination : "))
      print(nx.dijkstra_path(G2, elt1, elt2))
      end = input("Enter any caracter to continue : ")
  elif selection == '8':
      print("minimum spanning tree : ")
      mst = nx.minimum_spanning_edges(G2, data=False)
      edgelist = list(mst)
      print(sorted(edgelist))
      GMST = nx.DiGraph()
      GMST.add_edges_from(edgelist)
      plt.subplot(121)
      nx.draw(GMST, with_labels=True)
      pyl.show()
      end = input("Enter any caracter to continue : ")
  elif selection == '9':
      edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
      pos = nx.spring_layout(G)

      plt.subplot(121)
      nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
      nx.draw(G, pos, with_labels=True, node_size=800)
      pyl.show()
      end = input("Enter any caracter to continue : ")
  elif selection == '0':
      break
  else:
      print("Unknown Option Selected!")

