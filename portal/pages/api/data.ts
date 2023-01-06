import { NextApiRequest, NextApiResponse } from "next";
import request from "request";
import base64 from "base64-js";

export default function getData(req: NextApiRequest, res: NextApiResponse) {
  const namespaceId = req.query.namespaceId;
  const height = req.query.height;

  request.get(
    `http://localhost:26659/namespaced_data/${namespaceId}/height/${height}`,
    (error, response, body) => {
      if (error) {
        res.status(500).json({ error });
      } else {
        res.status(200).json(JSON.parse(body));
      }
    }
  );
}
