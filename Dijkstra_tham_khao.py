
#( Giải thích đoạn code: đoạn code được viết bằng ngôn ngữ python và thư viện heapq( là thư viện được dùng để xử lý 
# cấu trúc dữ liệu heap . thuật toán tìm đường đi ngắn nhất được tạo bằng cấu trúc dữ liệu heap và thư viện heapq))


# import thư viện heapq là thư viện dùng để xử lý cấu trúc dữ liệu heap(heap là cấu trúc dữ liệu gần giống với câu nhhị phân nhưng nó có đk rằng buộc nên đc chia ra làm min heap và max heap)
import heapq

# tạo hàm dijkstra là hàm để chạy thuật toán
def dijkstra(graph, start):

    # tạo ra một dictionery để chứa các khoảng cách ngắn nhất từ điểm ban đầu tơi các diểm ( ban đầu khởi tạo cho mặc định là vô cùng inf)
    distances = {node: float('inf') for node in graph}

    # khoảng cách từ điểm bắt đâu đến điểm bắt đầu luôn luôn cho mặc định là 0 ( trong trường hợp này A -> A)
    distances[start] = 0

    # tạo ra một heap là danh sách hằng đợi ưu tiên với các phần tử là tuple với cấu trúc của tuple là (khoảng cách từ diểm bắt đầu đến điểm đỉnh, tên đỉnh)
    priority_queue = [(0, start)]

    # tạo một vòng lặp while chyaj đến khi priority_queue rỗng
    while priority_queue:

        # câu lệnh lấy ra cho chúng ta đỉnh mà từ điểm bắt đầu đến đỉnh đó là ngắn nhất ( hay nói cách khác là nó lấy ra cho chúng ta đối tượng được ưu tiên nhất trong priority_queue) sau khi lấy ra thì câu lệnh sẽ xóa nó khỏi priority_queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # điều kiện để xét xem khoảng cách mới của một đỉnh có nhỏ hơn khoảng cách ban đầu của đỉnh đó không 
        if current_distance > distances[current_node]:
            continue

        # câu lệnh để tính khoảng cách ngắn nhất từ đỉnh đc lấy trong câu lệnh dòng thứ 26 đến các đỉnh của nó
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# khởi tạo một map đế di chuyển 
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {}
}

# nhập điểm bắt đầu
start_node = 'A'

# thực hiện thuạt toán Dijkstraa
shortest_distances = dijkstra(graph, start_node)

# in ra kết quả là một dictionery chưa khoảng cách ngắn nhất từ diểm bắt đầu đến các đỉnh còn lại
print(shortest_distances)
