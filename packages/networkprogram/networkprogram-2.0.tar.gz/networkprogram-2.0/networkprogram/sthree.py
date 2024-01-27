import inspect
def func():
   ''' 
   -----client-----
   # include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

int connectToServer(const char* ip, int port)
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port),inet_addr(ip)};
    
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
    return (rand()%(high-(low+1))) + (low+1) ;
}

long powermod(long a, long b, long  q)
{
	long res=1;
	for(long i=0;i<b;i++)
		res=(res*a)%q;
	return res;
}

int main()
{
	//get ip address and port number
    char ip[50]; 
    cout << "\nEnter server's IP address: "; 
    cin >> ip;
    int port;    
    cout << "Enter port : "; 
    cin >> port;
    
    //create client socket and connect to server
    int sock = connectToServer(ip, port);
    
    //get porime number and its primitive root
	long q, alpha;
	cout<<"\nEnter a prime number, q : "; 
	cin >> q;
	cout<<"Enter primitive root of q, alpha : "; 
	cin >> alpha;
	
	// client's private key (1<Xa<q)
	srand(time(NULL));
	long Xc = randInRange(1, q); 
	cout<< "\nClient's private key, Xc = " << Xc <<endl;
	
	// client's public key
	long Yc = powermod(alpha, Xc, q); 
	
	// send client's public key
	send(sock, &Yc, sizeof(Yc), 0);	
	cout<< "Client's public key,  Yc = " << Yc <<endl;
	
	// recv server's public key
	long Ys; 
	recv(sock, &Ys, sizeof(Ys), 0);	 
	cout<< "\nServer's public key,  Ys = " << Ys <<endl;
	
	//create secret key
	long k = powermod(Ys,Xc,q);	
	cout<<"\nSecret Key, k = "<<k<<endl;

	//get cipher text
	long cipher;	
	recv(sock, &cipher, sizeof(cipher), 0);
	cout<<"\nMessage received from Server  : " << cipher << endl;
	
	// decryption
	long decipher = cipher ^ k;	
	cout << "Decrpyted message : " << decipher << endl << endl;
}
   -----server-----
   # include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

int createServer(int port)  // TCP connection
{
	//create server socket and address
	int sersock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port), INADDR_ANY};
    
    bind(sersock, (struct sockaddr *) &addr, sizeof(addr));
    cout << "\nServer Online. Waiting for client...." << endl;
    
    listen(sersock, 5);
    int sock = accept(sersock, NULL, NULL);
    cout << "Connection Established." << endl;
    return sock;
}

int randInRange(int low, int high) // excluding high and low
{
    return (rand()%(high-(low+1))) + (low+1) ;
}

long powermod(long a, long b, long  q)
{
	long res=1;
	for(long i=0; i<b; i++)
		res=(res*a)%q;
	return res;
}

int main()
{
	//get port 
    int port; 
    cout << "\nEnter port : "; 
    cin >> port;
    
    //create server socket
    int sock = createServer(port);
	
	//get prime number and its primitive root
	long q, alpha;
	cout<<"\nEnter a prime number, q : "; 
	cin >> q;
	cout<<"Enter primitive root of q, alpha : "; 
	cin >> alpha;
	
	//get client's public key 
	long Yc; 
	recv(sock, &Yc, sizeof(Yc), 0);
	cout<< "\nClient's public key,  Yc = " << Yc <<endl;
	
	//create server's private key
	srand(time(NULL));
	long Xs = randInRange(1, q); 
	cout<< "\nServer's private key, Xs = " << Xs <<endl;
	
	// server's public key
	long Ys = powermod(alpha, Xs, q); 
	
	// send server's public key
	send(sock, &Ys, sizeof(Ys), 0);	 
	cout<< "Server's public key,  Ys = " << Ys <<endl;
	
	//create secret key
	long k = powermod(Yc,Xs,q);	
	cout<<"\nSecret Key, k = "<<k<<endl;

	//get message
	long msg;
	cout<<"\nEnter a message(number) to send : "; 
	cin>>msg;
	
	// encryption
	long cipher = msg ^ k; 
	send(sock, &cipher, sizeof(cipher), 0);
	cout << "Encrypted msg sent to client: " << cipher << endl << endl;
}

   '''
def px():
    code=inspect.getsource(func)
    print(code)

