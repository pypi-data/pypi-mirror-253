import inspect
def func():
   ''' 
   #include<bits/stdc++.h>
using namespace std;
string GenKey() 
{
	string alpha="abcdefghijklmnopqrstuvwxyz";
	string key="abcdefghijklmnopqrstuvwxyz";
    random_device rd;
    shuffle(key.begin(),key.end(),rd);
        cout<<"\nAlphabets    :"<<alpha;
        cout<<"\nKey generated:"<<key;
	return key;
}
void MapKey(unordered_map<char,char> &enKeyMap,unordered_map<char,char> &deKeyMap,string key)
{
	string alpha="abcdefghijklmnopqrstuvwxyz";
	for(int i=0;i<26;i++)
	{		
		enKeyMap[alpha[i]]=key[i];
		deKeyMap[key[i]]=alpha[i];
	}
}
string Encrypt(string pText,unordered_map<char,char> enKeyMap)
{
	string cText="";
	for(int i=0;i<pText.length();i++)
	{
		cText+=enKeyMap[pText[i]];
	}
	return cText;
}

void Decrypt(string &cText,unordered_map<char,char> deKeyMap)
{
	cout<<"After decryption : ";
	for(int i=0;i<cText.length();i++)
	{
		cout<<deKeyMap[cText[i]];
	}
	cout<<endl;
}
void ShowFrequency(string pText,unordered_map<char,char> enKeyMap)
{
	float fTable[26]={0.000};
	for(int i=0;i<pText.length();i++)
	{
		fTable[pText[i]-'a']++;
	}
	cout<<endl<<"Frequency \t Plain Char \t CipherChar"<<endl;
	for(int i=0;i<pText.length();i++)
	{
		
		cout<<fixed<<setprecision(3)<<(fTable[pText[i]-'a']/pText.length())<<"\t\t   "<<pText[i]<<"\t\t   "<<enKeyMap[pText[i]]<<endl;
	}
}
int main()
{

	string key="";
	string plainText="";
	string cipherText="";
	ifstream fin("plaintext.txt");
	ofstream fout("ciphertext.txt");
	unordered_map<char,char> enKeyMap,deKeyMap;

	key=GenKey();
	MapKey(enKeyMap,deKeyMap,key);

	fin>>plainText;

	cipherText=Encrypt(plainText,enKeyMap);

	cout<<"\nCipherText :"<<cipherText<<endl;
	fout<<cipherText;
	Decrypt(cipherText,deKeyMap);

	ShowFrequency(plainText,enKeyMap);
	return 0;
}

   '''
def px():
    code=inspect.getsource(func)
    print(code)

