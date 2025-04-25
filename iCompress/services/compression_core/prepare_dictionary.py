class PrepareDictionary:
    def __init__(self, frequency_tree):
        self.frequency_tree = frequency_tree
        self.dictionary = {}

    def build_dictionary(self, node, code):
        if not node:
            return None
        if node.left == None and node.right == None:
            self.dictionary[node.key] = code
            return
        self.build_dictionary(node.left, code+"0")
        self.build_dictionary(node.right, code+"1")

    def get_dictionary(self):
        self.build_dictionary(self.frequency_tree, "")
        return self.dictionary