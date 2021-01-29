public class control {
    public static void main(String[] args) {
        // System.out.println("Hello World!");
        int[][] myGrid = {{5,3,0,0,7,0,0,0,0},
                          {6,0,0,1,9,5,0,0,0},
                          {0,9,8,0,0,0,0,6,0},
                          {8,0,0,0,6,0,0,0,3},
                          {4,0,0,8,0,3,0,0,1},
                          {7,0,0,0,2,0,0,0,6},
                          {0,6,0,0,0,0,2,8,0},
                          {0,0,0,4,1,9,0,0,5},
                          {0,0,0,0,8,0,0,7,9}};
                          
        Solver mySudoku = new Solver(myGrid);
        mySudoku.viewMatrix();
        System.out.println("");
        mySudoku.solve();
    }
}
