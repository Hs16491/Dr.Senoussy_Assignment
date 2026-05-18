const express = require("express");
const axios = require("axios");
const app = express();

app.get("/orders", async (req, res) => {
  try {
    const response = await axios.get("http://user-service:3000/users");
    res.json({
      orderId: 1,
      user: response.data
    });
  } catch (error) {
    res.status(500).json({ error: "User service not available" });
  }
});

app.listen(3000, () => {
  console.log("Order Service running");
});
