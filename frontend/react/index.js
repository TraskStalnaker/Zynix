import React from "react";
import ReactDOM from "react-dom";
import Dashboard from "./components/Dashboard";
import "./styles/global.css";

const App = () => {
  return (
    <div className="container">
      <Dashboard />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
