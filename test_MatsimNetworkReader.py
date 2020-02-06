from unittest import TestCase

import MatsimNetworkReader


class TestNetworkHandler(TestCase):

    def test(self):
        network = MatsimNetworkReader.read('C:\\Users\\Janekdererste\\PycharmProjects\\matsim-analysis\\test.xml')
        for link in network.links().values():
            print(link.id)
