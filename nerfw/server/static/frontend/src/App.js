import './stylesheets/App.css';
import RoutesHome from './routes'
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <RoutesHome />
    </BrowserRouter>
  );
}

export default App;
