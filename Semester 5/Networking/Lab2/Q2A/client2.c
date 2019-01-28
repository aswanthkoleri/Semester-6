#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#pragma pack(1)
#pragma pack(0)

int main(int argc, char const *argv[])
{
    int socket_fd;
    char temp='a';
    struct sockaddr_in server;/*Declare the server address structure*/
    socket_fd = socket(AF_INET,SOCK_DGRAM,0);/*Create the socket */
    if(socket_fd < 0){
        perror("socket creation failed");
        return 0;
    }
    /*Declare the variale to recieve data */
    char info;
    /*Clear the server address*/
    memset(&server,'0',sizeof(server));
    /*Set the server a port no */
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(4040);
    /*Declare the length of the server address*/
    int server_len_of_addr;
    /*Send to the server for server to identify the client */
    sendto(socket_fd,&temp,sizeof(temp),MSG_CONFIRM,(const struct sockaddr *)&server,sizeof(server));
     /*Recieve from server*/
    int rec = recvfrom(socket_fd,&info,sizeof(info),MSG_WAITALL,(struct sockaddr *)&server,&server_len_of_addr);
    /*Print the recieved data*/
    printf("Client received : \n");
    printf("%c  ",info);
    /*Close the socket */
    close(socket_fd);
    return 0;
}
