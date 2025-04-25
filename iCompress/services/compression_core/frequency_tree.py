import heapq

class Node:
    def __init__(self, key, frequency, left, right):
        self.key = key
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other_node):
        return self.frequency < other_node.frequency

    def __eq__(self, other_node):
        if other_node is not None:
            return self.frequency == other_node.frequency
        return False

class FrequencyTree:
    def __init__(self, alphabets_frequency):
        self.alphabets_frequency = alphabets_frequency
        self.heap = []

    def build_tree(self):
        for alphabet in self.alphabets_frequency:
            node = Node(alphabet, self.alphabets_frequency[alphabet], None, None)
            heapq.heappush(self.heap, node)
        
        while len(self.heap) != 1:
            self.merge_two_nodes()
        
        return heapq.heappop(self.heap)
    
    def merge_two_nodes(self):
        node1 = heapq.heappop(self.heap)
        node2 = heapq.heappop(self.heap)
        merged_node = Node(None, node1.frequency+node2.frequency, node1, node2)
        heapq.heappush(self.heap, merged_node)