import heapq
import os


class Node:
    def __init__(self, frequency,value):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.value = value

    def __lt__(self, other):
        if other is None:
            return -1
        else:
            return self.frequency < other.frequency


class Huffman:
    def __init__(self, file_path):
        self.file = file_path
        self.dict = {}
        self.dictionary_of_values = {}
        self.dictlist = []
        self.newlist = []
        self.list_of_tuples = []
        self.heap = []
        self.codes_dict = {}
        self.codes = []
        self.values = []
        self.initial_byte_counter = 0
        self.original_size = os.path.getsize(file_path)

    def create_output(self):
        self.read_binary_file()
        self.create_list_of_lists_from_dictionary()
        self.reverse_list_and_create_tuples_and_create_heap()
        self.create_heap_of_nodes_from_heap_of_tuples()
        self.merge_nodes_to_create_new_heap()
        self.create_codes(heapq.heappop(self.heap), [])
        ratio = self.create_output_file()
        return ratio

    def read_binary_file(self):
        with open(self.file, "rb") as f:
            byte = f.read(3)
            while byte:
                byte = f.read(3)
                self.initial_byte_counter += 1
                decimal = int.from_bytes(byte, byteorder='big', signed=True)
                self.values.append(decimal)
                if decimal not in self.dictionary_of_values.keys():
                    self.dictionary_of_values[decimal] = 1
                else:
                    self.dictionary_of_values[decimal] += 1
        self.dict = self.dictionary_of_values

    def create_list_of_lists_from_dictionary(self):
        for key1, value1 in self.dict.items():
            temp = [key1, value1]
            self.dictlist.append(temp)

    def reverse_list_and_create_tuples_and_create_heap(self):
        for each in self.dictlist:
            self.newlist.append(each[::-1])
        self.list_of_tuples = [tuple(l) for l in self.newlist]
        heapq.heapify(self.list_of_tuples)

    def create_heap_of_nodes_from_heap_of_tuples(self):
        for individual_tuple in self.list_of_tuples:
            new_node = Node(individual_tuple[0], individual_tuple[1])
            heapq.heappush(self.heap, new_node)

    def merge_nodes_to_create_new_heap(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged_node = Node(node1.frequency + node2.frequency, None)
            merged_node.left = node1
            merged_node.right = node2
            heapq.heappush(self.heap, merged_node)

    # in order depth first search of min heap
    def create_codes(self, node,current_code):
        if node:
            if node.left is None and node.right is None:
                temp_code = (','.join(self.codes)).replace(',','')
                self.codes_dict[node.value] = temp_code # need to keep running string for left and right traversal
                temp_code = None
            self.codes.append("0")
            self.create_codes(node.left, self.codes)
            self.codes.pop()
            self.codes.append("1")
            self.create_codes(node.right,self.codes)
            self.codes.pop()

    def bitstring_to_bytes(s):
        return int(s, 2).to_bytes(len(s) // 8, byteorder='big')

    def create_output_file(self):
        string_output = ""
        with open("app/outputs/output.bin", 'wb') as output:
            for value in self.values:
                # pad string to multiple of 8
                padded = len(self.codes_dict[value]) % 8 * "0" + self.codes_dict[value]
                byte_value = str.encode(padded)
                output.write(byte_value)
                string_output += self.codes_dict[value]
        output.close()

        count = 0
        for key in self.values:
            count += len(self.codes_dict[key])*self.dictionary_of_values[key]
            print(len(self.codes_dict[key]), "    ", self.dictionary_of_values[key],"     ", (len(self.codes_dict[key])*self.dictionary_of_values[key]))
        print(count/8)
        print("The initial file size was: ", self.initial_byte_counter*3)
        print("The compressed file size is: ", count/8)
        compression_ratio = (self.initial_byte_counter*3)/(count/8)
        print("The compression ratio: ", compression_ratio)
        return compression_ratio


sample = Huffman("/Users/vasavivempati/Downloads/sample_ecg_raw 3.bin")
sample.create_output()


