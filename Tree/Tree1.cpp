#include <stdlib.h>
#include <stdio.h>
#define queuesize 100
#define null 0
typedef char datatype;
typedef struct TreeNode
{
	datatype data;
	struct TreeNode *lc,*rc;
}TreeNode,*Tree;
createTree(TreeNode *L){
	char ch;
	if((ch=getchar())==''){
		*L=null;
	}
	else{
		*L=(TreeNode*)malloc(sizeof(TreeNode));
		(*L)->data=ch;
		createTree(&(*L)->lc);
		createTree(&(*L)->rc);
	}
}
main(){
	TreeNode L=null;
	printf("shuru\n");
	createTree(&L);
}
