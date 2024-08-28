class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert_at_beg(head,data):
    newnode = Node(data)
    newnode.data = data
    newnode.next = head
    return newnode

def insert_at_end(head,data):
    newnode = Node(data)
    newnode.data = data
    newnode.next = None

    if head is None:  # Handle the case of an empty list
        head = newnode  # Make the new node the head of the list
        return head

    ptr = head
    while ptr.next:
        ptr = ptr.next

    ptr.next = newnode
    return head

def insert_after_node(head,data,node):
    newnode = Node(data)
    newnode.next = None
    current = head
    while current:
        if current.data == node:
            newnode.next = current.next
            current.next = newnode
            current = newnode

        current = current.next

    return head
def display(head):
    current = head
    while current:
        print(" ",current.data)
        current = current.next


    print("NULL")



head = None
while 1:
    data = int(input("Enter the value of data :: "))
    head = insert_at_end(head, data)
    choice = int(input("Do you want to continue :: "))
    if choice==0:
        break
    else:
        continue

print("The Linked List :: ")
display(head)
print("For Insert At beginning write 1 and For insert after a node write 2")
choice = int(input("Enter the choice :: "))

if choice == 1:
    data = int(input("Enter the data insert at beginning:: "))
    head = insert_at_beg(head, data)
    print("After Inserting the data At beginning :: ")
    display(head)

elif choice == 2:
    node = int(input("Enter the node :: "))
    data = int(input("Enter the data of new node:: "))
    head = insert_after_node(head, data, node)
    print("After Inserting the data  :: ")
    display(head)
