# Start with the Golang Alpine base image
FROM golang:alpine

# Install Docker and other dependencies
RUN apk update && \
    apk add --no-cache \
    bash \
    ca-certificates \
    iptables \
    curl \
    make \
    libc6-compat \
    build-base \
    gcc \
    g++


# Set up the working directory for the application
WORKDIR /go/src/mosn

# Copy the local MOSN files into the container
COPY ./mosn /go/src/mosn

# # Build MOSN inside the container
RUN make build-local
WORKDIR /go/src/mosn/cmd/mosn/main
RUN go build .

RUN apk update && \
    apk add --no-cache \
    bash \
    zsh \
    git \
    openssl && \
    # Install Oh My Zsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    # Set Zsh as the default shell
    # Clean up
    apk del git && \
    mv main /go/src/mosn/examples/codes/http-sample
# RUN go run /go/src/mosn/examples/codes/http-sample/server.go
WORKDIR /go/src/mosn/examples/codes/http-sample
RUN go build server.go && apk add nano
# Set environment variables for MOSN
# ENV CONFIG_FILE=/go/src/mosn/build/bundles/v1.6.0/binary/mosn_config.json
# # Expose port 2045 for MOSN or any other port you plan to use
# EXPOSE 2045

# # Start Docker daemon and run a Bash shell for interaction
# CMD ["sh", "-c", "dockerd & bash"]
CMD ["zsh"]
