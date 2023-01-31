from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3

class SimpleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        self.logger.info("switch_features_handler: %s", msg)

    @set_ev_cls(ofp_event.EventOFPHello, MAIN_DISPATCHER)
    def hello_handler(self, ev):
        self.logger.info("Received Hello message")

        # Measure performance
        start = time.time()
        headers_received = 0
        while headers_received < 20:
            header = ev.msg.pack()
            headers_received += 1
        end = time.time()

        # Calculate elapsed time
        elapsed = end - start

        # Print results
        self.logger.info("Time elapsed: {:.2f} seconds".format(elapsed))
        self.logger.info("Bandwidth: {:.2f} MBps".format(20 * 8 / (10**6 * elapsed)))
