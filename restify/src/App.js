//import logo from './logo.svg';
import './App.css';

import React, { useState } from 'react';
//import Login from './components/Login';
import Router from "./components/Router";

function App() {
  const [token, setToken] = useState();

  //if(!token) {
  //  return <Login setToken={setToken} />
  //}

  return (
        <Router />
    //<div className="App">
    //  <header className="App-header">
    //    <img src={logo} className="App-logo" alt="logo" />
    //    <p>
    //      Edit <code>src/App.js</code> and save to reload.
    //    </p>
    //    <a
    //      className="App-link"
    //      href="https://reactjs.org"
    //      target="_blank"
    //      rel="noopener noreferrer"
    //    >
    //      Learn React
    //    </a>
    //  </header>
    //</div>
  );
}

export default App;
