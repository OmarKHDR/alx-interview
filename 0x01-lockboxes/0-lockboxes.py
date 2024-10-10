#!/usr/bin/python3
'''A lockboxes module.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    length = len(boxes)
    unlocked = {0}
    queue = []
    for i in boxes:
        if i not in queue:
            queue.append(i)
            for j in i:
                if boxes[j] not in queue:
                    queue.append(boxes[j])
    for i in queue:
        if boxes.index(i) in unlocked:
            for j in i:
                unlocked.add(j)
    return len(unlocked) == length
