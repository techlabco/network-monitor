import unittest
from src import data_analysis

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.data = [
            {'source_ip': '192.168.1.1', 'destination_ip': '192.168.1.2', 'protocol': 'TCP', 'size': 100},
            {'source_ip': '192.168.1.2', 'destination_ip': '192.168.1.1', 'protocol': 'UDP', 'size': 150},
            {'source_ip': '192.168.1.1', 'destination_ip': '192.168.1.3', 'protocol': 'TCP', 'size': 120},
            {'source_ip': '192.168.1.3', 'destination_ip': '192.168.1.1', 'protocol': 'TCP', 'size': 200},
            {'source_ip': '192.168.1.2', 'destination_ip': '192.168.1.3', 'protocol': 'UDP', 'size': 180},
        ]

    def test_total_packets(self):
        total_packets = data_analysis.calculate_total_packets(self.data)
        self.assertEqual(total_packets, 5)

    def test_average_packet_size(self):
        average_size = data_analysis.calculate_average_packet_size(self.data)
        self.assertEqual(average_size, 150)

    def test_most_common_protocol(self):
        most_common_protocol = data_analysis.find_most_common_protocol(self.data)
        self.assertEqual(most_common_protocol, 'TCP')

if __name__ == '__main__':
    unittest.main()
