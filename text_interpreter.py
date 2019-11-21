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


class TextInterpreter:
    def __init__(self, file_path):
        self.file = file_path
        self.dict = {}
        self.dictlist = []
        self.newlist = []
        self.list_of_tuples = []
        self.heap = []
        self.codes_dict = {}
        self.codes = []
        self.values = []

    def create_output(self):
        self.read_binary_file()
        self.create_list_of_lists_from_dictionary()
        self.reverse_list_and_create_tuples_and_create_heap()
        self.create_heap_of_nodes_from_heap_of_tuples()
        self.merge_nodes_to_create_new_heap()
        self.create_codes(heapq.heappop(self.heap), [])
        print(self.codes_dict)
        self.create_output_file()

    def read_binary_file(self):
        x = 5
        dictionary_of_values = {}
        with open(self.file, "rb") as f:
            byte = f.read(3)
            while byte:
                byte = f.read(3)
                decimal = int.from_bytes(byte, byteorder='little', signed=True)
                self.values.append(decimal)
                if decimal not in dictionary_of_values.keys():
                    dictionary_of_values[decimal] = 1
                else:
                    dictionary_of_values[decimal] += 1
        self.dict = dictionary_of_values

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
                print(temp_code)
                self.codes_dict[node.value] = temp_code # need to keep running string for left and right traversal
                temp_code = None
            self.codes.append("0")
            self.create_codes(node.left, self.codes)
            self.codes.pop()
            self.codes.append("1")
            self.create_codes(node.right,self.codes)
            self.codes.pop()

    def create_output_file(self):
        string_output = ""
        print(os.getcwd())
        with open("app/outputs/output.bin", 'wb') as output:
            for value in self.values:
                # pad string to multiple of 8
                padded = len(self.codes_dict[value]) % 8 * "0" + self.codes_dict[value]
                byte_value = str.encode(padded)
                output.write(byte_value)
                # create bytes 1 byte = 8 bits
                # write byte to output binary file
                string_output += self.codes_dict[value]
        output.close()




#print(sample.list_of_tuples)
#sample.create_heap_of_nodes_from_heap_of_tuples()
#sample.merge_nodes_to_create_new_heap()
#print (sample.heap)
# while sample.heap:
#     current = heapq.heappop(sample.heap)
#     print(
#         current.value,
#         current.frequency,
#         current.left.value,
#         current.left.frequency,
#         current.right.value,
#         current.right.frequency
#     )


