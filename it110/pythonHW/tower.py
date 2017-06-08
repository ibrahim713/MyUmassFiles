# demo for hanoi tower

def hanoi(n):
    hanoiHelper(n, 'towerA','towerB','towerC')

def hanoiHelper(n, source,helper,target):
    if n ==1:
        print 'Move Disk', n, 'from',source,'to', target
    else:
        hanoiHelper(n-1, source, target, helper)
        print 'Move Disk', n, 'from', source,'to', target
        hanoiHelper(n-1, helper, source, target)
n =64
hanoi(n)
