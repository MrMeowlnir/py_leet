from collections import defaultdict
class Node(object):
    def __init__(self):
        self.keys = set([])
        self.prev, self.next = None, None

    def add(self, key):
        self.keys.add(key)

    def remove(self, key):
        self.keys.remove(key)

    def getKey(self):
        if self.keys:
            res = self.keys.pop()
            self.add(res)
            return res
        return None

    def count(self):
        return len(self.keys)

    def isEmpty(self):
        return self.count() == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfter(self, key):
        node = Node()
        temp = key.next
        key.next, node.prev = node, key
        node.next, temp.prev = temp, node
        return node

    def insertBefore(self, key):
        return self.insertAfter(key.prev)

    def remove(self, key):
        prev = key.prev
        prev.next, key.next.prev = key.next, prev

    def getHead(self):
        return self.head.next

    def getTail(self):
        return self.tail.prev

    def getSentHead(self):
        return self.head

    def getSentTail(self):
        return self.tail


class AllOne(object):

    def __init__(self):
        self.dll = DoubleLinkedList()
        self.count = defaultdict(int)
        self.node_freq = {0: self.dll.getSentHead()}

    def remove_key_pfreq(self, pfreq, key):
        node = self.node_freq[pfreq]
        node.remove(key)
        if node.isEmpty():
            self.dll.remove(node)
            self.node_freq.pop(pfreq)

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        self.count[key] += 1
        curfreq = self.count[key]
        pfreq = self.count[key] - 1
        if not (curfreq in self.node_freq):
            self.node_freq[curfreq] = self.dll.insertAfter(self.node_freq[pfreq])
        self.node_freq[curfreq].add(key)
        if pfreq > 0:
            self.remove_key_pfreq(pfreq, key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.count:
            self.count[key] -= 1
            curfreq = self.count[key]
            pfreq = self.count[key] + 1
            if self.count[key] == 0:
                self.count.pop(key)
            if curfreq != 0:
                if not (curfreq in self.node_freq):
                    self.node_freq[curfreq] = self.dll.insertBefore(self.node_freq[pfreq])
                self.node_freq[curfreq].add(key)
            self.remove_key_pfreq(pfreq, key)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.dll.getTail().count() > 0:
            return self.dll.getTail().getKey()
        return ''

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.dll.getHead().count() > 0:
            return self.dll.getHead().getKey()
        return ''


if __name__ == "__main__":
    allOne = AllOne()
    allOne.inc('hello')
    allOne.inc('goodbye')
    allOne.inc('hello')
    allOne.inc('hello')
    print(allOne.getMaxKey())
    print(allOne.getMinKey())
    allOne.inc('leet')
    print(allOne.getMaxKey())
    print(allOne.getMinKey())

    case2 = AllOne()
    case2.inc('a')
    case2.inc('b')
    case2.inc('c')
    case2.inc('d')
    case2.inc('a')
    case2.inc('b')
    case2.inc('c')
    case2.inc('d')
    case2.inc('a')
    case2.inc('d')
    case2.inc('d')
    case2.inc('a')
    print(case2.getMinKey())

    case3 = AllOne()
    case3.inc('hello')
    case3.inc('goodbye')
    case3.inc('hello')
    case3.inc('hello')
    print(case3.getMaxKey())
    case3.inc('leet')
    case3.inc('code')
    case3.inc('leet')
    case3.dec('hello')
    case3.inc('leet')
    case3.inc('code')
    case3.inc('code')
    print(case3.getMaxKey())
