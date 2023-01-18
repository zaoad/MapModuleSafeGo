import json
import datetime
import networkx as nx
import plotly.graph_objects as go
from graph_preparation import *
import osmnx as ox
from data_logger import log_queries, get_logged_data


def get_shortest_road_path(origin_point, destination_point):
    print(origin_point, destination_point)
    origin_node = ox.nearest_nodes(G, origin_point[0], origin_point[1])
    destination_node = ox.nearest_nodes(G, destination_point[0], destination_point[1])
    # origin_node, destination_node = 3310434904, 3220453983
    print(origin_node, destination_node)
    route = nx.shortest_path(G, origin_node, destination_node, weight='length')
    route_nodes = nodes_frame.loc[route]

    # origin_node_point, destination_node_point = nodes_frame.loc[origin_node][['y', 'x']].values, \
    #                                             nodes_frame.loc[destination_node][['y', 'x']].values
    # lat_series, lon_series = route_nodes['y'].values, route_nodes['x'].values
    # plot_path(lat_series, lon_series, origin_point, destination_point)

    path_series = route_nodes[['y', 'x']]
    return path_series


def road_path_operator(origin_point, destination_point):
    # origin_point, destination_point = (23.87, 90.43), (23.73, 90.37)

    # log_queries(origin_point, destination_point)
    # logged_data = get_logged_data()
    # print(logged_data)

    path_series = get_shortest_road_path(origin_point, destination_point)
    print(path_series)


def plot_path(lat_series, lon_series, origin_point, destination_point):
    # adding the lines joining the nodes
    fig = go.Figure(go.Scattermapbox(
        name="Path",
        mode="lines",
        lon=lon_series,
        lat=lat_series,
        marker={'size': 10},
        line=dict(width=4.5, color='grey')))

    # adding source marker
    fig.add_trace(go.Scattermapbox(
        name="Source",
        mode="markers",
        lon=[origin_point[1]],
        lat=[origin_point[0]],
        marker={'size': 12, 'color': "pink"}

    ))

    # adding destination marker
    fig.add_trace(go.Scattermapbox(
        name="Destination",
        mode="markers",
        lon=[destination_point[1]],
        lat=[destination_point[0]],
        marker={'size': 12, 'color': 'green'}))

    lat_center, long_center = np.mean(lat_series), np.mean(lon_series)
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox={
                          'center': {'lat': lat_center,
                                     'lon': long_center},
                          'zoom': 12})
    fig.show()


if __name__ == '__main__':
    exit()
