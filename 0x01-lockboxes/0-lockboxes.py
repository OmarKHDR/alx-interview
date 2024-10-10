#!/usr/bin/python3

def canUnlockAll(boxes):
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
