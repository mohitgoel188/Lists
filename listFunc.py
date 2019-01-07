class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def mergeLists(head1,head2):
    """ To merge two lists in sorted order.\n
            [TC=O(n) or O(m)/SC=O(1)]
    """
    if not head1:
        return head2
    if not head2:
        return head1
    prevNode=None
    combHead=head1
    while(head1 and head2):
        if head1.val<=head2.val:
            prevNode=head1
            head1=head1.next
        else:
            nextNode=head2.next
            head2.next=head1
            if not prevNode:
                combHead=head2  
            else:
                prevNode.next=head2
            prevNode=head2
            head2=nextNode
    if head2:
        prevNode.next=head2
    return combHead

def isSame(head1,head2):
    """ To check if two lists are some(elementwise and lengthwise).\n
            [TC=O(n)/SC=O(1)]
    """
    while head1 and head2:
        if head1.val!=head2.val:
            return False
        head1=head1.next
        head2=head2.next
    if head1 or head2:
        return False
    return True

class List:
    """ A Class to implement singly linked lists and associated functions""" 
    def __init__(self,lst):
        self.head=Node(lst[0])
        self.len=len(lst)
        head=self.head
        for i in lst[1:]:
            head.next=Node(i)
            head=head.next

    def retEnd(self,head=None):
        """ To return the end node of linked list.  [TC=O(n)/SC=O(1)]"""
        if not head:            
            head=self.head
        while(head.next):
            head=head.next
        return head

    def insertNode(self,val,beg=True,sorted=False,doSort=False):
        """ To insert a node in the linked list at:\n
            begining: default       [TC=O(n)/SC=O(1)]\n
            ending: pass->beg=False [TC=O(n)/SC=O(1)]\n
            in sorted order: if list is sorted pass->sorted=True    [TC=O(n)/SC=O(1)]\n
                             else pass->sorted=True,doSort=True     [TC=O(nlogn)/SC=O(n)]
        """
        if sorted:
            if doSort:
                self.head=self.mergeSortList(self.head)
            self.head=mergeLists(self.head,Node(val))
            return
        if beg:
            newnode=Node(val,self.head)
            # newnode.next=self.head
            self.head=newnode
            self.len+=1
        else:
            newnode=Node(val)
            head=self.head
            while(head.next):
                head=head.next
            head.next=newnode
            self.len+=1

    def deleteNode(self,beg=True,rand=False,val=None):
        """ To delete a node in the linked list from:\n
            begining: default       [TC=O(1)/SC=O(1)]\n
            ending: pass->beg=False [TC=O(n)/SC=O(1)]\n
            randomly with some VALUE: pass->rand=True,val=VALUE [TC=O(n)/SC=O(1)]
        """
        head=self.head
        if rand:
            if head.val==val:
                return self.deleteNode()
            while(head.next):
                if head.next.val==val:
                    temp=head.next
                    head.next=temp.next
                    del temp
                    self.len-=1
                    return True
            return False
        if beg:
            if head.next:
                self.head=head.next
            else:
                self.head=None
            del head
            self.len-=1
        else:
            if self.len==1:
                del self.head
                self.head=None
                self.len-=1
            while(head.next):
                if head.next.next:
                    head=head.next
                else:
                    break
            del head.next
            head.next=None
            self.len-=1
        return True

    def reverse(self,head=None,retEndNode=False):
        """ To reverse the linked list.\n
            [TC=O(n)/SC=O(1)]
        """
        if not head:
            head=self.head
        prevNode=None
        nextNode=None
        combHead=head
        newEnd=head
        while(head):
            if head.next:
                nextNode=head.next
                head.next=prevNode
                prevNode=head
                head=nextNode
            else:
                head.next=prevNode
                combHead=head
                # head=head.next
                break
        if retEndNode:
            return combHead,newEnd
        else:
            return combHead

    def reverseK(self,head=None,k=0):
        """ To reverse the linked list in group of k size.\n
            [TC=O(n)/SC=O(1)]
        """
        if not head:
            head=self.head
        if k==1:
            return self.reverse(head)
        count=1
        start=head
        combHead=None
        prevNode=None
        while(head):
            if count==k:
                nextNode=head.next
                head.next=None
                newBeg,head=self.reverse(start,retEndNode=True)
                if not combHead:
                    combHead=newBeg
                if not prevNode:
                    prevNode=head
                else:
                    prevNode.next=newBeg
                    prevNode=head
                head.next=nextNode
                start=nextNode
                count=0
            if head.next:
                head=head.next
                count+=1
            else:
                if count!=0:
                    newBeg,head=self.reverse(start,retEndNode=True)
                    if not combHead:
                        combHead=newBeg
                    if not prevNode:
                        prevNode=head
                    else:
                        prevNode.next=newBeg
                        prevNode=head
                    # head.next=nextNode
                    # start=nextNode
                    # count=0
                break
        return combHead

    def isPalindrome(self,head=None):
        """A function to check if the list nodes form palindrome or not.\n
           [TC=O(n)/SC=O(1)]
        """
        if not head:
            head=self.head
        midHead=self.midNode(head,sever=True)
        midHead=self.reverse(midHead)
        if isSame(head,midHead):
            endNode=self.retEnd(head)
            endNode.next=self.reverse(midHead)
            return True
        else:
            endNode=self.retEnd(head)
            endNode.next=self.reverse(midHead)
            return False
        
    def evenOdd(self,head=None):
        """A function to segregate even and odd numbers in the linked list.\n
           [TC=O(n)/SC=O(1)]
        """
        if not head:
            head=self.head
        oddHead=None
        prevNode=None
        combHead=head
        while(head):
            if head.val%2!=0:
                if not oddHead:
                    oddHead=head
                    head2=oddHead
                else:
                    head2.next=head
                    head2=head
                if not prevNode:
                    combHead=head.next
                else:
                    if head.next:
                        prevNode.next=head.next
                    else:
                        prevNode.next=None
                head.next=None
                if prevNode:
                    head=prevNode.next
                else:
                    head=combHead
            else:
                prevNode=head
                head=head.next
        prevNode.next=oddHead
        return combHead

    def mergeSortList(self,head):
        """ To sort the linked list inplace.\n
            [TC=O(nlogn)/SC=O(n)]"""
        if not head or not head.next:
            return head
        secondHead=self.midNode(head,True)
        head=self.mergeSortList(head)
        secondHead=self.mergeSortList(secondHead)
        return mergeLists(head,secondHead)

    def show(self,beg=True,head=None):
        """ Display the linked list from:\n
            begining: default                       [TC=O(n)/SC=O(1)]\n
            ending: pass->beg=False,head=OBJ.head   [TC=O(n)/SC=O(n)]\n 
        """
        if beg:
            head=self.head
            while(head):
                print(f"->{head.val}",end='')
                head=head.next
            print()
        else:
            if head.next:
                print(f"->{self.show(False,head.next)}",end='')
            return head.val

    def midNode(self,head,sever=False):
        """ To return the middle node of linked list.\n
            if sever=True then break list from mid.\n
            [TC=O(n)/SC=O(1)]
        """
        if head:
            slow=head
            fast=head
            prevNode=None
            while slow and fast:
                fast=fast.next
                if fast:
                    fast=fast.next
                else:
                    break
                prevNode=slow
                slow=slow.next
            if sever and prevNode.next:
                prevNode.next=None
            return slow

    def loopList(self,findStart=False,findLength=False):
        """ A function which finds whether the passed list contain cycle or not.\n
            Parameters:\n
            lst: Head of singly linked list which needed to be checked.   \n
                (type-List[ADT])\n
            findStart: To return the start of the cycle(if found)\n
                    (type-bool)\n
            findLength: To return the length of the cycle(if found)\n
                    (type-bool)\n
            [TC=O(n)/SC=O(1)]
        """
        cycleExist=False
        count=None
        start=None
        head=self.head
        slow=head
        fast=head
        while(slow and fast):
            # print(f"slow:{slow.val}\tfast:{fast.val}")
            fast=fast.next
            if slow==fast:
                cycleExist=True
                break
            if not fast:
                break
            fast=fast.next
            if slow==fast:
                cycleExist=True
                break
            slow=slow.next
        if cycleExist and findLength:
            # print('FindLength')
            count=1
            # print(f"slow:{slow.val}\tfast:{fast.val}")
            slow=slow.next
            while(slow!=fast):
                # print(f"slow:{slow.val}\tfast:{fast.val}")
                slow=slow.next
                count+=1
        if cycleExist and findStart:
            # print('FindStart')
            slow=head
            while(slow!=fast):
                # print(f"slow:{slow.val}\tfast:{fast.val}")
                slow=slow.next
                fast=fast.next
                fast=fast.next
            start=slow
        return (cycleExist,start,count)

def main():
    lst=List([5,2,7,4,11,33,22,8])
    print('List:')
    lst.show()

    print('From end:')
    print(f"->{lst.show(False,lst.head)}")
    
    print('Inserting 0 at beg...')
    lst.insertNode(0)
    lst.show()
    print('Inserting 9 at end...')
    lst.insertNode(9,beg=False)
    lst.show()
    
    print("Reversing the linked list...")
    lst.head=lst.reverse()
    lst.show()
    
    print(f"MidNode of linked list: {lst.midNode(lst.head).val}")
    
    print("Sorting the linked list...")
    lst.head=lst.mergeSortList(lst.head)
    lst.show()
    
    print(f"Inserting 10 in sorted order...")
    lst.insertNode(10,sorted=True)
    lst.show()

    print("Reversing list in pairs...")
    lst.head=lst.reverseK(lst.head,k=2)
    lst.show()
    
    print("Seprating even odd values...")
    lst.head=lst.evenOdd(lst.head)
    lst.show()
    
    print("Checking if list is palindrome...")
    print(lst.isPalindrome(lst.head))
    lst=List([1,2,3,3,2,1])
    lst.show()
    print("Checking if list is palindrome...")
    print(lst.isPalindrome(lst.head))
    
    print("Checking for loop...")
    if not lst.loopList()[0]:
        print('No loop found.')
    print(f"Joining end of link list to node with value {lst.head.next.next.val}...")
    end=lst.retEnd()
    end.next=lst.head.next.next
    print("Checking for loop...")
    loop,start,length=lst.loopList(findStart=True,findLength=True)
    if loop:
        print(f"Loop found at node {start.val} and has length {length}")

if __name__ == '__main__':
    main()