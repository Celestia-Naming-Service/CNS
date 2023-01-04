import requests from "request";
import base64 from "base64-js";

function getData(namespaceId: string, height: number) {
  const r = requests.get(
    `http://localhost:26659/namespaced_data/${namespaceId}/height/${height}`
  );
  return r.json();
}

function parse(data: string) {
  const decodedData = base64.decode(data).toString("utf-8");
  return decodedData;
}

function postData(namespaceId: string, data: any, gasLimit: number = 70000) {
  const dataString = JSON.stringify(data);
  const dataBuffer = Buffer.from(dataString, "utf-8");
  const dataHex = dataBuffer.toString("hex");
  const r = requests.post(`http://localhost:26659/submit_pfd`, {
    json: { namespaceId, data: dataHex, gasLimit },
  });
  console.log(r.json());
  console.log(getData("756f60cbe7bf5401", r.json().height));
}

postData("756f60cbe7bf5401", { Pratham: "prasoon.cel" });

interface Action {
  type: string;
  payload?: any;
  signature?: string;
}

const state: { [key: string]: string } = {};

function getAddress(signature: string): string {
  return signature;
}

function isValidAddress(address: string): boolean {
  return typeof address === "string";
}

function updateState(action: Action) {
  const actionType = action.type;
  const address = getAddress(action.signature);
  if (actionType === "REGISTER_NAME") {
    const name = action.payload.name;
    state[name] = address;
  } else if (actionType === "TRANSFER_NAME") {
    const name = action.payload.name;
    const recipient = action.payload.recipient;
    if (state[name] === address && isValidAddress(recipient)) {
      state[name] = recipient;
    }
  }
}

const myNamespace = "756f60cbe7bf5401";
const initialHeight = 27070;
const latestHeight = 27525;

for (let height = initialHeight; height < latestHeight; height += 1) {
  const dataList = getData(myNamespace, height);
  try {
    const parsedData = parse(dataList.data[0]);
    updateState(parsedData);
    console.log(parsedData);
    console.log(dataList);
  } catch (e) {
    // do nothing
  }
}
