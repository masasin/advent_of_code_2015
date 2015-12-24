#cython: boundscheck=False, wraparound=False, nonecheck=False
cimport cython
import numpy as np
cimport numpy as np


def get_house_n_gifts(unsigned int target, unsigned int gifts_per_house=10,
                      max_visits=None):
    cdef np.uint_t i, j, limit
    cdef np.uint_t max_number = target // gifts_per_house
    cdef np.ndarray[np.uint_t, ndim=1] houses = np.zeros(max_number + 1,
                                                         dtype=np.uint)
    limit = (max_number + 1) if max_visits is None else max_visits

    for i in range(1, max_number + 1):
        houses[j:i*limit:i] += gifts_per_house * i

    return np.where(houses >= target)[0][0]


def part_one():
    cdef np.uint_t i, j
    cdef np.uint_t puzzle_input = 29000000
    cdef np.uint_t max_number = puzzle_input // 10
    cdef np.ndarray[np.uint_t, ndim=1] houses = np.zeros(max_number + 1,
                                                         dtype=np.uint)
    for i in range(1, max_number + 1):
        j = i
        while j < max_number + 1:
            houses[j] += 10 * i
            j += i
    print(np.where(houses >= puzzle_input)[0][0])


def part_two():
    cdef np.uint_t i, j
    cdef np.uint_t puzzle_input = 29000000
    cdef np.uint_t max_number = puzzle_input // 11
    cdef np.ndarray[np.uint_t, ndim=1] houses = np.zeros(max_number + 1,
                                                         dtype=np.uint)
    for i in range(1, max_number + 1):
        j = i
        while j < i * 50 and j <= max_number:
            houses[j] += 11 * i
            j += i
    print(np.where(houses >= puzzle_input)[0][0])
