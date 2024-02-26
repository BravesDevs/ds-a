class Solution(object):
    def spiralOrder(self, matrix):

        direction=1
        row,col=0,0
        traversedNodes = []
        traversal = []
        nColumns = len(matrix[0])
        nRows = len(matrix)

        while len(traversedNodes)<(nRows*nColumns):
            if direction==1:
                if (row,col) not in traversedNodes and col<nColumns:
                    traversal.append(matrix[row][col])
                    traversedNodes.append((row,col))
                    col+=1
                else:
                    col-=1
                    row+=1
                    direction=2
            elif direction==2:
                if (row,col) not in traversedNodes and row<nRows:
                    traversal.append(matrix[row][col])
                    traversedNodes.append((row,col))
                    row+=1
                else:
                    row-=1
                    col-=1
                    direction=3
            elif direction==3:
                if (row,col) not in traversedNodes and col>=0:
                    traversal.append(matrix[row][col])
                    traversedNodes.append((row,col))
                    col-=1
                else:
                    direction=4
                    col+=1
                    row-=1
            elif direction==4:
                if (row,col) not in traversedNodes and row>=0:
                    traversal.append(matrix[row][col])
                    traversedNodes.append((row,col))
                    row-=1
                else:
                    direction=1
                    col+=1
                    row+=1
        return traversal    
       
            


sln = Solution()
result = sln.spiralOrder([[1]])

print("Result: ",result)