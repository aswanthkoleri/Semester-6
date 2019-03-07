#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

struct Info{
    char letter;
    int val1;
    float val2;
};

int main(int argc, char const *argv[])
{
    int socket_fd = 0;
    struct sockaddr_in server,client,sendclient;
    int rec;
    char temp[10];
    
    struct Info info;

    memset(temp,'0',sizeof(temp));

    socket_fd = socket(AF_INET,SOCK_DGRAM,0);
    if(socket_fd < 0){
        perror("socket creation failed");
        return 0;
    }

    memset(&server,'0',sizeof(server));
    memset(&client,'0',sizeof(client));
    memset(&sendclient,'0',sizeof(sendclient));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8080);

    if(bind(socket_fd,(struct sockaddr*)&server,sizeof(server)) < 0){
        perror("bind failed");
        return 0;
    }
    socklen_t send_addr_size;
    int len_addr,send_len_addr;
    rec = recvfrom(socket_fd,&info,sizeof(info),MSG_WAITALL,(struct sockaddr*)&client,&len_addr);
    printf("server received : \n");
    printf("%c  \n",info.letter);
    if(info.letter == 'a'){ info.letter = 'z'; }
    else if(info.letter == 'A'){ info.letter = 'Z'; }
    else{ info.letter = info.letter-1; }

    rec = recvfrom(socket_fd,temp,1000,MSG_WAITALL,(struct sockaddr*)&sendclient,&send_len_addr);
    //rec : bytes received.
    //MSG_WAITALL. It tells that the syscall should not return before length bytes are read.

    sendto(socket_fd,&info,sizeof(info),MSG_CONFIRM,(const struct sockaddr *)&sendclient,send_len_addr);

    close(socket_fd);
    return 0;
}
