import unittest
import visualization


class TestVisualization(unittest.TestCase):
    def test_bar_chart(self):
        # Dummy data for testing
        data = {'Website 1': 100, 'Website 2': 200, 'Website 3': 150}

        # Test if bar chart is generated without errors
        try:
            visualization.plot_bar_chart(data)
        except Exception as e:
            self.fail(f"Failed to generate bar chart: {e}")

    def test_line_chart(self):
        # Dummy data for testing
        timestamps = ['2024-05-01 10:00', '2024-05-01 11:00', '2024-05-01 12:00', '2024-05-01 13:00']
        data = {'Website 1': [100, 150, 200, 180], 'Website 2': [80, 120, 170, 150]}

        # Test if line chart is generated without errors
        try:
            visualization.plot_line_chart(timestamps, data)
        except Exception as e:
            self.fail(f"Failed to generate line chart: {e}")


if __name__ == '__main__':
    unittest.main()
