public class Solver {
    public final static int ROW_COL = 9;
    public final static int S_ROW_COL = 3;

    public int[][] grid;
    
    public Solver(int[][] grid){
        this.grid = grid;
    }
    
    public void viewMatrix(){
        int i, j;

        for(i = 0; i < ROW_COL; i++){
            for(j = 0; j < ROW_COL; j++){
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }

    public boolean possible(int row, int col, int actualNum){
        int i, j;
        int smallR, smallC;

        //Check row
        for(i = 0; i < ROW_COL; i++){
            if(grid[row][i] == actualNum){
                return false; 
            }
        }

        //Check col
        for(i = 0; i < ROW_COL; i++){
            if(grid[i][col] == actualNum){
                return false;
            }
        }
        smallC = (col / 3) * 3;
        smallR = (row / 3) * 3;
        
        //Cehck small grid
        for(i = 0; i < S_ROW_COL; i++){
            for(j = 0; j < S_ROW_COL; j++){
                if(grid[smallR + i][smallC + j] == actualNum){
                    return false;
                }
            }
        }
        return true;
    }

    public void solve(){
        int i, j, n;
    
        for(i = 0; i < ROW_COL; i++){
            for(j = 0; j < ROW_COL; j++){
                if(grid[i][j] == 0){
                    for(n = 1; n <= ROW_COL; n++){
                        if(possible(i, j, n)){
                            grid[i][j] = n;
                            solve();
                            grid[i][j] = 0;
                        }
                    }
                    return;
                }
            }
        } 
        viewMatrix();
    }
}       
