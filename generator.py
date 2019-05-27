#!/usr/bin/env python

import networkx as nx

class generate:
  """Generate various graph

  Attributes:
    type (string): Which graph type to generate.
      See https://networkx.github.io/documentation/stable/reference/generators.html for required additional argument
      Supported:
        - acomplete: Almost complete graph
        - complete
        - circulant
        - dgm: Dorogovtsev Goltsev Mendes graph
        - ladder
        - turan
        - wheel
    out (string): What the class should return
      Supported:
        - file (TODO)
        - networkx
        - 2d_list
  """

  def __init__(self, type, **kwargs):
    """Init class

    Attributes:
      supported_type (dict): Supported graph type correspond to its function pointer
    """

    self.supported_type = {
      "acomplete": self.acomplete_graph,
      "complete": nx.generators.classic.complete_graph,
      "circulant": nx.generators.classic.circulant_graph,
      "dgm": nx.generators.classic.dorogovtsev_goltsev_mendes_graph,
      "ladder": nx.generators.classic.ladder_graph,
      "turan": nx.generators.classic.turan_graph,
      "wheel": nx.generators.classic.wheel_graph
    }

    self.type = type

    # Check supported type
    if self.type not in self.supported_type:
      raise Exception('Type \'{}\' not supported'.format(self.type))

    # Ask networkx to generate the graph for us
    self.g_nx = self.supported_type[self.type](**kwargs)
    return

  def out(self, type="nx"):
    """Emit the graph
    Args:
      type (string): Type the method should return
    Attributes:
      supported_type (dict): Supported output style
    """
    self.supported_type = {"file", "nx", "2d_list"}

    self.type = type

    if self.type not in self.supported_type:
      raise Exception('Return type \'{}\' not supported'.format(self.type))

    if self.type == "nx":
      return self.g_nx
    elif self.type == "2d_list":
      return nx.to_numpy_matrix(self.g_nx)

  def acomplete_graph(self):
    pass

