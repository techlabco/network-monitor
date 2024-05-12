# network_monitor.py

import packet_capture
import data_analysis
import visualization

def main():
    # Capture network packets
    packets = packet_capture.capture_packets()

    # Analyze captured packets
    analysis_result = data_analysis.analyze_packets(packets)

    # Visualize analysis result
    visualization.plot_results(analysis_result)

if __name__ == "__main__":
    main()
