class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        q=[]

        def addCell(i,j):
            if(i<0 or i>=rows or j<0 or j>=cols or (i,j) in visit or grid[i][j]==-1):
                return 
            visit.add((i,j))
            q.append([i,j])
        
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==0):
                    q.append([i,j])
                    visit.add((i,j))
        dist=0
        while(q):
            for _ in range(len(q)):
                r,c=q.pop(0)
                grid[r][c]=dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist+=1