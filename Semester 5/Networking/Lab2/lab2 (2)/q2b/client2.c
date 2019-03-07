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
    int socket_fd;
    struct sockaddr_in server;
    char *hello = "client2";
    int rec;

    struct Info info;

    socket_fd = socket(AF_INET,SOCK_DGRAM,0);
    if(socket_fd < 0){
        perror("socket creation failed");
        return 0;
    }

    memset(&server,'0',sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8080);

    sendto(socket_fd,(const char *)hello, strlen(hello),MSG_CONFIRM, (const struct sockaddr *)&server,sizeof(server));

    int len_addr;
    rec = recvfrom(socket_fd,&info,sizeof(info),MSG_WAITALL, (struct sockaddr *)&server,&len_addr);
    printf("client2 received : \n");
    printf("%c  ",info.letter);
    printf("%d  ",info.val1);
    printf("%f\n",info.val2);

    close(socket_fd);
    return 0;
}
