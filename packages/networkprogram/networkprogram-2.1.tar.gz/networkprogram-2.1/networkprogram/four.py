import inspect
def func():
   ''' 
   #include <bits/stdc++.h>
using namespace std;
string encrypt(string pt, string key)
{
    string ct = "";
    
    int cols = key.length();
    while(pt.length()%cols!=0)
        pt+='x';
    int rows = pt.length() / cols;
    char mat[rows][cols];
    int k = 0;
    cout << "\nEncryption Matrix :" << endl;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
                cout << (mat[i][j] = pt[k++]) << " ";

        }
        cout << endl;
    }
    for (int i = 0; i < cols; i++)
    {
        for (int j = 0; j < rows; j++)
            ct += mat[j][key.find(i + '1')];
    }
    cout << "\nEncrypted text \t: " << ct << endl;
    return ct;
}
string decrypt(string ct, string key)
{
    string pt = "";
    int cols = key.length();
    int rows = ct.length() /cols;
    char mat[rows][cols];
    int k = 0;
    for (int i = 0; i < cols; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            mat[j][key.find(i + '1')] = ct[k++];
           
        }
    }
    cout << "\nDecryption Matrix :" << endl;
    for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                cout << mat[i][j] << " ";
                pt += mat[i][j];
            }
            cout << endl;
        }
    cout << "\nDecrypted text \t: " << pt << endl;
    return pt;
}
string format(string key)
{   string sortkey=key,newkey="";
    sort(sortkey.begin(),sortkey.end());
    for(int i=0;i<key.length();i++)
    {
        newkey+=to_string(sortkey.find(key[i])+1);
    }
    
    return newkey;
}int main()
{
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    string plaintext, key,k, ciphertext, decryptext;
    cout << "Enter text : ";
    cin >> plaintext;
    cout << "Enter key : ";
    cin >> k;   
    key=format(k);
    
    int i = 1;
    while (n > 0)
    {
        cout << "LEVEL " << i << endl;
        ciphertext = encrypt(plaintext, key);
        plaintext = ciphertext;
        n--;
        i++;
    }
    n = i - 1, i = 1;
    while (n > 0)
    {
        cout << "LEVEL " << i << endl;
        decryptext = decrypt(ciphertext, key);
        ciphertext = decryptext;
        n--;
        i++;
    }
    return 0;
}

   '''
def px():
    code=inspect.getsource(func)
    print(code)

