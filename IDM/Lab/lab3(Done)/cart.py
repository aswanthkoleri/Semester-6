from math import log2
from itertools import combinations


attrs = []
class_label = ''
attributes = {}

with open('./resources/info.txt', 'r') as f:
    lines = f.readlines()
    attr = lines[0].strip().split(',')
    class_label = attr[-1]
    attrs = attr

    for i in range(1, len(lines)):
        temp = lines[i].split(':')
        key = temp[0].strip()
        values = list(map(lambda x: x.strip(), temp[1].strip().split(',')))
        attributes[key] = values

data = []

with open('./resources/data.txt', 'r') as fp:
    lines = [line.rstrip('\n') for line in fp]
    data = list(map(lambda x: x.split(','), lines))

def gini(D):
    total = len(D)
    result = 1
    idx = attrs.index(class_label)
    counts = {}

    for element in D:
        label = element[idx]

        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1

    for v in counts.values():
        result = result - ((v / total) ** 2)

    return result


def gini_a(D, attr, split_values):
    total = len(D)
    idx = attrs.index(attr)
    counts = {'in': 0, 'out': 0}
    result = 0

    for element in D:
        label = element[idx]

        if label in split_values:
            counts['in'] += 1
        else:
            counts['out'] += 1

    D_j = list(filter(lambda x: x[idx] in split_values, D))
    gini_Dj = gini(D_j)
    result = result + ((counts['in'] / total) * gini_Dj)

    D_k = list(filter(lambda x: x[idx] not in split_values, D))
    gini_Dk = gini(D_k)
    result = result + ((counts['out'] / total) * gini_Dk)

    return result


def cart(D, exclude):
    best = ''
    split_values = []
    best_score = 1000

    for i in range(len(attrs) - 1):
        if attrs[i] not in exclude:
            attr_values = attributes[attrs[i]]
            # print(attr_values)
            for k in range(1, (len(attr_values) // 2) + 1):
                subsets = list(combinations(attr_values, k))
                # print(subsets)
                for subset in subsets:
                    gini_i = gini_a(D, attrs[i], subset)

                    if gini_i < best_score:
                        best_score = gini_i
                        best = attrs[i]
                        split_values = subset

    return best, split_values


def print_tree(node, tabs=0):
    print("  " * tabs + node.name)

    if not node.is_leaf:
        for k, v in node.children.items():
            print("  " * tabs + k + ":")
            print_tree(v, tabs + 1)

def cart_parse_tree(node, element):
    label = node.name

    if not node.is_leaf:
        idx = attrs.index(label)
        attr_val = element[idx]

        for k, child in node.children.items():
            split_values = k.split(',')

            if attr_val in split_values:
                # print(label + ' : ' + str(split_values) + ' : ' + attr_val)
                cart_parse_tree(child, element)
    else:
        # print(label)
        pass


class Node:
    def __init__(self, data, exclude):
        self.exclude = exclude
        self.data = data
        self.is_leaf = False

        if self.check_same():
            return

        if len(exclude) == len(attrs) - 1:
            self.majority_class()

            return

        self.cart_selection()

    def check_same(self):
        class_labels = set()
        idx = attrs.index(class_label)

        for elem in self.data:
            class_labels.add(elem[idx])

        if len(class_labels) > 1:
            return False
        else:
            self.is_leaf = True
            self.name = class_labels.pop()

            return True

    def majority_class(self):
        idx = attrs.index(class_label)
        counts = {}

        for element in self.data:
            label = element[idx]

            if label in counts:
                counts[label] += 1
            else:
                counts[label] = 1

        best = ''
        best_score = 0

        for k, v in counts.items():
            if v > best_score:
                best_score = v
                best = k

        self.is_leaf = True
        self.name = best


    def cart_selection(self):
        best_attribute, split_values = cart(self.data, self.exclude)
        self.name = best_attribute
        self.exclude.append(best_attribute)
        self.children = {}

        idx = attrs.index(self.name)
        attr_values = attributes[self.name]
        other_split_values = [x for x in attr_values if x not in split_values]

        Dj = list(filter(lambda x: x[idx] in split_values, self.data))
        new_node_a = Node(Dj, self.exclude[:])
        key_a = ','.join(split_values)
        self.children[key_a] = new_node_a

        Dk = list(filter(lambda x: x[idx] in other_split_values, self.data))
        new_node_b = Node(Dk, self.exclude[:])
        key_b = ','.join(other_split_values)
        self.children[key_b] = new_node_b


root = Node(data, [])
print_tree(root)
cart_parse_tree(root, data[1365])