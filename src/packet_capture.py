import pyshark

class PacketCapture:
    def __init__(self, interface='eth0', capture_filter=None):
        self.interface = interface
        self.capture_filter = capture_filter

    def start_capture(self):
        print("Starting packet capture on interface:", self.interface)
        try:
            capture = pyshark.LiveCapture(interface=self.interface, display_filter=self.capture_filter)
            return capture
        except pyshark.capture.capture.TSharkCrashException:
            print("Error: TShark crashed. Make sure you have sufficient permissions to capture packets.")

    def stop_capture(self, capture):
        if capture:
            capture.close()
            print("Packet capture stopped.")
        else:
            print("No capture session to stop.")

    def capture_packets(self, num_packets=10):
        capture = self.start_capture()
        packets = []
        try:
            for packet in capture.sniff_continuously(packet_count=num_packets):
                packets.append(packet)
                print(packet)
        except KeyboardInterrupt:
            self.stop_capture(capture)
        return packets

if __name__ == "__main__":
    # Example usage
    packet_capture = PacketCapture(interface='eth0', capture_filter='tcp')
    packets = packet_capture.capture_packets(num_packets=5)
