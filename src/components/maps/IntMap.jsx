import * as React from 'react';
import ReactMapGl from 'react-map-gl';

function Map() {
  const [viewState, setViewState] = React.useState({
    longitude: -100,
    latitude: 40,
    zoom: 3.5
  });

  return <ReactMapGl
    {...viewState}
    onMove={evt => setViewState(evt.viewState)}
    mapStyle="mapbox://styles/vinzi0812/clv6jps7r00m601qr98yg8ef2"
    mapboxAccessToken = "pk.eyJ1IjoidmluemkwODEyIiwiYSI6ImNsdjZnY3oyZTBmazQycXFmaTRheGlleGQifQ.ObEhAN1o246llp-AhpYetg"
    style = {{width: '100vw' , height:'100vh'}}
  />;
}

export default Map
