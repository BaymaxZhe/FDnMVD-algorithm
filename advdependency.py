# advdependency.py

class FunctionalDependency:
    def __init__(self, lhs, rhs):
        self.left_hand_side = lhs
        self.right_hand_side = rhs


class MultivaluedDependency:
    def __init__(self, lhs, rhs):
        self.left_hand_side = lhs
        self.right_hand_side = rhs


def compute_fd_closure(fd_set, attributes):
    closure = set(attributes)
    while True:
        new_closure = set(closure)
        for fd in fd_set:
            if set(fd.left_hand_side).issubset(closure):
                new_closure.update(fd.right_hand_side)
        if new_closure == closure:
            break
        closure = new_closure
    return closure


def decide_fd_implication(fd_set, fd):
    closure = compute_fd_closure(fd_set, fd.left_hand_side)
    return set(fd.right_hand_side).issubset(closure)


def compute_mvd_closure(mvd_set, attributes):
    closure = set(attributes)
    while True:
        new_closure = set(closure)
        for mvd in mvd_set:
            if set(mvd.left_hand_side).issubset(closure):
                new_closure.update(mvd.right_hand_side)
        if new_closure == closure:
            break
        closure = new_closure
    return closure


def decide_mvd_implication(mvd_set, mvd):
    closure = compute_mvd_closure(mvd_set, mvd.left_hand_side)
    return set(mvd.right_hand_side).issubset(closure)


# Random data generation functions

import random
import string

def generate_random_fd(num_attributes, num_fds):
    attributes = [chr(i) for i in range(65, 65 + num_attributes)]
    fd_set = []
    for _ in range(num_fds):
        lhs = random.sample(attributes, random.randint(1, num_attributes - 1))
        rhs = random.sample(attributes, random.randint(1, num_attributes - len(lhs)))
        fd_set.append(FunctionalDependency(lhs, rhs))
    return fd_set

def generate_random_mvd(num_attributes, num_mvds):
    attributes = [chr(i) for i in range(65, 65 + num_attributes)]
    mvd_set = []
    for _ in range(num_mvds):
        lhs = random.sample(attributes, random.randint(1, num_attributes - 1))
        rhs = random.sample(attributes, random.randint(1, num_attributes - len(lhs)))
        mvd_set.append(MultivaluedDependency(lhs, rhs))
    return mvd_set
