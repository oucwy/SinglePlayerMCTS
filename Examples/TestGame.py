
import sys
import os
sys.path.append(os.pardir)
print(sys.path)
# import test1 as t

from mcts import node as nd
import numpy as np
from mcts import mcts

RootState = np.array([1.,1.,1.,1.])
Root = nd.Node(RootState)

t.prt("msg")

x = mcts.MCTS(Root)
x.Run()
