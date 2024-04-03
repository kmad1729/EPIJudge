from typing import List, Tuple
from collections.abc import Sized, Iterable, Iterator

from test_framework import generic_test

def merge_k_sorted_list_iterators(A: List[(Iterator[int])])  -> List[int]:
    import heapq
    curr_heap: List[Tuple[int, int, Iterator[int]]] = []
    result: List[int] = []
    for list_idx, curr_iter in enumerate(A):
        elem = next(curr_iter, None)
        if elem is not None:
            elemToPush = (elem, list_idx, curr_iter)
            heapq.heappush(curr_heap,  elemToPush)
    while len(curr_heap) > 0:
        elem, curr_list_idx, curr_iter = heapq.heappop(curr_heap)
        result.append(elem)
        elem = next(curr_iter, None)
        if elem is not None:
            heapq.heappush(curr_heap, (elem, curr_list_idx, curr_iter))
    return result


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_lists = []; is_increasing = True; start_idx = 0;
    for i in range(1, len(A) + 1):
        if (i == len(A) or
            (is_increasing and A[i] < A[i-1]) or
            ((not is_increasing) and A[i] > A[i-1])):
            if is_increasing:
                sorted_lists.append(iter(A[start_idx:i]))
            else:
                sorted_lists.append(reversed(A[start_idx:i]))
            is_increasing = not is_increasing
            start_idx = i
    
    return merge_k_sorted_list_iterators(sorted_lists)


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))