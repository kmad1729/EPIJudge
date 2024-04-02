import heapq
from heapq import heappush, heappop
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    curr_heap = []
    result = []
    for (i, l) in enumerate(sorted_arrays):
        if len(l) == 0: continue
        heapq.heappush(curr_heap, (l[0], i, 0))

    while len(curr_heap) > 0:
        val, list_idx, idx_in_list = heappop(curr_heap)
        result.append(val)
        idx_in_list += 1

        if idx_in_list < len(sorted_arrays[list_idx]):
            heappush(curr_heap,
                    (sorted_arrays[list_idx][idx_in_list],
                        list_idx,
                        idx_in_list))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
