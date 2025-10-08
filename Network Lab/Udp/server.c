#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080
#define BUFFER_SIZE 256
#define LOCALHOST "127.0.0.1"

void check(int x, char msg[]) {
    if (x < 0) {
        perror("something went wrong");
        exit(1);
    } else {
        printf("%s\n", msg);
    }
}

struct sockaddr_in create_socket_address() {
    struct sockaddr_in socket_address;
    socket_address.sin_family = AF_INET;
    socket_address.sin_addr.s_addr = inet_addr(LOCALHOST);
    socket_address.sin_port = htons(PORT);
    return socket_address;
}

int main() {
    // 1. Create UDP socket
    int server_sock = socket(AF_INET, SOCK_DGRAM, 0);
    check(server_sock, "UDP server socket created successfully");

    // 2. Bind to localhost:8080
    struct sockaddr_in server_address = create_socket_address();
    int b = bind(server_sock, (struct sockaddr *)&server_address, sizeof(server_address));
    check(b, "Binding successful");

    // 3. Wait for message from client
    char buffer[BUFFER_SIZE];
    struct sockaddr_in client_address;
    socklen_t client_len = sizeof(client_address);

    printf("Server is listening on %s:%d ...\n", LOCALHOST, PORT);

    int status = recvfrom(server_sock, buffer, BUFFER_SIZE, 0,
                          (struct sockaddr *)&client_address, &client_len);
    check(status, "Message received from client");

    buffer[status] = '\0';  // null-terminate
    printf("Client (%s:%d) says: %s\n",
           inet_ntoa(client_address.sin_addr),
           ntohs(client_address.sin_port),
           buffer);

    // 4. Send reply to client
    char reply[] = "Hello, this is the UDP server!";
    status = sendto(server_sock, reply, strlen(reply), 0,
                    (struct sockaddr *)&client_address, client_len);
    check(status, "Reply sent to client");

    // 5. Close socket
    close(server_sock);
    printf("Server closed.\n");
    return 0;
}
