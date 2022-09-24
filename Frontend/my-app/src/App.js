import { Fragment } from 'react';
import './App.css';
import Camera from './Components/Camera';
import {Sound} from './Components/Sound'

function App() {
  return (
    <Fragment>
      <Sound />
      <Camera />
    </Fragment>
  );
}

export default App;
