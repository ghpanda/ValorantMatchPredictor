import { Link } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <h1>Hello World!</h1>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default App;