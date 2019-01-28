#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int socket_fd = 0;
	char buff[1024];

	memset(buff, '0',sizeof(buff));

	socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_fd<0){
		perror("socket creation failed");
		return 0;
	}

	struct sockaddr_in server;
	memset(&server,'0',sizeof(server));

	server.sin_family = AF_INET;
	server.sin_port =  htons(8080);

    int in;
	if((in = inet_pton(AF_INET,"127.0.0.1", &server.sin_addr)) < 0){
		perror("IP not initialized succesfully");
		return 0;
	}

	in = connect(socket_fd, (struct sockaddr *)&server, sizeof(server));
	if(in < 0){
		perror("connection failed.");
		return 0;
	}

	printf("Please enter the message: ");
    bzero(buff,256);
    fgets(buff,255,stdin);
    in = send(socket_fd,buff,strlen(buff),0);
	if (in < 0){
		perror("error\n");
	    return 0;
	}
    bzero(buff,256);
	in = recv(socket_fd,buff,255,0);
	if (in < 0){
  		perror("error\n");
  		return 0;
	}
	printf("message received : %s\n",buff);
    close(in);
    close(socket_fd);
	return 0;
}
