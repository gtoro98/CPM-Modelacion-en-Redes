import pylab
import matplotlib.pyplot as plt
import networkx as nx

def crearGrafo(tabla_cpm, actividades,RutaMasCorta):
    G=nx.DiGraph()
    G.clear()
    for actividad in tabla_cpm:
        G.add_node(actividad["numero_act"], CPM=str(actividad['ES'])+'|'+str(actividad['duracion'])+'|'+str(actividad['EF'])+'\n'+actividad['actividad']+'\n'+str(actividad['LS'])+'|'+str(actividad['duracion'])+'|'+str(actividad['LF']))

    edgeColor=[]
    edgeWeighy=[]
    for i in range(len(actividades)):
        if(len(actividades[i]['predecesor']) > 0):
            for predecesor in actividades[i]['predecesor']:
                if str(actividades[i]['descripcion']) in RutaMasCorta and str(actividades[predecesor]['descripcion']) in RutaMasCorta:
                    edgeColor.append("red")
                    edgeWeighy.append(3)
                else:
                    edgeColor.append("black")
                    edgeWeighy.append(1)
                    
                G.add_edge(predecesor, actividades[i]['numero_act'])
    
    labels = nx.get_node_attributes(G, 'CPM')
    nx.draw(G, labels=labels, with_labels = True, node_size=4000, node_color="#8DF2F2", font_color="black",edge_color =edgeColor, width =edgeWeighy)
    plt.show()