from abc import ABC, abstractmethod

# Implementor
class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

# Concrete Implementors
class Radio(Device):
    def __init__(self):
        self.on = False
        self.volume = 50
        self.channel = 1

    def is_enabled(self):
        return self.on

    def enable(self):
        self.on = True

    def disable(self):
        self.on = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

class TV(Device):
    def __init__(self):
        self.on = False
        self.volume = 30
        self.channel = 1

    def is_enabled(self):
        return self.on

    def enable(self):
        self.on = True

    def disable(self):
        self.on = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

# Abstraction
class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)

# Refined Abstraction
class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)

def main():
    radio = Radio()
    tv = TV()

    remote = Remote(radio)
    advanced_remote = AdvancedRemote(tv)

    print("Usando el control remoto simple con la radio:")
    remote.toggle_power()
    print(f"Radio encendida: {radio.is_enabled()}")
    remote.volume_up()
    print(f"Volumen de la radio: {radio.get_volume()}")

    print("\nUsando el control remoto avanzado con la TV:")
    advanced_remote.toggle_power()
    print(f"TV encendida: {tv.is_enabled()}")
    advanced_remote.volume_up()
    advanced_remote.volume_up()
    print(f"Volumen de la TV: {tv.get_volume()}")
    advanced_remote.mute()
    print(f"Volumen de la TV después de silenciar: {tv.get_volume()}")

if __name__ == "__main__":
    main()
