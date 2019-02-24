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
    # print(len(itemset))
    # print(len(transaction_list))
    return itemset, transaction_list


def itemset_support(transaction_list, itemset, min_support=0):
    len_transaction_list = len(transaction_list)
    l = [
        (item, float(sum(1 for row in transaction_list if item.issubset(row)))/len_transaction_list) 
        for item in itemset
    ]
    return dict([(item, support) for item, support in l if support >= min_support])


def hashf(item):
    # val=(item[0]*10+item[1])%7
    # print(val)
    count=0
    val=0
    for i in item:
        if(count==0):
            val=int(i)*10
            conunt=1
        else:
            val=val+int(i)
    return val%7

def freq_itemset(transaction_list, c_itemset, min_support):
    f_itemset = dict()
    print(len(transaction_list))
    k = 1
    hashbucket={}
    frequent_itemset={}
    while True:
        if k > 1:
            c_itemset = joinset(l_itemset, k)
            # print(c_itemset)
            print('--HashBucket--')
            for item in c_itemset:
                counter = 0
                hashvalue=hashf(item)
                for row in transaction_list:
                    if(item.issubset(row)):
                        counter = counter + 1
                for i in range(counter):
                    if(hashvalue in hashbucket):
                        push_item=hashbucket[hashvalue]
                        push_item.append(item)
                        hashbucket.update({hashvalue:push_item})
                    else:
                        push_item=[item]
                        hashbucket.update({hashvalue:push_item})
                print(hashvalue,"---->",counter)
            
            visited=[]
            print('--Frequent Itemset--')
            # print(hashbucket)
            for key, value in hashbucket.iteritems():
                if(len(set(value))==1):
                    if(float(len(value))/len(transaction_list)>min_support):
                        print(value[0],"->",float(len(value))/len(transaction_list))
                else:
                    unique_set=set(value)
                    for p in unique_set:
                        count=value.count(p)
                        if(float(count)/len(transaction_list)>min_support):
                            print(p,"->",float(count)/len(transaction_list))
            break
        l_itemset = itemset_support(transaction_list, c_itemset, min_support)
        if not l_itemset:
            break
        f_itemset.update(l_itemset)
        k += 1
    # print(hashbucket)
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
    print('--Frequent Itemset--')
    for item, support in sorted(f_itemset.items(), key=lambda (item, support): support):
        print('[I] {} : {}'.format(tuple(item), round(support, 4)))

    print('')
    print('--Rules--')
    for A, B, confidence in sorted(rules, key=lambda (A, B, confidence): confidence):
        print('[R] {} => {} : {}'.format(tuple(A), tuple(B), round(confidence, 4))) 


def data_from_dataset(filename):
    f = open(filename, 'rU')
    for l in f:
        row = map(str.strip, l.split(' '))
        yield row

def main():
    print("Enter File Name")
    file_name=raw_input()
    print("Enter Minimum Support")
    supp=float(raw_input())
    print("Enter Minimun Confidence")
    conf=float(raw_input())
    data = data_from_dataset(file_name)
    rules, itemset = apriori(data, supp, conf)


if __name__ == '__main__':
    main()