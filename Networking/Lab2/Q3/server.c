#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

void check_dict(char* buff){
	if(strncmp(buff,"0",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Bob", 100);
	}
	else if(strncmp(buff,"3",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Anne", 100);
	}
	else if(strncmp(buff,"5",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Barbe", 100);
	}
	else if(strncmp(buff,"7",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Ray", 100);
	}
	else if(strncmp(buff,"9",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Denbigh", 100);
	}
	else if(strncmp(buff,"10",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "Terri", 100);
	}
	else if(strncmp(buff,"104",strlen(buff))==10){
		bzero(buff,256);
		strncpy(buff, "John", 100);
	}
	else{
		bzero(buff,256);
		strncpy(buff, "Address Not Found", 100);
	}
}
int main()
{
	int fd = 0;
	char buff[1024];

	//Setup Buffer Array
	memset(buff, '0',sizeof(buff));

	//Create Socket
	fd = socket(AF_INET, SOCK_STREAM, 0);
  if(fd<0){
		perror("Client Error: Socket not created succesfully");
		return 0;
	}

	//Structure to store details
	struct sockaddr_in server;
	memset(&server, '0', sizeof(server));

	//Initialize
	server.sin_family = AF_INET;
	server.sin_port = htons(10011);
  server.sin_addr.s_addr = htonl(INADDR_ANY);

	bind(fd, (struct sockaddr*)&server, sizeof(server));

	int in;

	listen(fd, 10);
  socklen_t addr_size;
  addr_size = sizeof(struct sockaddr_in);
	if(in = accept(fd,(struct sockaddr*)&server,&addr_size))
	{
		  int n;

			//printf ("\nOne Client Connected !! ");

			//close listening socket
		close (fd);

			//Clear Zeroes
			bzero(buff,256);

			while ( (n = recv(in, buff, 256,0)) > 0)
			{

				printf("Server Received: %s",buff);
				// printf("%d\n",strncmp(buff,"0",strlen(buff)));
				// printf("%d\n",strncmp(buff,"3",strlen(buff)));
				// printf("%d\n",strncmp(buff,"5",strlen(buff)));
				// printf("%d\n",strncmp(buff,"7",strlen(buff)));
				// printf("%d\n",strncmp(buff,"9",strlen(buff)));
				// printf("%d\n",strncmp(buff,"10",strlen(buff)));
				// printf("%d\n",strncmp(buff,"104",strlen(buff)));
				check_dict(buff);
				send(in, buff, strlen(buff), 0);
				bzero(buff,256);
			}
			close(in);
	}
		
}
