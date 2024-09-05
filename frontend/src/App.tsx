import React from 'react';
import {BrowserRouter} from "react-router-dom";
import RoutesHome from "./routes/routes";

function App() {
  return (
    <BrowserRouter>
        <RoutesHome />
    </BrowserRouter>
  );
}

export default App;
