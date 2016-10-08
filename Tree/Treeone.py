class TreeNode(object):
	"""docstring for Tree"""
	def __init__(self, data=-1,lchild=None,rchild=None):
		self.data=data
		self.lc=lchild
		self.rc=rchild
	
class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root=TreeNode()

	def CreateTree(self,data):
		node=TreeNode(data)
		if self.root.data==-1:
			self.root=node;
		else:
			myQ=[]
			treeNode=self.root
			myQ.append(treeNode)
			while myQ:
				treeNode=myQ.pop(0)
				if treeNode.lc==None:
					treeNode.lc=node
					return
				elif treeNode.rc==None:
					treeNode.rc=node
					return
				else:
					myQ.append(treeNode.lc)
					myQ.append(treeNode.rc)

	def font_Travers(self,root):

		if root!=None:
			print(root.data)
		else:
			return
		self.font_Travers(root.lc)
		self.font_Travers(root.rc)
	def add(self,data):
		
		if self.root.data==-1:
			self.root=TreeNode(data)
		else:
			self.add(self.root.lc)
			self.add(self.root.rc)

def AddT(Tree,data):
	if Tree==None:
		Tree=TreeNode()
	if Tree.lc==None:
		Tree.lc=TreeNode(data)
		return
	elif Tree.rc==None:
		Tree.rc=TreeNode(data)
		return
	else:
		AddT(Tree.lc,data)
		AddT(Tree.rc,data)
		return Tree
def f_T(Tree):
		if Tree!=None:
			print(Tree.data)
		else:
			return
		f_T(Tree.lc)
		f_T(Tree.rc)

if __name__=='__main__':
	data=range(10)
	Tree=TreeNode()
	L=TreeNode()
	for d in data:
		L=AddT(Tree,d)
		print(L.data)

	f_T(Tree)
