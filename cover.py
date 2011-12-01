#!/usr/bin/env python2.7
#coding=utf-8
def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)
    # Side length of subboardi:
    s = side / 2
    #offset for outer / inner squares of subboards:
    offset = (0,-1), (side-1, 0)
    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # if the outer corner is not set ...
            if not board[top+dy_outer][left+dx_outer]:
                # ... label the inner corner:
                board[top+s+dy_inner][left+s+dx_inner] = lab
