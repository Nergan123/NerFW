import React from 'react';
import {BrowserRouter} from "react-router-dom";
import RoutesHome from "./routes/routes";
import {BackgroundProvider} from "./utils/backgroundProvider";

function App() {
  return (
    <BrowserRouter>
        <BackgroundProvider>
            <RoutesHome />
        </BackgroundProvider>
    </BrowserRouter>
  );
}

export default App;
