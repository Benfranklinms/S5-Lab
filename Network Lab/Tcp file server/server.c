#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fcntl.h>

#define PORT 8080
#define BUFFER_SIZE 256

int main() {
    int server_fd, client_fd;
    struct sockaddr_in address;
    char buffer[BUFFER_SIZE];

    // 1. Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // 2. Bind and listen
    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 5);
    printf("TCP File Server running on port %d...\n", PORT);

    while (1) {
        socklen_t addrlen = sizeof(address);
        client_fd = accept(server_fd, (struct sockaddr*)&address, &addrlen);

        // 3. Read filename from client
        memset(buffer, 0, BUFFER_SIZE);
        read(client_fd, buffer, BUFFER_SIZE);
        printf("Client requested: %s\n", buffer);

        // 4. Open file
        int fd = open(buffer, O_RDONLY);
        if (fd < 0) {
            snprintf(buffer, BUFFER_SIZE, "Server PID: %d\nFile not found.\n", getpid());
            write(client_fd, buffer, strlen(buffer));
        } else {
            snprintf(buffer, BUFFER_SIZE, "Server PID: %d\n", getpid());
            write(client_fd, buffer, strlen(buffer));

            ssize_t n;
            while ((n = read(fd, buffer, BUFFER_SIZE)) > 0) {
                write(client_fd, buffer, n);
            }
            close(fd);
        }

        close(client_fd); // Done with this client
    }

    return 0;
}
