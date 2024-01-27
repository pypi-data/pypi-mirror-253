import inspect
def func():
   ''' 
   #include<bits/stdc++.h>
using namespace std;
int key[3][3];

int mod26(int x)
{
	return x>=0?(x%26):26-(abs(x)%26);
}
void display(int m[1000][3],int row,int col)
{
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<col;j++)
			cout<<m[i][j]<<"\t";
		cout<<endl;
	}
}

int findDet(int m[3][3],int n)
{
	int det;
	if(n==2)
		det=m[0][0]*m[1][1]-m[0][1]*m[1][0];
	else if(n==3)
		det=m[0][0]*(m[1][1]*m[2][2]-m[2][1]*m[1][2])-m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])+m[0][2]*(m[1][0]*m[2][1]-m[2][0]*m[1][1]);
	else 
	det=0;    
	return mod26(det);
			    
}

int findDetInverse(int r2,int r1=26)
{
	int t1=0,t2=1;
	while(r2!=0)
	{
		int q=r1/r2;
		int r=r1-(q*r2);
		int t=t1-(q*t2);
		r1=r2;
		r2=r;
		t1=t2;
		t2=t;
	}
	return mod26(t1);
}

void multiplyMatrices(int a[1000][3],int a_rows,int a_cols,int b[1000][3],int b_rows,int b_cols,int res[1000][3])
{
	for(int i=0;i<a_rows;i++)
	{
		for(int j=0;j<b_cols;j++)
		{
			for(int k=0;k<b_rows;k++)
				res[i][j]+=a[i][k]*b[k][j];
			res[i][j]=mod26(res[i][j]);
		}
	}
}


void findInverse(int m[3][3],int n,int m_inverse[3][3])
{
	int adj[3][3]={0};
	int det=findDet(m,n);
     cout<<"Determinant: "<<det<<endl;
	int detInverse=findDetInverse(det);
    cout<<"Multiplicative Inverse: "<<detInverse<<endl;
	if(n==2)
	{
		adj[0][0]=m[1][1];
		adj[1][1]=m[0][0];
		adj[0][1]=-m[0][1];
		adj[1][0]=-m[1][0];
	}
	
	else if(n==3)
	{
		int temp[5][5]={0};
		for(int i=0;i<5;i++)
		{
			for(int j=0;j<5;j++)
				temp[i][j]=m[i%3][j%3];
		}
		for(int i=1;i<=3;i++)
		{
			for(int j=1;j<=3;j++)
			{
				adj[j-1][i-1]=temp[i][j]*temp[i+1][j+1]-temp[i][j+1]*temp[i+1][j];
			}
		}
	}
	cout<<"\nADJOINT MATRIX"<<endl;
	display(adj,n,n);
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			m_inverse[i][j]=mod26(adj[i][j]*detInverse);
	}
	cout<<"INVERSE MATRIX"<<endl;
	display(m_inverse,n,n);

}

string encrypt(string pt,int n)
{
	int p[1000][3]={0};
	int c[1000][3]={0};
	int ptIter=0;
	while(pt.length()%n!=0)
		pt+='x';
	int row=(pt.length())/n;
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<n;j++)
		{
			p[i][j]=pt[ptIter++]-'a';
		}
	}
	cout<<"Plain Text Matrix:\n";
	display(p,row,n);
	cout<<"\nKey Matrix:\n";
	display(key,n,n);
	cout<<"\nEncryption Process\n";
	
	multiplyMatrices(p,row,n,key,n,n,c);
	cout<<"\nEncrypted Matrix\n";
	display(c,row,n);
		string ct="\0";
		for(int i=0;i<row;i++)
		{
			for(int j=0;j<n;j++)
			{
				ct+=(c[i][j]+'a');
			}
		}
		
	return ct;
	
}


string decrypt(string ct,int n)
{
	int p[1000][3]={0};
	int c[1000][3]={0};
	int ctIter=0;
	int row=ct.length()/n;
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<n;j++)
			c[i][j]=ct[ctIter++]-'a';
	}
	int k_inverse[3][3]={0};
	cout<<"\nDecryption Process\n";
	findInverse(key,n,k_inverse);
   
	multiplyMatrices(c,row,n,k_inverse,n,n,p);
	string pt="\0";
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<n;j++)
			pt+=(p[i][j]+'a');
	}
	return pt;
}
int main()
{
	string pt;
	int n;
	cout<<"Enter the text to be encrypted: ";
	cin>>pt;
	cout<<"Enter the order of key matrix: ";
	cin>>n;	
	cout<<"Enter the key matrix:";
	cout<<endl;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			cin>>key[i][j];
			
	}
	cout<<"\nOriginal text: "<<pt<<endl;
	string ct=encrypt(pt,n);
	cout<<"\nEncrypted text: "<<ct<<endl;
	string dt=decrypt(ct,n);
	cout<<"Decrypted text: "<<dt<<endl;
}

   '''
def px():
    code=inspect.getsource(func)
    print(code)

