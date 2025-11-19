def leaky_bucket(input_packets, bucket_size, output_rate):
    """
    Simulates the Leaky Bucket algorithm.
    input_packets : list of integers (packets entering per second)
    bucket_size   : maximum capacity of the bucket
    output_rate   : packets that can be sent per second
    """

    n = len(input_packets)
    print("\n--- Leaky Bucket Simulation ---\n")
    print(f"{'Time(s)':<10}{'Packets Received':<18}{'Packets Sent':<15}{'Packets in Bucket':<20}{'Packets Dropped'}")
    print("-" * 75)

    bucket_content = 0  # Current number of packets in bucket

    for i in range(n):
        # Packets arrive
        incoming = input_packets[i]

        # Check for overflow
        if incoming + bucket_content > bucket_size:
            dropped = (incoming + bucket_content) - bucket_size
            bucket_content = bucket_size
        else:
            dropped = 0
            bucket_content += incoming

        # Send packets (leak)
        if bucket_content >= output_rate:
            sent = output_rate
            bucket_content -= output_rate
        else:
            sent = bucket_content
            bucket_content = 0

        # Display time step
        print(f"{i + 1:<10}{incoming:<18}{sent:<15}{bucket_content:<20}{dropped}")

    # Empty remaining packets in bucket
    time = n
    while bucket_content > 0:
        time += 1
        if bucket_content >= output_rate:
            sent = output_rate
            bucket_content -= output_rate
        else:
            sent = bucket_content
            bucket_content = 0
        print(f"{time:<10}{0:<18}{sent:<15}{bucket_content:<20}{0}")


if __name__ == "__main__":
    print("=== Leaky Bucket Algorithm Simulation ===")

    # User Inputs
    n = int(input("Enter the number of time intervals (e.g. 5): "))
    input_packets = []

    print("\nEnter the number of packets arriving at each second:")
    for i in range(n):
        packets = int(input(f"  Second {i + 1}: "))
        input_packets.append(packets)

    bucket_size = int(input("\nEnter bucket capacity (in packets): "))
    output_rate = int(input("Enter output rate (packets per second): "))

    # Run Simulation
    leaky_bucket(input_packets, bucket_size, output_rate)
