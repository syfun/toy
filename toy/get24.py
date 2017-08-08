from copy import copy

import click


add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y


def div(x, y):
    if y == 0:
        return 0
    else:
        return x * 1.0 / y


ops = {'+': add, '-': sub, '*': mul, '/': div}
op_order = ['+', '-', '*', '/']


class Get24(object):
    def __init__(self, nums):
        self.nums = nums
        self.num_scenes = []
        self.op_scenes = []

    def arrange(self, prefix, nums):
        length = len(nums)
        for n in nums:
            if n in prefix:
                continue
            prefix.append(n)
            if len(prefix) == length:
                self.num_scenes.append(copy(prefix))
            else:
                self.arrange(prefix, nums)
            prefix.pop()

    def combine(self, prefix, nums, length):
        op_scenes = []
        for n in nums:
            prefix.append(n)
            if len(prefix) == length:
                self.op_scenes.append(copy(prefix))
            else:
                self.combine(prefix, nums, length)
            prefix.pop()

    def count(self, nums, num_scene, op_scene):
        opstr0 = op_order[op_scene[0]]
        opstr1 = op_order[op_scene[1]]
        opstr2 = op_order[op_scene[2]]
        op0 = ops[opstr0]
        op1 = ops[opstr1]
        op2 = ops[opstr2]
        a = nums[num_scene[0]]
        b = nums[num_scene[1]]
        c = nums[num_scene[2]]
        d = nums[num_scene[3]]
        t = op0(a, b)
        s = '({a} {opstr0} {b})'.format(a=a, b=b, opstr0=opstr0)

        def format(fmt):
            return fmt.format(s=s, opstr1=opstr1, opstr2=opstr2, c=c, d=d)

        if op2(op1(t, c), d) == 24:
            print(format('({s} {opstr1} {c}) {opstr2} {d} = 24'))
        if op2(d, op1(t, c)) == 24:
            print(format('{d} {opstr2} ({s} {opstr1} {c}) = 24'))
        if op2(op1(c, t), d) == 24:
            print(format('({c} {opstr1} {s}) {opstr2} {d} = 24'))
        if op2(d, op1(c, t)) == 24:
            print(format('{d} {opstr2} ({c} {opstr1} {s}) = 24'))

    def run(self):
        self.arrange([], [0, 1, 2, 3])
        self.combine([], [0, 1, 2, 3], 3)
        for num_scene in self.num_scenes:
            for op_scene in self.op_scenes:
                self.count(self.nums, num_scene, op_scene)


@click.command()
@click.argument('numbers')
def get24(numbers):
    """Get 24, for numbers like 1,2,3,4"""
    numbers = [int(n) for n in numbers.split(',')]
    ob = Get24(numbers)
    ob.run()
