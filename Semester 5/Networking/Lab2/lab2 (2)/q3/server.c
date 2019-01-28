#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

void solu(char *buff){
    int a = atoi(buff);
    switch (a){
        case(0):
            strcpy(buff,"Bob");
            break;
        case(3):
            strcpy(buff,"Anne");
            break;
        case(5):
            strcpy(buff,"Barbe");
            break;
        case(7):
            strcpy(buff,"Ray");
            break;
        case(9):
            strcpy(buff,"Denbigh");
            break;
        case(10):
            strcpy(buff,"Terri");
            break;
        case(104):
            strcpy(buff,"John");
            break;                       
        default:
            strcpy(buff,"Not Found!");
            break;
    }
}
int main()
{
	int socket_fd = 0;
	char buff[1024];

	memset(buff, '0',sizeof(buff));

	socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_fd<0){
		perror("socket creation failed\n");
		return 0;
	}

	struct sockaddr_in server;
	memset(&server,'0',sizeof(server));

	server.sin_family = AF_INET;
	server.sin_port = htons(8080);
    server.sin_addr.s_addr = htonl(INADDR_ANY);

	bind(socket_fd, (struct sockaddr*)&server, sizeof(server));

	listen(socket_fd, 10);
    socklen_t addr_size;
    addr_size = sizeof(struct sockaddr_in);

    int in;
	if(in = accept(socket_fd,(struct sockaddr*)&server,&addr_size)){
		int n;
		bzero(buff,256);
		if((n = recv(in, buff, 256,0)) > 0){
			printf("message received : %s\n",buff);
			solu(buff);
			send(in, buff, strlen(buff), 0);
			bzero(buff,256);
		}
		close(in);
	}
    close (socket_fd);
}
