# 이진 트리 구현

# 초기화
memory = []
root = None
nameAry = ['블랭핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# TreeNode 클래스 선언
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

# 메인 모듈
if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name

        current = root
        while True:
            if name < current.data: # 현재 name이 노드의 데이터보다 작으면
                if current.left == None:
                    current.left = node
                    break # 연결했으니 반복문 탈출
                else:
                    current = current.left # 왼쪽으로 더 내려감
            else: # 오른쪽으로 보냄
                if current.right == None:
                    current.right = node
                    break
                else:
                    current = current.right

        memory.append(node)

    print('이진탐색 트리 구성 완료!')

    findName = input('찾을 이름 입력 > ')
    
    current = root
    while True:
        if findName == current.data:
            print(f'{findName} 찾음')
            break
        elif findName < current.data:
            if current.left == None:
                print(f'{findName} 트리에 없음')
                break
            else:
                current = current.left
        else:
            if current.right == None:
                print(f'{findName} 트리에 없음')
                break
            else:
                current = current.right
                
    print('검색 종료')

## 트리노드 삭제
delName = input('삭제할 이름 입력 > ')
current = root
parent = None
while True:
    if delName == current.data: # 삭제할 때
        if current.left == None and current.right == None: # 리프노드
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)

        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)
        
        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del(current)

        print(f'{delName} 이(가) 삭제됨')
        break

    elif delName < current.data:
        if current.left == None:
            print(f'{delName} 이(가) 트리에 없음')
            break
        parent = current
        current = current.left
    
    else:
        if current.right == None:
            print(f'{delName} 이(가) 트리에 없음')
            break
        parent = current
        current = current.right

    