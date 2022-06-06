
# import sys
# import os
# sys.path.append(os.pardir)
# print(sys.path)
# # import test1 as t

import node as nd
import numpy as np
import mcts

RootState = np.array([1.,1.,1.,1.])
Root = nd.Node(RootState)

# t.prt("msg")

x = mcts.MCTS(Root)
x.Run()
