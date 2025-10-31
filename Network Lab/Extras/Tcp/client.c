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

void check(int x, char success[]) {
    if (x < 0) {
        perror("something went wrong");
        exit(1);
    } else {
        printf("%s\n", success);
    }
}

struct sockaddr_in create_client_address() {
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = inet_addr(LOCALHOST);
    return addr;
}

int main() {
    // 1. Create client socket
    int s = socket(AF_INET, SOCK_STREAM, 0);
    check(s, "Client socket created successfully");

    // 2. Connect to the server
    struct sockaddr_in server_address = create_client_address();
    int c = connect(s, (struct sockaddr *)&server_address, sizeof(server_address));
    check(c, "Connected to server");

    // 3. Prepare and send message to server
    char buffer[BUFFER_SIZE] = "";
    char message[] = "Hello, this is the client!";

    int status = send(s, message, strlen(message), 0);
    check(status, "Message sent to server");

    // 4. Receive reply from server
    memset(buffer, 0, BUFFER_SIZE);
    status = recv(s, buffer, BUFFER_SIZE, 0);
    check(status, "Reply received from server:");
    printf("Server says: %s\n", buffer);

    // 5. Close socket
    close(s);
    printf("Connection closed.\n");

    return 0;
}
