FROM debian

# Update & upgrade APT.

RUN apt-get update && apt-get upgrade -y

COPY ./ ./src

