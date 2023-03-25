import json
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CheckCircularLL:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def get_length(self):
        count=1
        current = self.head
        while current.next:
            count+=1
            current=current.next
        return count

    def appendAndPointNext(self,data, nextCount):
        new_node = Node(data)
        count=1
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_ptr = self.head
            while count<nextCount:
                count= count + 1
                new_ptr = new_ptr.next
            new_node.next = new_ptr
        else:
            self.head = new_node

        
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def checkIfCircular(self):
        nodeDataDict = {}
        current = self.head

        while current.next:
            if (hex(id(current.next)) in nodeDataDict):
                print("Circular")
                break
                # return
            else:
                nodeDataDict[current] = current.next
            current = current.next
        data = json.dumps(nodeDataDict, indent=4)
        print(data)
        return
        print("Not circular")

e1 = Node(1)
ll = CheckCircularLL(e1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.appendAndPointNext(5,2)
ll.checkIfCircular()
# ll.print_list()