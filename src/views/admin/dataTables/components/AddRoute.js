import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Flex, Icon, Image, Text, useColorModeValue } from "@chakra-ui/react";
import SuggestionCard from "../../marketplace/components/SuggestionCard"

const AddRoute = () => {
  const history = useHistory();
  const [step, setStep] = useState(1);
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [transportModes, setTransportModes] = useState([]);
  const [routes, setRoutes] = useState([]);
  const textColor = useColorModeValue("secondaryGray.900", "white");
  const borderColor = useColorModeValue("gray.200", "whiteAlpha.100");
  const iconColor = useColorModeValue("brand.500", "white");
  
  const handleNext = () => {
    setStep(step + 1);
  };

  const handleBack = () => {
    setStep(step - 1);
  };

  const handleOriginChange = (e) => {
    setOrigin(e.target.value);
  };

  const handleDestinationChange = (e) => {
    setDestination(e.target.value);
  };

  const handleCheckboxChange = (mode) => {
    if (transportModes.includes(mode)) {
      setTransportModes(transportModes.filter(item => item !== mode));
    } else {
      setTransportModes([...transportModes, mode]);
    }
  };

  const handleSubmit = () => {
    // Here you would typically fetch routes from an API based on user preferences
    // For demo purpose, generating some sample routes
    const generatedRoutes = [
      { name: 'Route 1', timeTaken: '2 hours', cost: '$50', transportPercentage: { car: 50, train: 30, plane: 20 } },
      { name: 'Route 2', timeTaken: '3 hours', cost: '$60', transportPercentage: { car: 40, train: 50, plane: 10 } },
      { name: 'Route 3', timeTaken: '4 hours', cost: '$70', transportPercentage: { car: 60, train: 20, plane: 20 } },
    ];
    setRoutes(generatedRoutes);
    setStep(step + 1)
  };

  const renderStepContent = () => {
    switch (step) {
      case 1:
        return (
          <div className='inputContainer'>
            <input style={styles.inputBox} type="text" value={origin} onChange={handleOriginChange} placeholder='Enter Origin'/>
          </div>
        );
      case 2:
        return (
          <div className='inputContainer'>
            <input style={styles.inputBox} type="text" value={destination} onChange={handleDestinationChange} placeholder='Enter Destination'/>
          </div>
        );
    //   case 3:
    //     return (
    //       <div>
    //         <h2>Choose Transport Modes</h2>
    //         <div>
    //           <input type="checkbox" id="car" checked={transportModes.includes('car')} onChange={() => handleCheckboxChange('car')} />
    //           <label htmlFor="car">Car</label>
    //         </div>
    //         <div>
    //           <input type="checkbox" id="train" checked={transportModes.includes('train')} onChange={() => handleCheckboxChange('train')} />
    //           <label htmlFor="train">Train</label>
    //         </div>
    //         <div>
    //           <input type="checkbox" id="plane" checked={transportModes.includes('plane')} onChange={() => handleCheckboxChange('plane')} />
    //           <label htmlFor="plane">Plane</label>
    //         </div>
    //       </div>
    //     );
      default:
        return null;
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.box}>
        {step !== 3 ? (
          <div className={styles.innerContainer}>
            {renderStepContent()}
            <div style={styles.buttonContainer}>
              {step > 1 && step < 3 && <button onClick={handleBack}>Back</button>}
              <button onClick={step === 2 ? handleSubmit : handleNext}>{step === 2 ? 'Submit' : 'Next'}</button>
            </div>
          </div>
        ) : (
          <div className={styles.bigBox}>
          <SuggestionCard />
          <SuggestionCard />
          <SuggestionCard />
          <SuggestionCard />
          </div>
        )}
      </div>
    </div>
  );
};

const styles = {

  page: {
    display: 'flex',
    width: '100%',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    backgroundColor: 'iconColor',
  },
  inputBox:{
    width: '100%',
    padding: '10px',
  },
  innerContainer:{
    width: '30%',
  },
  h2:{
    color:'textColor',
  },
  box: {
    width: '90%',
    maxWidth: '1000px',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#iconColor',
    padding: '20px',
  },
  bigBox:{
    width: '100%',
  },
  buttonContainer: {
    marginTop: '20px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',

  },
  inputContainer: {

  }
};

export default AddRoute;
