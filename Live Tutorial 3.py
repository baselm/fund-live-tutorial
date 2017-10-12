# Live Tutorial 3 commands and examplesp = graphs.CompleteGraph(5); pp.is_connected()g =Graph({'Dublin':{'Naas':'M7'}, 'Naas':{ 'Newbridge':'M7','Carlow':'M9'}, 'Newbridge':{'Kildare':'M7'}, 'Kildare':{'Portlaoise':'M7'}})
g.graphplot(title = 'Irish Map',
                        vertex_size=1500,
                        edge_thickness=3,
                        edge_color='green',
                       vertex_color='Red',
                      edge_labels=True).plot()
p.is_connected()
# To check connected components
G = Graph( { 0 : [1, 3], 1 : [2], 2 : [3], 4 : [5, 6], 5 : [6] }); G
L = G.connected_components_subgraphs()
graphs_list.show_graphs(L) 
#OPTIONAL  LollipopGraph
x = graphs.LollipopGraph(4,2); x.show()
print "Summary"
print "*****************************"
print("Test is 1 a cute vertex: "),x.is_cut_vertex(1) 
print("Tes t is 2 a cute vertex: "),x.is_cut_vertex(2) 
print("Test is 3 a cute vertex: "),x.is_cut_vertex(3) 
print("Test is 4 a cute vertex: "),x.is_cut_vertex(4) 
print("Test is 5 a cute vertex: "),x.is_cut_vertex(5) 
print ("")
print("Test if (0,1) is a cute edge:"), x.is_cut_edge(0,1) 
print("Test if (0,2) is a cute edge:"), x.is_cut_edge(0,2) 
print("Test if (0,3) is a cute edge:"), x.is_cut_edge(0,3) 
print("Test if (1,2) is a cute edge:"), x.is_cut_edge(1,2) 
print("Test if (1,3) is a cute edge:"), x.is_cut_edge(1,3) 
print("Test if (2,3) is a cute edge:"), x.is_cut_edge(2,3) 
print("Test if (3,4) is a cute edge:"), x.is_cut_edge(3,4) 
print("Test if (4,5) is a cute edge:"), x.is_cut_edge(4,5)
 #OPTIONAL TASK of Lab 4
#GRAPH G
g = DiGraph(6,multiedges = True)
g.relabel({0:'u1', 1:'u2', 2:'u3', 3:'u4', 4:'u5', 5: 'u6'})
g.add_edge('u1','u4')
g.add_edge('u2','u5')
g.add_edge('u3','u4')
g.add_edge('u3','u6')
g.add_edge('u4','u2')
g.add_edge('u5','u1')
g.add_edge('u5','u3')
g.add_edge('u6','u2')
g.add_edge('u6','u1')


#GRAPH H
h = DiGraph(6,multiedges = True)
h.relabel({0:'v1', 1:'v2', 2:'v3', 3:'v4', 4:'v5', 5: 'v6'})
h.add_edge('v1','v2')
h.add_edge('v1','v6')
h.add_edge('v2','v5')
h.add_edge('v3','v2')
h.add_edge('v3','v4')
h.add_edge('v4','v1')
h.add_edge('v5','v4')
h.add_edge('v6','v5')
h.add_edge('v6','v3')


#PRINTABLES
print('GRAPH G')
g.show()
print('SUMMARY')
print('****************************************************')
print('TOTAL EDGES IN GRAPH IS: ' + str(g.num_edges()))
print('TOTAL DEGREES IN GRAPH IS: ' + str(sum(g.degree())))
print('ADJACENCY MATRIX')
g.adjacency_matrix()
print('GRAPH H')
h.show()
print('SUMMARY')
print('****************************************************')
print('TOTAL EDGES IN GRAPH IS: ' + str(h.num_edges()))
print('TOTAL DEGREES IN GRAPH IS: ' + str(sum(h.degree())))
print('ADJACENCY MATRIX')
h.adjacency_matrix()
print('ARE THE ADJACENCY MATRIX EQUAL IN GRAPHS A & B')
g.adjacency_matrix() == h.adjacency_matrix()
print('ARE THE ADJACENCY MATRIX EQUAL IN GRAPHS G & H')
g.adjacency_matrix() == h.adjacency_matrix()
#PART 2 ISOMORPHIC OR NOT??
print('NUMBER OF EDGES IN G & H ARE EQUAL : ' + str(g.num_edges() == h.num_edges()))
print('NUMBER OF DEGREES IN G & H ARE EQUAL : ' + str(g.degree() == h.degree()))
print('NUMBER OF VERTICES IN G & H ARE EQUAL : ' + str(g.num_verts() == h.num_verts()))
print('NUMBER OF DEGREES IN EACH VERTEX OF G')
print('U1 Degrees : ' + str(g.degree('u1')))
print('U2 Degrees : ' + str(g.degree('u2')))
print('U3 Degrees : ' + str(g.degree('u3')))
print('U4 Degrees : ' + str(g.degree('u4')))
print('U5 Degrees : ' + str(g.degree('u5')))
print('U6 Degrees : ' + str(g.degree('u6')))    
print('*************************************')
print('NUMBER OF DEGREES IN EACH VERTEX OF H')
print('V1 Degrees : ' + str(h.degree('v1')))
print('V2 Degrees : ' + str(h.degree('v2')))
print('V3 Degrees : ' + str(h.degree('v3')))
print('V4 Degrees : ' + str(h.degree('v4')))
print('V5 Degrees : ' + str(h.degree('v5')))
print('V6 Degrees : ' + str(h.degree('v6')))
print('IS ISOMORPHIC : ' + str(h.is_isomorphic(h)))#OPTIONAL TASK of Lab 4
#GRAPH G
g = DiGraph(6,multiedges = True)
g.relabel({0:'u1', 1:'u2', 2:'u3', 3:'u4', 4:'u5', 5: 'u6'})
g.add_edge('u1','u4')
g.add_edge('u2','u5')
g.add_edge('u3','u4')
g.add_edge('u3','u6')
g.add_edge('u4','u2')
g.add_edge('u5','u1')
g.add_edge('u5','u3')
g.add_edge('u6','u2')
g.add_edge('u6','u1')


#GRAPH H
h = DiGraph(6,multiedges = True)
h.relabel({0:'v1', 1:'v2', 2:'v3', 3:'v4', 4:'v5', 5: 'v6'})
h.add_edge('v1','v2')
h.add_edge('v1','v6')
h.add_edge('v2','v5')
h.add_edge('v3','v2')
h.add_edge('v3','v4')
h.add_edge('v4','v1')
h.add_edge('v5','v4')
h.add_edge('v6','v5')
h.add_edge('v6','v3')


#PRINTABLES
print('GRAPH G')
g.show()
print('SUMMARY')
print('****************************************************')
print('TOTAL EDGES IN GRAPH IS: ' + str(g.num_edges()))
print('TOTAL DEGREES IN GRAPH IS: ' + str(sum(g.degree())))
print('ADJACENCY MATRIX')
g.adjacency_matrix()
print('GRAPH H')
h.show()
print('SUMMARY')
print('****************************************************')
print('TOTAL EDGES IN GRAPH IS: ' + str(h.num_edges()))
print('TOTAL DEGREES IN GRAPH IS: ' + str(sum(h.degree())))
print('ADJACENCY MATRIX')
h.adjacency_matrix()
print('ARE THE ADJACENCY MATRIX EQUAL IN GRAPHS A & B')
g.adjacency_matrix() == h.adjacency_matrix()
print('ARE THE ADJACENCY MATRIX EQUAL IN GRAPHS G & H')
g.adjacency_matrix() == h.adjacency_matrix()
#PART 2 ISOMORPHIC OR NOT??
print('NUMBER OF EDGES IN G & H ARE EQUAL : ' + str(g.num_edges() == h.num_edges()))
print('NUMBER OF DEGREES IN G & H ARE EQUAL : ' + str(g.degree() == h.degree()))
print('NUMBER OF VERTICES IN G & H ARE EQUAL : ' + str(g.num_verts() == h.num_verts()))
print('NUMBER OF DEGREES IN EACH VERTEX OF G')
print('U1 Degrees : ' + str(g.degree('u1')))
print('U2 Degrees : ' + str(g.degree('u2')))
print('U3 Degrees : ' + str(g.degree('u3')))
print('U4 Degrees : ' + str(g.degree('u4')))
print('U5 Degrees : ' + str(g.degree('u5')))
print('U6 Degrees : ' + str(g.degree('u6')))    
print('*************************************')
print('NUMBER OF DEGREES IN EACH VERTEX OF H')
print('V1 Degrees : ' + str(h.degree('v1')))
print('V2 Degrees : ' + str(h.degree('v2')))
print('V3 Degrees : ' + str(h.degree('v3')))
print('V4 Degrees : ' + str(h.degree('v4')))
print('V5 Degrees : ' + str(h.degree('v5')))
print('V6 Degrees : ' + str(h.degree('v6')))
print('IS ISOMORPHIC : ' + str(h.is_isomorphic(h)))p.is_connected()# Live Tutorial 3 commands and examples# Live Tutorial 3 commands and examplesp = graphs.CompleteGraph(5); pp = graphs.CompleteGraph(5); pg =Graph({'Dublin':{'Naas':'M7'}, 'Naas':{ 'Newbridge':'M7','Carlow':'M9'}, 'Newbridge':{'Kildare':'M7'}, 'Kildare':{'Portlaoise':'M7'}})
g.graphplot(title = 'Irish Map',
                        vertex_size=1500,
                        edge_thickness=3,
                        edge_color='green',
                       vertex_color='Red',
                      edge_labels=True).plot()p.is_connected()p.is_connected()p = graphs.CompleteGraph(5); pp = graphs.CompleteGraph(5); pp.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()p.is_connected()g =Graph({'Dublin':{'Naas':'M7'}, 'Naas':{ 'Newbridge':'M7','Carlow':'M9'}, 'Newbridge':{'Kildare':'M7'}, 'Kildare':{'Portlaoise':'M7'}})
g.graphplot(title = 'Irish Map',
                        vertex_size=1500,
                        edge_thickness=3,
                        edge_color='green',
                       vertex_color='Red',
                      edge_labels=True).plot()g =Graph({'Dublin':{'Naas':'M7'}, 'Naas':{ 'Newbridge':'M7','Carlow':'M9'}, 'Newbridge':{'Kildare':'M7'}, 'Kildare':{'Portlaoise':'M7'}})
g.graphplot(title = 'Irish Map',
                        vertex_size=1500,
                        edge_thickness=3,
                        edge_color='green',
                       vertex_color='Red',
                      edge_labels=True).plot()# Live Tutorial 3 commands and examplesp = graphs.CompleteGraph(5); pp = graphs.CompleteGraph(5); pp.is_connected()p = graphs.CompleteGraph(5); pg =Graph({'Dublin':{'Naas':'M7'}, 'Naas':{ 'Newbridge':'M7','Carlow':'M9'}, 'Newbridge':{'Kildare':'M7'}, 'Kildare':{'Portlaoise':'M7'}})
g.graphplot(title = 'Irish Map',
                        vertex_size=1500,
                        edge_thickness=3,
                        edge_color='green',
                       vertex_color='Red',
                      edge_labels=True).plot()p.is_connected()g.connected_components()g.connected_components()G = Graph( { 0 : [1, 3], 1 : [2], 2 : [3], 4 : [5, 6], 5 : [6] }); G
L = G.connected_components_subgraphs()
graphs_list.show_graphs(L)
