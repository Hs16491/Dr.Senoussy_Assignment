const express = require("express");
const app = express();

app.get("/users", (req, res) => {
  res.json([{ id: 1, name: "Habiba" }]);
});

app.listen(3000, () => {
  console.log("User Service running");
});
