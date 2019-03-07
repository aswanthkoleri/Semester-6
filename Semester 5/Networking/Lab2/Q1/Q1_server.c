// Server side C/C++ program to demonstrate Socket programming
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#define PORT 8080/*The port number*/
int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    char *hello = "Hello from server";
     /*Initially the socket is created.*/ 
    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    /*using setsockopt we attach the socket to the port 8080*/
    if (setsockopt(server_fd/*socket descriptor*/, SOL_SOCKET/*Level arguement */, SO_REUSEADDR | SO_REUSEPORT/*Optname helps in reuse of address and ports */,
                                                  /*Optvlaue*/&opt, /*Address len of opt*/sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );
      
    // Forcefully attaching socket to the port 8080
    /*bind will provide the socket with the address and the port number*/
    if (bind(server_fd, (struct sockaddr *)&address, 
                                 addrlen)<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    /*Will allow the socket to be in the passive mode. Will wait for the client to make the connection */
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    /*This will establish the connection from the client */
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, 
                       (socklen_t*)&addrlen))<0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }
    /*Reads the message from the client using the new_socket decriptor which we get when we accept the connection */
    valread = read( new_socket , buffer, 1024);
    printf("%s\n",buffer );
    /*This will send the message to the client*/
    send(new_socket , hello , strlen(hello) , 0 );
    printf("Hello message sent\n");
    return 0;
}