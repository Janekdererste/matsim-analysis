from src import MatsimEventsReader


class LinkEnterEvent(MatsimEventsReader.Event):

    def __init__(self, time, attrs):
        super().__init__(time)
        self.vehicleId = attrs['vehicle']
        self.linkId = attrs['link']


class LinkLeaveEvent(MatsimEventsReader.Event):

    def __init__(self, time, attrs):
        super().__init__(time)
        self.vehicleId = attrs['vehicle']
        self.linkId = attrs['link']
