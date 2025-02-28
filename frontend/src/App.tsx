import { BrowserRouter as Router } from "react-router-dom";
import RoutesComponent from "./routes"; // Import the Routes file
import AppNavbar from "./components/NavBar";

function App() {
  return (
    <Router>
      <AppNavbar />
      <RoutesComponent />
    </Router>
  );
}

export default App;
