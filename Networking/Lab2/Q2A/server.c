#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>



int main(int argc, char const *argv[])
{
    int socket_fd = 0;
    struct sockaddr_in server,new_server,client1,client2;
    int rec;

    char temp;
    /*Declare info*/
    char info;

    /*Make socket */
    socket_fd = socket(AF_INET,SOCK_DGRAM,0);
    if(socket_fd < 0){
        perror("socket creation failed");
        return 0;
    }
    /*Clear the server address and client addreses*/
    memset(&server,'0',sizeof(server));
    
    /*Set port for server address*/
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8080);
    /*Bind the server address*/
    if(bind(socket_fd,(struct sockaddr*)&server,sizeof(server)) < 0){
        perror("bind failed");
        return 0;
    }
    /*Recieve the data from the first client*/
    int client1_len_of_addr,client2_len_of_addr;
    rec = recvfrom(socket_fd,&info,sizeof(info),MSG_WAITALL,(struct sockaddr*)&client1,&client1_len_of_addr);
    /*Display the recieved data*/
    printf("server received : \n");
    printf("%c ",info);
     /*Change the data */
    info = 'r';
    printf("%c ",info);
    close(socket_fd);
    int socket_fd1=0;
    socket_fd1 = socket(AF_INET,SOCK_DGRAM,0);
    if(socket_fd1 < 0){
        perror("socket creation failed");
        return 0;
    }
    memset(&new_server,'0',sizeof(new_server));
    /*Set port for server address*/
    new_server.sin_family = AF_INET;
    new_server.sin_addr.s_addr = INADDR_ANY;
    new_server.sin_port = htons(4040);

    if(bind(socket_fd1,(struct sockaddr*)&new_server,sizeof(new_server)) < 0){
        perror("bind failed");
        return 0;
    }
    /*Recieve something dummy from client2 so that server can send the changed data to the 2nd second client*/
    rec = recvfrom(socket_fd1,&temp,sizeof(temp),MSG_WAITALL,(struct sockaddr*)&client2,&client2_len_of_addr);
    /*Send the changed data to the client 2*/
    sendto(socket_fd1,&info,sizeof(info),MSG_CONFIRM,(const struct sockaddr *)&client2,sizeof(client2));
    /*Close the socket */
    
    return 0;
}
