//============================================================================
// Name        : socket.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <socket.h>


#define port "3490"
#define backlog 10  //max number of connection
using namespace std;

int main()
{
    int fb;
    int sockfd, new_fd; //listen on sockfd, new connection on new_fd
    struct addrinfo hint, *servinfo, *p;
    struct sockaddr_storage conn_addr;   //connector's address info

    memset(&hint, 0, sizeof(hint));
    hint.ai_flags = AI_PASSIVE; //fill in current IP
    hint.family = AF_UNFSPEC;
    hint.ai_socktype = SOCK_STREAM;

    fb = getaddrinfo("127.0.0.1",port, &hint, &servinfo);


}

