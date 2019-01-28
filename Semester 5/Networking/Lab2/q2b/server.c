#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#pragma pack(1)
struct Info{
    char letter;
    int val1;
    float val2;
};
#pragma pack(0)

int main(int argc, char const *argv[])
{
    int socket_fd = 0;
    struct sockaddr_in server,client1,client2;
    int rec;

    char temp[10];
    /*Declare info*/
    struct Info info;

    memset(temp,'0',sizeof(temp));
    /*Make socket */
    socket_fd = socket(AF_INET,SOCK_DGRAM,0);
    if(socket_fd < 0){
        perror("socket creation failed");
        return 0;
    }
    /*Clear the server address and client addreses*/
    memset(&server,'0',sizeof(server));
    memset(&server,'0',sizeof(client1));
    memset(&server,'0',sizeof(client2));
    /*Set port for server address*/
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8080);
    /*Bind the server address*/
    if(bind(socket_fd,(struct sockaddr*)&server,sizeof(server)) < 0){
        perror("bind failed");
        return 0;
    }
    
    int client1_len_of_addr,client2_len_of_addr;
/*Recieve the data from the first client*/
    rec = recvfrom(socket_fd,&info,sizeof(info),MSG_WAITALL,(struct sockaddr*)&client1,&client1_len_of_addr);
    /*Display the recieved data*/
    printf("server received : \n");
    printf("%c  ",info.letter);
    printf("%d  ",info.val1);
    printf("%f\n",info.val2);
    /*Change the data */
    info.letter = 'r';
    info.val1 = 8;
    info.val2 = 9.1;
    /*Recieve something dummy from client2 so that server can send the changed data to the 2nd second client*/
    rec = recvfrom(socket_fd,&temp,sizeof(temp),MSG_WAITALL,(struct sockaddr*)&client2,&client2_len_of_addr);
    /*Send the changed data to the client 2*/
    sendto(socket_fd,&info,sizeof(info),MSG_CONFIRM,(const struct sockaddr *)&client2,sizeof(client2));
    /*Close the socket */
    close(socket_fd);
    return 0;
}
