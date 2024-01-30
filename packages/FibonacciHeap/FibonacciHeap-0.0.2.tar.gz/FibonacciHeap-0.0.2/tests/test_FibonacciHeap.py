from FibonacciHeap.FibonacciHeap import FibonacciHeap, Node


def test_f_heap_basic():
    f_heap = FibonacciHeap()

    assert f_heap.get_min() is None
    assert f_heap.extract_min() is None
    assert f_heap.is_empty() is True

    f_heap.insert(Node(5))
    f_heap.insert(Node(15))
    f_heap.insert(Node(11))

    result1 = f_heap.get_min()
    result2 = f_heap.extract_min()
    result3 = f_heap.get_min()

    expected1 = Node(5)
    expected2 = Node(5)
    expected3 = Node(11)

    assert result1 == expected1
    assert result2 == expected2
    assert result3 == expected3


def test_f_heap_large():
    f_heap = FibonacciHeap()
    test_data = [13, 47, 99, 24, 63, 52, 67, 55, 43, 7, 19, 78, 35, 94, 46, 70]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    result = []
    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data_nodes)


def test_f_heap_decimals():
    f_heap = FibonacciHeap()
    test_data = [43.57, 23.73, 812.34, 42, 83, 72.01, 38.59, 50, 63, 0.45, 9.36]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    result = []
    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data_nodes)


def test_f_heap_negative():
    f_heap = FibonacciHeap()
    test_data = [65, 42, -12, 57, -6, -49, -84, 9, 14, 73, -95]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    result = []
    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data_nodes)


def test_f_heap_complex_test_data():
    f_heap = FibonacciHeap()
    test_data = [(-43.27, 'c'), (54, 97), (79.33, 'abc'), (-6.45, False), (-42.99, 'mango'), (-14.64, 'g3RtCVy5'),
                 (17.23, 'K'), (-17.23, True), (-79.33, '-79.33'), (-88, '*$@*>:'), (37, 'ApPLe'), (52.04, 'GyUFi75e')]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    result = []
    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data_nodes)


def test_union_operation():
    test_data1 = [65, 42, -12, 57, -6, -49, -84, 9, 14, 73, -95]
    test_data2 = [-43.27, 54, 79.33, -6.45, -42.99, -14.64, 17.23, -17.23, -79.33, -88, 37, 52.04]

    f_heap1 = FibonacciHeap()
    f_heap2 = FibonacciHeap()
    test_data_nodes = []
    for i in test_data1:
        node = Node(i)
        f_heap1.insert(node)
        test_data_nodes.append(node)
    for i in test_data2:
        node = Node(i)
        f_heap2.insert(node)
        test_data_nodes.append(node)

    f_heap1.union(f_heap2)

    f_heap3 = FibonacciHeap()
    f_heap3.union(f_heap1)

    # assert

    result = []
    while f_heap1.num_nodes > 0:
        result.append(f_heap1.extract_min())

    assert result == sorted(test_data_nodes)


def test_decrease_key_operation():
    f_heap = FibonacciHeap()
    test_data = [-43.27, 54, 79.33, -6.45, -42.99, -14.64, 17.23, -17.23, -79.33, -88, 37, 52.04]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    f_heap.decrease_key(test_data_nodes[4], -100)
    f_heap.decrease_key(test_data_nodes[1], 14.99)

    # test_data_nodes[4].key = -100
    # test_data_nodes[1].key = 14.99

    result = []
    for _ in range(2):
        result.append(f_heap.extract_min())

    expected = []
    for _ in range(2):
        expected.append(min(test_data_nodes))
        test_data_nodes.remove(min(test_data_nodes))

    f_heap.decrease_key(test_data_nodes[3], -16.45)
    f_heap.decrease_key(test_data_nodes[8], -143.24)
    f_heap.decrease_key(test_data_nodes[5], 5.79)

    # test_data_nodes[3].key = -16.45
    # test_data_nodes[8].key = -143.24
    # test_data_nodes[5].key = 5.79

    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    expected += sorted(test_data_nodes)

    assert result == expected


def test_delete_operation():
    f_heap = FibonacciHeap()
    test_data = [-43.27, 54, 79.33, -6.45, -42.99, -14.64, 17.23, -17.23, -79.33, -88, 37, 52.04]
    test_data_nodes = []
    for i in test_data:
        node = Node(i)
        f_heap.insert(node)
        test_data_nodes.append(node)

    f_heap.delete(test_data_nodes[1])
    f_heap.delete(test_data_nodes[7])

    test_data_nodes.pop(1)
    test_data_nodes.pop(6)

    result = []
    while f_heap.num_nodes > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data_nodes)


def test_f_heap_empty():
    f_heap = FibonacciHeap()
    assert f_heap.is_empty() is True

    f_heap.insert(Node(5))
    assert f_heap.is_empty() is False

    f_heap.extract_min()
    assert f_heap.is_empty() is True


def test_f_heap_comprehensive():
    f_heap1 = FibonacciHeap()
    f_heap2 = FibonacciHeap()

    assert f_heap1.get_min() is None
    assert f_heap1.extract_min() is None
    assert f_heap1.is_empty() is True

    test_data1 = [-100.19, 9.64, -6.12, 83.24, 72.19, -53.96, 84.69, 70.51, 30.55, 59.17, -78.04, 50.78, 31.27, 85.21,
                  44.07, -19.39, 40.26, 90.93, -85.88, 72.32, 45.76, -27.17, 82.35, 8.55, -58.27]
    test_data2 = [44.35, 17.37, 2.32, -95.28, -100.68, 80.79, -38.27, -41.05, 72.52, -31.91, -65.81, -42.03, 80.32,
                  28.87, -61.68, -43.62, 64.71, 40.97, 60.98, 6.46, 52.98, -37.22, 5.13, 17.49, 6.78]
    test_data_nodes1 = []
    test_data_nodes2 = []
    for i in test_data1:
        node = Node(i)
        f_heap1.insert(node)
        test_data_nodes1.append(node)
    for i in test_data2:
        node = Node(i)
        f_heap2.insert(node)
        test_data_nodes2.append(node)

    assert f_heap1.get_min() == min(test_data_nodes1)
    assert f_heap2.get_min() == min(test_data_nodes2)

    f_heap1_extracted = []
    f_heap2_extracted = []

    for _ in range(5):
        f_heap1_extracted.append(f_heap1.extract_min())
        f_heap2_extracted.append(f_heap2.extract_min())

    extract_min_expected1 = []
    extract_min_expected2 = []
    for _ in range(5):
        extract_min_expected1.append(min(test_data_nodes1))
        test_data_nodes1.remove(min(test_data_nodes1))

        extract_min_expected2.append(min(test_data_nodes2))
        test_data_nodes2.remove(min(test_data_nodes2))

    assert f_heap1_extracted == extract_min_expected1
    assert f_heap2_extracted == extract_min_expected2

    assert f_heap1.get_min() == min(test_data_nodes1)
    assert f_heap2.get_min() == min(test_data_nodes2)

    # with pytest.raises(ValueError):
    #     f_heap1.decrease_key(test_data_nodes1[0], -99)

    f_heap1.decrease_key(test_data_nodes1[1], -40.73)
    f_heap1.decrease_key(test_data_nodes1[12], -27.64)
    f_heap1.decrease_key(test_data_nodes1[7], -133.97)

    f_heap2.decrease_key(test_data_nodes2[0], -6.28)
    f_heap2.decrease_key(test_data_nodes2[19], -0.93)
    f_heap2.decrease_key(test_data_nodes2[14], -140.48)

    # test_data_nodes1[1].key = -40.73
    # test_data_nodes1[12].key = -27.64
    # test_data_nodes1[7].key = -133.97
    #
    # test_data_nodes2[0].key = -6.28
    # test_data_nodes2[19].key = -0.93
    # test_data_nodes2[14].key = -140.48

    f_heap1.union(f_heap2)

    assert f_heap1.get_potential() == 15

    for i in range(15, 20):
        f_heap1.delete(test_data_nodes1[i])
        f_heap1.delete(test_data_nodes2[i])

    assert f_heap1.get_potential() == 10

    test_data_nodes = test_data_nodes1[:15] + test_data_nodes2[:15]

    result = []
    while f_heap1.num_nodes > 0:
        result.append(f_heap1.extract_min())

    assert result == sorted(test_data_nodes)

    assert f_heap1.get_min() is None
    assert f_heap1.extract_min() is None
