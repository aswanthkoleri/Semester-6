#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

int main(int argc, char const *argv[])
{
    struct sockaddr_in address;
    int socket_fd,valread;
    struct sockaddr_in server;

    char *hello;
    char buffer[1024];

    memset(buffer,'0',sizeof(buffer));
    
    socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_fd < 0){
        printf("socket creation failed\n");
        return 0;
    }
  
    memset(&server,'0',sizeof(server));
  
    server.sin_family = AF_INET;
    server.sin_port = htons(atoi("1234"));
    
    int in;
    if(in = inet_pton(AF_INET, "127.0.0.1", &server.sin_addr) < 0){
        printf("invalied address\n");
        return 0;
    }

    in = connect(socket_fd,(struct sockaddr *)&server, sizeof(server));
	if(in < 0){
		perror("connection failed\n");
		return 0;
	}

	while(1){
		printf("Enter the message: ");
        bzero(buffer,256);
    	fgets(buffer,255,stdin);
    	in = send(socket_fd,buffer,strlen(buffer),0);
		if (in < 0){
		    perror("writing to server failed\n");
			return 0;
		}
		bzero(buffer,256);
		in = recv(socket_fd,buffer,255,0);
		if (in < 0){
  		    perror("reading from server failed\n");
  		    return 0;
		}
		printf("received from server: %s \n",buffer);
        bzero(buffer,256);
        close(in);
	}
    close(socket_fd);
    return 0;
}
