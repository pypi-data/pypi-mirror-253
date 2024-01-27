import inspect
def func():
   ''' 
   -----cleint-------
   # include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

int connectToServer(const char* ip, int port)
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port), inet_addr(ip)};

    if(connect(sock, (struct sockaddr *) &addr, sizeof(addr)) < 0 )
    {
        cout << "\nRun server program first." << endl; 
        exit(0);
    }
    else
        cout << "\nClient is connected to Server." << endl; 
    return sock;
}

int randInRange(int low, int high) // excluding high and low
{
    return rand()%(high-(low+1)) + (low+1) ;
}

int gcd(int a, int b)
{
    return b==0 ? a : gcd(b, a%b);
}

int powermod(int a, int b, int n)
{
    int res = 1;
    for(int i=0; i<b; i++)
        res = (res*a) % n;
    return res;
}

// M = C^d mod n
int decrypt(int C, int PR[2])
{
    return powermod(C, PR[0], PR[1]);
}

// a=00, b=01, ... A=26, B=27...
char toChar(int n)
{
    return (n >= 26) ? (n+'A'-26) : (n+'a');
}

int main()
{
	//get ip address and port
    char ip[50];
    int port;
    cout << "Enter Server's IP address: "; 
    cin >> ip;
    cout << "Enter port : "; 
    cin >> port;
    
    //connect to server socket
    int sock = connectToServer(ip, port);

	//get two prime numbers
    int p,q; 
    cout << "\nEnter two large prime numbers(>100) : "; 
    cin >> p >> q;
    
    //compute n and phi
    int n = p * q ; // should be greater than 5151 (since ZZ=5151)
    int phi = (p-1) * (q-1);

	//choose e and d
    srand(time(NULL));
    int e, d;
    do{ 
    	e = randInRange(1, phi); 
    }while(gcd(e,phi) != 1);
    
    for(d=1; d<phi; d++)
        if((d*e)%phi == 1) 
        	break;
    
    int PU[2] = {e, n}; // public key
    int PR[2] = {d, n}; // private key
    cout << "\nPublic key , PU = {" << e << ", " << n << "}" << endl;
    cout << "Private key, PR = {" << d << ", " << n << "}" << endl;

    send(sock, &PU, sizeof(PU), 0); // send public key to server
    cout << "\nSent Public key to server." << endl;

    string msg = "";
    while (true)
    {
        int C; // ciphertext
        recv(sock, &C, sizeof(C), 0); 
        
        if(C == -1)   
        	break; // at the end -1 will be received 
        cout << "\nCiphertext received from server : " << C << endl;

        int M = decrypt(C,PR);
        cout << "Decrypted Text : " << M << endl;
        msg += toChar(M/100); // first char in block
        msg += toChar(M%100); // second char in block
    }
    cout << "\nDecrypted message : " << msg << endl << endl; 
}

-----server-------
# include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

int createServer(int port)  // TCP connection
{
    int sersock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port), INADDR_ANY};

    bind(sersock, (struct sockaddr *) &addr, sizeof(addr));
    cout << "\nServer Online. Waiting for client...." << endl;

    listen(sersock, 5);
    int sock = accept(sersock, NULL, NULL);
    cout << "Connection Established." << endl;

    return sock;
}

int powermod(int a, int b, int n)
{
    int res = 1;
    for(int i=0; i<b; i++)
        res = (res*a) % n;
    return res;
}

// C = M^e mod n
int encrypt(int M, int PU[2]) // PU = {e, n}
{
    return powermod(M, PU[0], PU[1]);
}

// a=00, b=01, ... A=26, B=27...
int toInt(char c)
{
    return (c < 'a') ? (c-'A'+26) : (c-'a');
}

int main()
{
	//get port number
    int port;
    cout << "Enter port : "; cin >> port;
    
    //create server socket
    int sock = createServer(port);

    int PU[2];
    recv(sock, &PU, sizeof(PU), 0); // receive public key from client
    cout << "\nPublic key received from client : {" << PU[0] << ", " << PU[1] << "}" << endl;

    string msg; // plaintext message
    cout << "\nEnter message to encrypt : "; 
    cin >> msg;
    
    //padding
    if(msg.length()% 2 != 0) 
    	msg+="x";

	//encryption blockwise
    for(int i=0; i<msg.length(); i+=2) // increment by 2 for block
    { 
        int M = toInt(msg[i])*100 + toInt(msg[i+1]); // block consist of two msg character 
        cout << "\nPlaintext block : " << M << endl;

        int C = encrypt(M, PU);
        cout << "Encrypted text  : " << C << endl;
        send(sock, &C, sizeof(C), 0); // send ciphertext to client
    }
    
    int stop = -1; // at end send -1 to tell client to stop
    send(sock, &stop, sizeof(stop), 0); //at end send stop to client
    cout << "\nSent ciphertext to client." << endl << endl;
}

   '''
def px():
    code=inspect.getsource(func)
    print(code)

