import hou


nodes=[]
for node in hou.selectedNodes():
    nodes.append(node)
    
for i in range(len(nodes)):
    if i != 0: 
        # print(nodes[i])
        nodes[i].setNextInput(nodes[0])
    else:
        pass
        
