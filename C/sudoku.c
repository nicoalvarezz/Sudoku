/*SUDOKU*/

#include <stdio.h>
#include <stdbool.h>

#define ROW_COL 9
#define S_ROW_COL 3

//GLOBAL VARIABLES
int grid[ROW_COL][ROW_COL]={{5,3,0,0,7,0,0,0,0},
							{6,0,0,1,9,5,0,0,0},
							{0,9,8,0,0,0,0,6,0},
							{8,0,0,0,6,0,0,0,3},
							{4,0,0,8,0,3,0,0,1},
							{7,0,0,0,2,0,0,0,6},
							{0,6,0,0,0,0,2,8,0},
							{0,0,0,4,1,9,0,0,5},
							{0,0,0,0,8,0,0,7,9}}; //Sudoku Grid
int counter; 

//FUNCTION SIGNATURE
void viewMatrix(); //Print sudoku grid
bool possible(int, int, int); //Check if anumber corresponds to a certain position
void solve(); //Solve sudoku

int main(){
	counter = 0;
	viewMatrix();
	printf("\n");
	solve();
	printf("\n");
	return 0;
}

void viewMatrix(){
	int i, j; //Loop variables

	//Basic nested loop to print a bidimensional array
	for(i = 0; i < ROW_COL; i++){
		for(j = 0; j < ROW_COL; j++){
			printf(" %d ", grid[i][j]);	
		}
		printf("\n");	
	}	
}

bool possible(int r, int c, int actualNum){
	int i, j; //Loop variables
	int smallR, smallC;

	//Check Row
	for(i = 0; i < ROW_COL; i++){
		if(grid[r][i] == actualNum){
			return false;
		}
	}

	//Check Column
	for(i = 0; i < ROW_COL; i++){
		if(grid[i][c] == actualNum){			
			return false;
		}
	}

	smallR = (r/3)*3; //Find Smaller row
	smallC = (c/3)*3; //Find the smaller column

	//Check small grid
	for(i = 0; i < S_ROW_COL; i++){
		for(j = 0; j < S_ROW_COL; j++){
			if(grid[smallR + i][smallC + j] == actualNum){
				return false;
			}			
		}
	}

	return true;
}

void solve(){
	int i, j, n;
	int aux;

	//Loop through grid untill a 0 is found
	for(i = 0; i < ROW_COL; i++){
		for(j = 0; j < ROW_COL; j++){
			if(grid[i][j] == 0){
				//Find number that must replace 0
				for(n = 1; n <= ROW_COL; n++){
					if(possible(i, j, n)){
						grid[i][j] = n;
						solve(); //Recursively call solve
						// Backtrackking Recusion
						counter++;
						grid[i][j] = 0;
					}
				}
				return;
			}
		}
	}
	viewMatrix(); //Print Result
}