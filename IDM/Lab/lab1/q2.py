import argparse
from itertools import chain, combinations


def joinset(itemset, k):
    return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])

def subsets(itemset):
    return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])
    
def itemset_from_data(data):
    itemset = set()
    transaction_list = list()
    for row in data:
        transaction_list.append(frozenset(row))
        for item in row:
            if item:
                itemset.add(frozenset([item]))
    return itemset, transaction_list


def itemset_support(transaction_list, itemset, min_support=0):
    len_transaction_list = len(transaction_list)
    l = [
        (item, float(sum(1 for row in transaction_list if item.issubset(row)))/len_transaction_list) 
        for item in itemset
    ]
    return dict([(item, support) for item, support in l if support >= min_support])

def freq_itemset(transaction_list, c_itemset, min_support):
    f_itemset = dict()

    k = 1
    while True:
        if k > 1:
            c_itemset = joinset(l_itemset, k)
        l_itemset = itemset_support(transaction_list, c_itemset, min_support)
        if not l_itemset:
            break
        f_itemset.update(l_itemset)
        k += 1

    return f_itemset    


def apriori(data, min_support, min_confidence):
    
    itemset, transaction_list = itemset_from_data(data)
    f_itemset = freq_itemset(transaction_list, itemset, min_support)
    rules = list()
    for item, support in f_itemset.items():
        if len(item) > 1:
            for A in subsets(item):
                B = item.difference(A)
                if B:
                    A = frozenset(A)
                    AB = A | B
                    confidence = float(f_itemset[AB]) / f_itemset[A]
                    if confidence >= min_confidence:
                        rules.append((A, B, confidence))    
    return rules, f_itemset


def print_report(rules, f_itemset):
    print('closed_frequent_itemset\n')
    for item, support in sorted(f_itemset.items(), key=lambda (item, support): support):
        print('[I] {} : {}'.format(tuple(item), round(support, 4)))

    print('')
    print('Association rules\n')
    for A, B, confidence in sorted(rules, key=lambda (A, B, confidence): confidence):
        print('[R] {} => {} : {}'.format(tuple(A), tuple(B), round(confidence, 4))) 


def data_from_csv(filename):
    f = open(filename, 'rU')
    for l in f:
        row = map(str.strip, l.split(' '))
        yield row

def main():
    print("Enter partition 1 filename :")
    part1=raw_input()
    # print(filename)
    print("Enter partition 2 filename :")
    part2=raw_input()
    print("Enter integrated filename :")
    filename=raw_input()
    print("Enter Min support value (0-1) ")
    min_support=float(raw_input())
    print("Enter the Min confidence value ")
    min_confidence=float(raw_input())
    data = data_from_csv(filename)
    data1=data_from_csv(part1)
    data2=data_from_csv(part2)
    rules, itemset = apriori(data, min_support, min_confidence)
    rules1, itemset1 = apriori(data1, min_support, min_confidence)
    rules2, itemset2 = apriori(data2, min_support, min_confidence)
    print("=====================Report of Integrated dataset====================")
    print_report(rules, itemset)
    print("=====================Report of partition 1 dataset====================")
    print_report(rules1, itemset1)
    print("=====================Report of partition 2 dataset====================")
    print_report(rules2, itemset2)


if __name__ == '__main__':
    main()