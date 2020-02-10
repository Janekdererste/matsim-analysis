from unittest import TestCase

import MatsimEventsReader

actTypes = {'actstart', 'actend', 'departure', 'arrival', 'travelled', 'PersonEntersVehicle', 'PersonLeavesVehicle',
            'vehicle enters traffic', 'vehicle leaves traffic', 'left link', 'entered link'}


class TestEventsHandler(TestCase):

    def test_parsing(self):
        callback = self.callback
        MatsimEventsReader.read('./test_events.xml.gz', callback)

    def callback(self, time, type, attrs):
        self.assertLessEqual(21510, time)
        self.assertTrue(type in actTypes, 'type ' + type + ' was not in act types')
