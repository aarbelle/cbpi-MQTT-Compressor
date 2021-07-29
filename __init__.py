from modules import cbpi
from modules.core.props import Property
from modules.plugins.MQTTPlugin import MQTTActor

import time
#@cbpi.actor
class Compressor(object):
    topic = Property.Text("Topic", configurable=True, default_value="", description="MQTT TOPIC")
    delay = Property.Number("Delay (Min)", configurable=True, default_value=3, description="Safty delay for compressor")
    def __init__(self):
      super(Compressor, self).__init__()
      self.last_off = 0 
      self.delay_sec = float(self.delay)*60.
    def on(self, power=100):
        if (self.last_off + self.delay_sec) < time.time():
            super(Compressor, self).on(power)
#        else:
 #           print('Can not start actor for another {} seconds due to delay.'.format(self.last_off + self.delay_sec - time.time()))
    def off(self):
        self.last_off = time.time()
        super(Compressor, self).off()
@cbpi.actor
class MQTTCompressor(Compressor,MQTTActor):
    pass
