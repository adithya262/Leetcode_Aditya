class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        i,j=0,0

        UP,DOWN,LEFT,RIGHT=0,1,2,3

        Direction= RIGHT

        UP_WALL=0
        RIGHT_WALL=n
        LEFT_WALL= -1
        DOWN_WALL=m

        ans=[]

        while len(ans) != m*n:
            if Direction == RIGHT:
                while j< RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                Direction= DOWN
                RIGHT_WALL-=1
            elif Direction == DOWN:
                while i< DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                DOWN_WALL-=1
                Direction= LEFT
            elif Direction == LEFT:
                while j> LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                LEFT_WALL+=1
                Direction= UP
            else:
                while i> UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                UP_WALL+=1
                Direction= RIGHT

        return ans


        