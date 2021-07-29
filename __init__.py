from modules import cbpi
from modules.plugins.MQTTPlugin import MQTTActor
from modules.plugins.GPIOCompressor import Compressor

@cbpi.actor
class MQTTCompressor(Compressor,MQTTActor):
    pass
