import inspect
def func():
   ''' 
   #include<bits/stdc++.h>
using namespace std;
int sBoxes[8][4][16] = {
   {14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
    0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
    4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
    15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13},

    {15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
    3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
    0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
    13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9},

    {10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
    13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
    13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
    1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12},

    {7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
    13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
    10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
    3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14},

    {2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
    14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
    4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
    11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3},

    {12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
    10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
    9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
    4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13,},

    {4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
    13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
    1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
    6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12},

    {13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
    1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
    7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
    2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11}
};

int permTable[] = {
    16, 7 , 20, 21, 29, 12, 28, 17,
    1 , 15, 23, 26, 5 , 18, 31, 10,
    2 , 8 , 24, 14, 32, 27, 3 , 9 ,
    19, 13, 30, 6 , 22, 11, 4 , 25 };

int ETable[]={32,1,2,3,4,5,
   4,5,6,7,8,9,
   8,9,10,11,12,13,
   12,13,14,15,16,17,
   17,17,18,19,20,21,
   20,21,22,23,24,25,
   24,25,26,27,28,29,
   28,29,30,31,32,1};

string expansion(string ip,int *Etable)
{
 string res="";
 for(int i=0;i<48;i++)
    res+=ip[Etable[i]-1];
 return res;
}
string substitution(string ipt)
{
    string res = "";
    for(int i=0; i<8; i++)
    {
        string sipt = ipt.substr(6*i, 6) ;
        int row = bitset<2>( sipt.substr(0,1) + sipt.substr(5,1) ).to_ulong() ;
        int col = bitset<4>( sipt.substr(1,4) ).to_ulong() ;
        res += bitset<4>(sBoxes[i][row][col]).to_string() ;

    }
    return res;
}/*
string substitution(string ipt)
{
    string res = "";
    for(int i=0; i<48; i+=6)
    {
        string temp = ipt.substr(i, 6) ;
        int row = bitset<2>( temp.substr(0,1) + temp.substr(5,1) ).to_ulong() ;
        int col = bitset<4>( temp.substr(1,4) ).to_ulong() ;
        res += bitset<4>(sBoxes[i][row][col]).to_string() ;

    }
    return res;
}*/

string permute(string ipt)
{
    string res = "";
    for(int i=0; i<32; i++)
    {
        res += ipt[permTable[i]-1];
    }
    return res;
}

string xor_operation(string x, string y){
    string res = "";
    for(int i=0; i<x.length(); i++)
    {
        res += (x[i] == y[i]) ? "0" : "1";
    }
    return res;
}


string bin_to_hex(string binary)
{
    string res="";
    unordered_map<string,char>m;
        m["0000"]='0';
        m["0001"]='1';
        m["0010"]='2';
        m["0011"]='3';
        m["0100"]='4';
        m["0101"]='5';
        m["0110"]='6';
        m["0111"]='7';
        m["1000"]='8';
        m["1001"]='9';
        m["1010"]='A';
        m["1011"]='B';
        m["1100"]='C';
        m["1101"]='D';
        m["1110"]='E';
        m["1111"]='F';
    for(int i=0;i<binary.length();i+=4)
    {
        res+=m[binary.substr(i,4)];
    }
    return res;

    
}
int main()
{
unsigned long long hexa,key_hex;
string binary;
cout<<"Enter the 16 bit hexadecimal input:"<<endl;
cin>>hex>>hexa;
binary=bitset<64>(hexa).to_string();
string key;
cout<<"Enter the 12 bit hexadecimal key:"<<endl;
cin>>hex>>key_hex;
key=bitset<48>(key_hex).to_string();

cout<<"*************\nRound Function\n*****************"<<endl;
string left=binary.substr(0,32);
string right=binary.substr(32,32);
cout<<"Binary form of 64 bit input:"<<binary<<endl;
cout<<"Left half:"<<left<<"\t\t"<<bin_to_hex(left)<<endl;
cout<<"Right half:"<<right<<"\t\t"<<bin_to_hex(right)<<endl;
string expRight=expansion(right,ETable);
cout<<"After expansion ,right half will be:"<<expRight<<"\t\t"<<bin_to_hex(expRight)<<endl;
cout<<"Key is:"<<key<<"\t\t"<<bin_to_hex(key)<<endl;
string sb_ip=xor_operation(expRight,key);


cout<<"*******S-box operation**************\n";
cout<<"The 48 bit input for S-box will be:"<<sb_ip<<"\t\t"<<bin_to_hex(sb_ip)<<endl;
string sBoxOutput = substitution(sb_ip);
cout << "\nS-Box output    = " << sBoxOutput <<"\t\t"<<bin_to_hex(sBoxOutput)<< endl;
string P = permute(sBoxOutput);
cout << "Permuted output = " << P <<"\t\t"<<bin_to_hex(P)<< endl;
string Ri = xor_operation(P,left);
cout << "\nOutput of ith round (Ri) = " << Ri <<"\t\t"<<bin_to_hex(Ri)<< endl << endl;
return 0;
}
   '''
def px():
    code=inspect.getsource(func)
    print(code)

