import xml.sax
from xml import sax


class Entity:

    def __init__(self, entity_id):
        self.id = entity_id


class Node(Entity):

    def __init__(self, entity_id, x, y):
        super().__init__(entity_id)
        self.x = x
        self.y = y


class Link(Entity):

    def __init__(self, entity_id, from_node, to_node, length, capacity, freespeed, permlanes, modes):
        super().__init__(entity_id)
        self.modes = modes
        self.permlanes = permlanes
        self.freespeed = freespeed
        self.capacity = capacity
        self.length = length
        self.to_node = to_node
        self.from_node = from_node


class Network:

    def links(self):
        return self._links.copy()

    def nodes(self):
        return self._nodes.copy()

    def __init__(self, nodes, links):
        self._nodes = nodes
        self._links = links


class NetworkHandler(xml.sax.ContentHandler):
    NODE = 'node'
    NODES = 'nodes'
    LINK = 'link'
    LINKS = 'links'

    def links(self):
        return self._links.copy()

    def nodes(self):
        return self._nodes.copy()

    def __init__(self):
        super().__init__()
        self._nodes = {}
        self._links = {}

    def startElement(self, name, attrs):
        if name == NetworkHandler.NODE:
            node = Node(attrs.get('id'), attrs.get('x'), attrs.get('y'))
            self._nodes[node.id] = node
        elif name == NetworkHandler.LINK:
            link = Link(attrs.get('id'), self._nodes[attrs.get('from')], self._nodes[attrs.get('to')],
                        attrs.get('length'), attrs.get('capactiy'), attrs.get('freespeed'), attrs.get('permlanes'),
                        str(attrs.get('modes')).split(','))
            self._links[link.id] = link
        else:
            print('start element', name, ' ', str(attrs))


def read(filepath):
    handler = NetworkHandler()
    sax.parse(filepath, handler)
    return Network(handler.nodes(), handler.links())
