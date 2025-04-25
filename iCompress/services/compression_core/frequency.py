class AlphabetFrequency:
    def __init__(self, file_content):
        self.file_content = file_content
        self.frequency = {}

    def get_alphabet_frequency_in_file(self):
        for alphabet in self.file_content:
            if alphabet in self.frequency:
                self.frequency[alphabet] += 1
            else:
                self.frequency[alphabet] = 1
        return self.frequency