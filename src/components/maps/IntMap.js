import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const IntMap = () => {
    const markers = [
        { lat: 51.5074, lng: -0.1278, name: 'London' },
        { lat: 40.7128, lng: -74.0060, name: 'New York' },
        { lat: 48.8566, lng: 2.3522, name: 'Paris' },
        // Add more markers as needed
    ];

    return (
        <MapContainer center={[51.5074, -0.1278]} zoom={3} style={{ height: '400px', width: '100%' }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {markers.map((marker, index) => (
                <Marker key={index} position={[marker.lat, marker.lng]}>
                    <Popup>{marker.name}</Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

export default IntMap;