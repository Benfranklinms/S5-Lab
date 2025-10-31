#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080
#define BUFFER_SIZE 256
#define LOCAL_HOST "127.0.0.1"

void error_check(int x, char success[]){
    if(x < 0) {
        perror("Error");
        exit(1);
    }
    else {
        printf("%s", success);
    }
}

struct sockaddr_in create_socket_address() {
    struct sockaddr_in socket_address;
    socket_address.sin_family = AF_INET;
    socket_address.sin_port = htons(PORT);
    socket_address.sin_addr.s_addr = inet_addr(LOCAL_HOST);
}

int main() {
    int server_sock = socket(AF_INET, SOCK_STREAM, 0);
    error_check(server_sock, "Server socket successfully created");

    struct sockaddr_in server_address = create_socket_address();
    int b = bind(server_sock, (struct sockaddr *)&server_address, sizeof(server_address));
    error_check(b, "Binding successfull");

    int l = listen(server_sock, 5);
    error_check(l, "Listening for connections...");

    struct sockaddr_in client_address;
    int client_sock = accept(server_sock, (struct sockaddr *)&client_address, sizeof(client_address));
    error_check(client_sock, "Accepted connection from client");

    char buffer[BUFFER_SIZE] = "";
    char reply[] = "Hello, this is the server...";

    int status = recv(client_sock, buffer, BUFFER_SIZE, 0);
    error_check(status, "Message received from client:");
    printf("Client says: %s\n", buffer);

    status = send(client_sock, reply, strlen(reply), 0);
    error_check(status, "Reply successfully sent to client");

    close(client_sock);
    close(server_sock);
}