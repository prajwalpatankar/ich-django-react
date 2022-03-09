import './App.css';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Home from './components/Home';

function App() {



  return (

    <BrowserRouter>
      <div className="App-mis">
        <Switch >
          <Route exact path='/' component={Home} />
          {/* <Route component={PageNotFound} /> */}
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;