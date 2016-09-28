var addTwoNumbers = function(l1, l2) {
    var carry = 0;
    var head = new ListNode(-1);
    var pre = head;
    while(l1 || l2 || carry){
        var s = carry;
        if(l1){
            s += l1.val;
            l1 = l1.next;
        }
        if(l2){
            s += l2.val;
            l2 = l2.next;
        }
        if(s >= 10){
            s -= 10;
            carry = 1;
        } else {
            carry = 0;
        }
        pre.next = new ListNode(s);
        pre = pre.next;
    }
    if(!head.next){
        head.next = new ListNode(0)
    }
    return head.next;
};
