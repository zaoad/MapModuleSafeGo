import osmnx as ox
import numpy as np
import pandas as pd
import pickle as pk


def prepare_dhaka_city_road_data():
    gname = 'road_graph.pk'

    try:
        with open(gname, "rb") as f:
            G = pk.load(f)
        # ox.plot_graph(G, bgcolor='lightgrey', edge_color='darkgrey', node_color='royalblue')
    except:
        north, south, east, west = 23.850551, 23.710392, 90.340775, 90.435281
        G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
        # ox.plot_graph(G, bgcolor='lightgrey', edge_color='darkgrey', node_color='royalblue')

        with open(gname, "wb") as f:
            pk.dump(G, f)

    return G


G = prepare_dhaka_city_road_data()
nodes, edges = list(G.nodes(data=True)), list(G.edges(data=True))
# print(nodes[:4],edges[:4])
nodes_array, edges_array = np.array(nodes), np.array(edges)
# print(pd.DataFrame(list(nodes_array[:, 1])))
# nodes_frame, edges_frame = pd.DataFrame(list(nodes_array[:, 1])).set_index('osmid'), pd.DataFrame(
#     list(edges_array[:, 2]), index=edges_array[:, :2])

nodes_frame, edges_frame = pd.DataFrame(list(nodes_array[:, 1]), index=nodes_array[:, 0]), pd.DataFrame(
    list(edges_array[:, 2]), index=edges_array[:, :2])
