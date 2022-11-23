# Celestia Naming Service ☄️

Celestia Naming Service is a name service like [ENS](ENS.domains) built with celestia's Data Availbility Sampling aka [DAS](https://docs.celestia.org/concepts/how-celestia-works/data-availability-layer/) layer using the [Node API](https://docs.celestia.org/developers/node-api/#endpoints). Instead of having a long and inconvenient address, you can use CNS to register a human readable name for your wallet address.


## Run Locally 

We'll need to setup an Arabica celestia light node before we can make calls to DAS.

The easiest way is to get a docker container running using this dockerfile 🐳

```dockerfile
FROM alpine:latest
FROM golang:1.19.1-alpine

EXPOSE 26659
EXPOSE 26658
 
COPY --from=golang:1.19.1-alpine /usr/local/go/ /usr/local/go/
 
ENV PATH="/usr/local/go/bin:${PATH}"

RUN apk update
RUN apk add curl tar wget clang pkgconfig libressl-dev jq alpine-sdk bash 
RUN rm -rf celestia-node && git clone https://github.com/celestiaorg/celestia-node.git && cd celestia-node && git checkout tags/v0.5.0-rc5 && make install && make cel-key && celestia light init
```

Lastly, setup and fund the wallet on the node using this [guide](https://docs.celestia.org/developers/wallet/#fund-a-wallet) 📚

et volia! Now you can run the commands in the Python notebook.
    
## Roadmap

- [x] Post address and name data to a namespace
- [x] Naive verification of data in a namespace
- [ ] Update state after txns to allow transfers and sells of names
- [ ] Actual verification of legitimate transactions
- [ ] Frontend site with keplr integration to buy a domain name


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)