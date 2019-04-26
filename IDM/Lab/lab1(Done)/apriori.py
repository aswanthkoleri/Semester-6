# def join(transactions,joined_itemset,k):
#     # Now we have to join the item set
#     # newSet=list()
#     # for i in joined_itemset:
#     #     for j in joined_itemset:
#     #         temp=list()
#     #         temp.append(i)
#     #         temp.append(j)
#     #         if len(temp)==k:
#     #             newSet.append()
#     # print(newSet)
#     newSet=[]
#     for i in joined_itemset:
#         for j in joined_itemset:
#             temp=i.union(j)
#             # print(temp)
#             if len(temp)==k:
#                 newSet.append(temp)
#     return newSet

# def generateLItemSet(transactions,itemset,min_support,min_confidence):
#     # Total no of transactions 
#     noOfTransactions=len(transactions)
#     # generate an array containing tuple of itemset as first element and support as second element
#     table=[]
#     for item in itemset:
#         # find the support of item in the whole transactions
#         # If item is present in a transaction then it is counted as support 
#         count=0 
#         for transaction in transactions:
#             if item.issubset(transaction):
#                 count+=1
#         if count>=min_support:
#             table.append((item,count))
#     # print(table)
#     return table

# def generateFreqItemSet(transactions,itemset,min_support,min_confidence):
#     k=1
#     # freq_itemset=[]
#     joined_itemset=itemset
#     while True:
#         if k>1:
#             # then we have to join
#             joined_itemset=join(transactions,joined_itemset,k)
#         lItemSet=generateLItemSet(transactions,joined_itemset,min_support,min_confidence)
#         if not lItemSet:
#             break
#         freq_itemset=lItemSet
#         k+=1
#     unique=[]
#     for item,support in freq_itemset:
#         if item not in unique:
#             unique.append(item)
#     return unique
#     # return freq_itemset

# def main():
#     # accept input file
#     filename=input() 
#     f = open(filename, 'r')
#     data=[]
#     for line in f:
#         # row=l
#         data.append(list(map(str.strip,line.split(" "))))
#     # extract each of the transactions in the data
#     transactions=[]
#     temp=set()
#     visited={}
#     for row in data:
#         row.pop()
#         transactions.append(set(row))
#         for i in row:
#             print(i,end=" ")
#             if i not in visited:
#                 temp.add(i)
#                 visited[i]=True
#         itemset=[]
#     print(temp)
#     for i in temp:
#         print(i)
#         itemset.append(set(i))
#     print(itemset)
#     # print(transactions)
#     # print(data)
#     print("Enter min support:")
#     min_support=int(input())
#     print("Enter the min confidence:")
#     min_confidence=int(input())
#     # Now generate the frequent itemset
#     freq_itemset=generateFreqItemSet(transactions,itemset,min_support,min_confidence)
#     print(freq_itemset)
# main()
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
    # Get first itemset and transactions
    itemset, transaction_list = itemset_from_data(data)

    # Get the frequent itemset
    f_itemset = freq_itemset(transaction_list, itemset, min_support)

    # Association rules
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


def data_from_csv(filename):
    f = open(filename, 'rU')
    for l in f:
        row = map(str.strip, l.split(' '))
        yield row


def parse_options():
    optparser = argparse.ArgumentParser(description='Apriori Algorithm.')
    optparser.add_argument(
        '-f', '--input_file',
        dest='filename',
        help='filename containing csv',
        required=True
    )
    optparser.add_argument(
        '-s', '--min_support',
        dest='min_support',
        help='minimum support',
        default=0.25,
        type=float
    )
    optparser.add_argument(
        '-c', '--min_confidence',
        dest='min_confidence',
        help='minimum confidence',
        default=0.5,
        type=float
    )
    return optparser.parse_args()


def main():
    options = parse_options()

    data = data_from_csv(options.filename)
    rules, itemset = apriori(data, options.min_support, options.min_confidence)
    print_report(rules, itemset)


if __name__ == '__main__':
    main()