import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App"; 


//grabs index.html by id
const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

//route to App.js
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
