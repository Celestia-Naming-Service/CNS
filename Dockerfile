FROM alpine:latest
FROM golang:1.19.1-alpine

EXPOSE 26659
EXPOSE 26658
 
COPY --from=golang:1.19.1-alpine /usr/local/go/ /usr/local/go/
 
ENV PATH="/usr/local/go/bin:${PATH}"

RUN apk update
RUN apk add curl tar wget clang pkgconfig libressl-dev jq alpine-sdk bash 
RUN rm -rf celestia-node && git clone https://github.com/celestiaorg/celestia-node.git && cd celestia-node && git checkout tags/v0.5.0-rc5 && make install && make cel-key && celestia light init