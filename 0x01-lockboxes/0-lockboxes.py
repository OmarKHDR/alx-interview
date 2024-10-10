#!/usr/bin/python3
'''A lockboxes module.
'''


def recurse(queue, boxes, curkeys):
    '''a function to recursively try to add
    the boxes in the open order in queue
    '''
    for i in curkeys:
        if i >= len(boxes):
            continue
        if boxes[i] not in queue:
            queue.append(boxes[i])
            recurse(queue, boxes, boxes[i])


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    length = len(boxes)
    unlocked = {0}
    queue = [boxes[0]]
    recurse(queue, boxes, boxes[0])
    for i in queue:
        if boxes.index(i) in unlocked:
            for j in i:
                if j >= len(boxes):
                    continue
                unlocked.add(j)
    return len(unlocked) == length
