import heapq

def min_packet_combination_cost(packet_lengths):
    heapq.heapify(packet_lengths)

    total_cost = 0

    while len(packet_lengths) > 1:
        smallest1 = heapq.heappop(packet_lengths)
        smallest2 = heapq.heappop(packet_lengths)

        combined_packet_length = smallest1 + smallest2
        total_cost += combined_packet_length

        heapq.heappush(packet_lengths, combined_packet_length)

    return total_cost

packet_lengths = list(map(int, input().split()))
result = min_packet_combination_cost(packet_lengths)
print(result)
