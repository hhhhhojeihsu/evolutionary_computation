#!/usr/bin/env python

import networkx as nx
import random

class generate:
  """Generate various graph
  Args:
    type (string): Which graph type to generate.
      See https://networkx.github.io/documentation/stable/reference/generators.html for required additional argument
      Supported:
        - acomplete: Almost complete graph, arguments should be the same as complete graph
          - TODO. Return complete graph currently
        - complete
        - circulant
        - dgm: Dorogovtsev Goltsev Mendes graph
        - ladder
        - random: fast_gnp_random_graph
          - It does not gurantee there will be no isolated nodes. Proceed with caution.
        - turan
        - wheel
    weight_limit (int pair): Random weight upper and lower bound
    **kwargs: Required arguments for specific graph type

  Attributes:
    type (string): Which graph type to generate.
    supported_type (dict): Supported graph type and its corresponding function pointer
    g_nx (nx): Graph object generated by nx
  """

  def __init__(self, type, weight_limit, **kwargs):
    """Init class
    """

    self.supported_type = {
      "acomplete": self.acomplete_graph,
      "complete": nx.generators.classic.complete_graph,
      "circulant": nx.generators.classic.circulant_graph,
      "dgm": nx.generators.classic.dorogovtsev_goltsev_mendes_graph,
      "ladder": nx.generators.classic.ladder_graph,
      "random": nx.generators.random_graphs.fast_gnp_random_graph,
      "turan": nx.generators.classic.turan_graph,
      "wheel": nx.generators.classic.wheel_graph
    }
    self.supported_out = {"file", "nx", "2d_list"}
    self.type = type

    # Check supported type
    if self.type not in self.supported_type:
      raise Exception('Type \'{}\' not supported'.format(self.type))

    # Ask networkx to generate the graph for us
    self.g_nx = self.supported_type[self.type](**kwargs)

    # Fill in the random value as weight
    for (u, v, w) in self.g_nx.edges(data=True):
      w['weight'] = random.randint(weight_limit[0], weight_limit[1])

    return

  def out(self, type="nx"):
    """Emit the graph
    Args:
      type (string): Type the method should return. Default to "nx"
        Supported:
          - file (TODO)
          - networkx
          - 2d_list
    """

    if type not in self.supported_out:
      raise Exception('Return type \'{}\' not supported'.format(type))

    if type == "nx":
      return self.g_nx
    elif type == "2d_list":
      return nx.to_numpy_array(self.g_nx, dtype=int)

  def acomplete_graph(self, **kwargs):
    g = self.supported_type['complete'](**kwargs)
    return g


