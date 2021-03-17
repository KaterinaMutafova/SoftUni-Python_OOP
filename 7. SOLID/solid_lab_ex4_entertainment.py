from abc import ABC,abstractmethod


class Cable(ABC):
    def connect(self, device):
        pass


class HdmiCable(Cable):
    pass


class RcaCable(Cable):
    pass


class EthernetCable(Cable):
    pass


class PowerCable(Cable):
    pass


class Device(ABC):
    pass





class Entertainment(Device):
    def __init__(self):
        self.hdmi_connector = HdmiCable()
        self.rca_cable = RcaCable()
        self.ethernet_cable = EthernetCable()
        self.power_outlet = PowerCable()



class Television(Device):
    def __init__(self):
        self.hdmi_connector = HdmiCable()
        self.rca_cable = RcaCable()
        self.power_outlet = PowerCable()


class dvd_player(Device):
    def __init__(self):
        self.hdmi_connector = HdmiCable()
        self.power_outlet = PowerCable()


class GameConsole(Device):
    def __init__(self):
        self.hdmi_connector = HdmiCable()
        self.ethernet_cable = EthernetCable()
        self.power_outlet = PowerCable()


class Router(Device):
    def __init__(self):
        self.ethernet_cable = EthernetCable()
        self.power_outlet = PowerCable()


tv = Television()
game_console = GameConsole()

tv.hdmi_connector.connect(game_console.hdmi_connector)
