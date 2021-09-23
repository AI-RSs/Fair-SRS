import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
from pyvis.network import Network
import pandas as pd


def ITEMnet_func(physics):
  item_net = Network(height='900px', width='100%', bgcolor='#222222', font_color='white',
                   heading='Graph representation of Items')

  # set the physics layout of the network
  item_net.barnes_hut()
  #C:/Users/45027889/Desktop/WSDM/demo/streamlitExamples/data/item_clicks.csv
  #https://github.com/AI-N/Fair-SRS-Demo/blob/main/data/item_clicks.csv
  item_clicks = pd.read_csv('data/item_clicks.csv')
  item_data = item_clicks

  sources = item_data['source']
  targets = item_data['target']
  weights = item_data['count']

  edge_data = zip(sources, targets, weights)

  for e in edge_data:
    src = 'item ' + str(e[0])
    dst = 'item ' + str(e[1])
    w = e[2]

    item_net.add_node(src, src, title=src)  # , color='#03DAC6'
    item_net.add_node(dst, dst, title=dst)
    item_net.add_edge(src, dst, value=w, title=w)

  neighbor_map = item_net.get_adj_list()

  # add neighbor data to node hover data
  for node in item_net.nodes:
    item_net.get_node(node['id'])
    {'size': '20'}
    node['title'] += ' Neighbors: <br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

  # item_net.get_node('item 1')
  # {'color': '#03DAC6','shape': 'star'}


  #if physics:
    #item_net.show_buttons(filter_=['physics'])
  #item_net.show('GraphRepresentationOfItem.html')


#ITEMnet_func(False)

