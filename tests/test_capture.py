import unittest
from packet_capture import PacketCapture

class TestPacketCapture(unittest.TestCase):
    def test_start_capture(self):
        # Initialize PacketCapture instance
        packet_capture = PacketCapture()

        # Test if capture starts successfully
        self.assertTrue(packet_capture.start_capture())

    def test_stop_capture(self):
        # Initialize PacketCapture instance
        packet_capture = PacketCapture()

        # Test if capture stops successfully
        self.assertTrue(packet_capture.stop_capture())

    def test_capture_packets(self):
        # Initialize PacketCapture instance
        packet_capture = PacketCapture()

        # Start capture
        packet_capture.start_capture()

        # Test if packets are captured
        captured_packets = packet_capture.capture_packets()
        self.assertGreater(len(captured_packets), 0)

        # Stop capture
        packet_capture.stop_capture()

if __name__ == '__main__':
    unittest.main()
