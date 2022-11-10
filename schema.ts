type address = string;
type domain_name = string;

type state = { [domain_name: string]: address };

// in the future
type metadata = {
    address,
    content: string
}
type stateV2 = { [domain_name: string]: metadata };


// important part here!
type action = {
    type: "REGISTER_NAME" | "TRANSFER_NAME",
    signature: string,
    payload: {
        // register name payload
        name: domain_name
    } | {
        // tranfer name payload
        name: domain_name,
        recipient: address
    }
}