# 2 link list input
# node(係數coef, 指數exp, 指標next)
# newNode(兩者相乘)
# return newNode head node
class ListNode:
    def __init__(self, coef=0, exp=0, next=None):
        self.coef = coef
        self.exp = exp
        self.next = next

def polyMul(poly1, poly2):
    result_head = ListNode()  # 結果多項式的鏈結串列頭節點
    current_result = result_head

    # 外層迴圈遍歷第一個多項式的每一項
    while poly1 is not None:
        current_poly2 = poly2

        # 內層迴圈遍歷第二個多項式的每一項，與第一個多項式的當前項相乘
        while current_poly2 is not None:
            # 計算乘積的係數和指數
            coef = poly1.coef * current_poly2.coef
            exp = poly1.exp + current_poly2.exp

            # 在結果多項式中尋找指數為exp的節點
            temp_result = result_head
            prev_result = None

            while temp_result is not None and temp_result.exp > exp:
                prev_result = temp_result
                temp_result = temp_result.next

            # 如果找到相同指數的節點，則將係數相加
            if temp_result is not None and temp_result.exp == exp:
                temp_result.coef += coef
            else:
                # 否則創建新的節點並插入到結果多項式中
                new_node = ListNode(coef, exp)
                new_node.next = temp_result

                if prev_result is not None:
                    prev_result.next = new_node
                else:
                    result_head = new_node

            current_poly2 = current_poly2.next

        poly1 = poly1.next

    return result_head

# 測試
# 假設多項式1: 3x^2 + 2x + 1
poly1_head = ListNode(3, 2)
poly1_head.next = ListNode(2, 1)
poly1_head.next.next = ListNode(1, 0)

# 假設多項式2: 2x + 1
poly2_head = ListNode(2, 1)
poly2_head.next = ListNode(1, 0)

result_head = polyMul(poly1_head, poly2_head)

# 列印結果多項式
while result_head is not None:
    print(f"{result_head.coef}x^{result_head.exp}", end=" ")
    if result_head.next is not None:
        print("+", end=" ")
    result_head = result_head.next