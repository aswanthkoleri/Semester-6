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
    print('closed_Frequent_itemset\n')
    for item, support in sorted(f_itemset.items(), key=lambda (item, support): support):
        print('[I] {} : {}'.format(tuple(item), round(support, 4)))

    print('')
    print('--Rules--')
    for A, B, confidence in sorted(rules, key=lambda (A, B, confidence): confidence):
        print('[R] {} => {} : {}'.format(tuple(A), tuple(B), round(confidence, 4))) 


def data_from_csv(filename):
    f = open(filename, 'rU')
    for l in f:
        row = map(str.strip, l.split(' '))
        yield row

def main():
    print("Enter the input file")
    filename=raw_input()
    print(filename)
    print("Enter Min support value (0-1) ")
    min_support=float(raw_input())
    print("Enter the Min confidence value ")
    min_confidence=float(raw_input())
    data = data_from_csv(filename)
    rules, itemset = apriori(data, min_support, min_confidence)
    print_report(rules, itemset)


if __name__ == '__main__':
    main()