#!/usr/bin/env python
import networkx as nx

class generate:
  """Generate various graph

  Attributes:
    type (string): Which graph type to generate.
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
        - file
        - networkx
        - 2d_list
  """

  def __init__(self, type, out="nx", **kwargs):
    """Init class

    Attributes:
      supported_type (dict): Supported graph type correspond to its function pointer
      supported_out (dict): Supported output style
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
    self.supported_out = {"file", "nx", "2d_list"}

    self.type = type
    self.out = out

    # Check supported
    if self.type not in self.supported_type:
      raise Exception('Type \'{}\' not supported'.format(self.type))
    if self.out not in self.supported_out:
      raise Exception('Return type \'{}\' not supported'.format(self.out))
    pass

