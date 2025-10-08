#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080
#define LOCALHOST "127.0.0.1"
#define BUFFER_SIZE 256

void check(int x, char msg[]) {
    if (x < 0) {
        perror("something went wrong");
        exit(1);
    } else {
        printf("%s\n", msg);
    }
}

struct sockaddr_in create_server_address() {
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = inet_addr(LOCALHOST);
    return addr;
}

int main() {
    // 1. Create UDP socket
    int client_sock = socket(AF_INET, SOCK_DGRAM, 0);
    check(client_sock, "UDP client socket created successfully");

    // 2. Create server address
    struct sockaddr_in server_address = create_server_address();

    // 3. Send message to server
    char message[] = "Hello, this is the UDP client!";
    int status = sendto(client_sock, message, strlen(message), 0,
                        (struct sockaddr *)&server_address, sizeof(server_address));
    check(status, "Message sent to server");

    // 4. Receive reply from server
    char buffer[BUFFER_SIZE];
    socklen_t addr_len = sizeof(server_address);
    status = recvfrom(client_sock, buffer, BUFFER_SIZE, 0,
                      (struct sockaddr *)&server_address, &addr_len);
    check(status, "Reply received from server");
    buffer[status] = '\0';
    printf("Server says: %s\n", buffer);

    // 5. Close socket
    close(client_sock);
    printf("Client closed.\n");

    return 0;
}
