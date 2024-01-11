#!/usr/bin/python3
"""
problem solving to lockboxes
"""


def canUnlockAll(boxes):
    """
    to open the locked boxes interveiw question
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for a in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = a in boxes[idx] and a != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
