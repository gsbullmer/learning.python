"""namedtuple.py"""


# the problem
vision = (9.5, 8.8)
print(vision)   # (9.5, 8.8)
print(vision[0])    # 9.5   # left eye (implicit positional reference)
print(vision[1])    # 8.8   # right eye (implicit positional reference)


# the solution
from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0])    # 9.5
print(vision.left)  # 9.5   # same as vision[0], but explicit
print(vision.right)     # 8.8   # same as vision[1], but explicit


# the change
Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
print(vision.left)  # 9.5   # still perfect
print(vision.right)     # 8.8   # still perfect (though now is vision[2])
print(vision.combined)  # 9.2   # the new vision[1]
