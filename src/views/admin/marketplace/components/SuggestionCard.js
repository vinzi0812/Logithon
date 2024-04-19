import React from 'react';
import '@fortawesome/fontawesome-free/css/all.css';
import avatarImage from "../../../../assets/img/avatars/stockman.jpg"
import { background } from '@chakra-ui/system';
import { ImFontSize } from 'react-icons/im';



const SuggestionCard = () => {
    const container = styles.container;
  return (
    <div className="card" style={styles.card}>
        <div className="details" style={styles.details}>
            <div className="profile" style={styles.profile}>
                <img src={avatarImage} alt="Profile" style={styles.profileImg} />
            </div>
            <div className="text-details" style={styles.textDetails}>
                <div className="name-time" style={styles.nameTime}>
                    <div className="name">
                        John Doe
                    </div>
                    <div className="time-taken" style={styles.timeTaken}>
                        <i className="far fa-clock" style={styles.icont}></i> 2 hours ago
                    </div>
                </div>
                <div className="other-details" style={styles.otherDetails}>
                    <div className="name-time" style={styles.nameTime}>
                        <div className="cost">
                            <i className="fas fa-dollar-sign" style={styles.icont}></i> $ 50
                        </div>
                        <div className="carbon-emission" style={styles.timeTaken}>
                            <i className="fas fa-cloud" style={styles.icont}></i> 5kg CO2
                        </div>
                    </div>
                    <div className="source-destination" style={styles.detailItem}>
                        <i className="fas fa-map-marker-alt" style={styles.icont} marginRight = '50px'></i> Source: Location A -----<i className="fas fa-map-marker-alt" marginRight='50px' style={styles.icon}></i> Destination: Location B
                    </div>
                </div>
            </div>  
        </div>
        
        <div style={styles.path}>
            <div style={styles.iconContainer}>
                <div style={styles.icon}><i className="fas fa-car"></i></div>
                <div style={styles.line}></div>
            </div>
            <div style={styles.iconContainer}>
                <div style={styles.icon}><i className="fas fa-train"></i></div>
                <div style={styles.line}></div>
            </div>
            <div style={styles.iconContainer}>
                <div style={styles.icon}><i className="fas fa-plane"></i></div>
            </div>
        </div>
        {/* <div style={container}>
        <div style={styles.hr} />
        <div style={styles.or}>or</div>
        </div> */}
    </div>

  );
}



const styles = {
  card: {
    display: 'flex',
    flexDirection: 'column',
    borderRadius: '20px',
    padding: '20px',
    margin: '10px',
    background: '#111C44',
  },
  details: {
    display: 'flex',
    flexDirection: 'row',
    flex: 1,
  },
  profile: {
    marginRight: '30px',
  },
  profileImg: {
    width: '120px',
    height: '110px',
    borderRadius: '50%',
  },
  textDetails: {
    width: '100%',
    flexDirection: 'column',
    justifyContent: 'space-between',
  },
  nameTime: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '15px'
  },
  otherDetails: {
    marginTop: '10px',
    
  },
  detailItem: {
    marginBottom: '5px',
  },
  path: {
    flex: 1,
    display: 'flex',
    alignItems: 'center',
  },
  timeline: {
    display: 'flex',
    alignItems: 'center',
  },
  icont: {
    marginRight: '10px',
  },
  container: {
    flex: 0,
    backgroundColor: '#FFFFFF',
    width: '100%',
  },
  path: {
    position: 'relative',
    display: 'flex',
    alignItems: 'center',
  },
  iconContainer: {
    position: 'relative',
    flex: 1,
    textAlign: 'center',
  },
  icon: {
    position: 'absolute',
    top: '50%',
    transform: 'translateY(-50%)',
  },
  line: {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -1px)',
    width: '100%',
    height: 2,
    backgroundColor: '#FFFFFF',
  },
  hr: {
    position: 'relative',
    top: 11,
    borderBottom: '1px solid #000000',
  },
  or: {
    width: 30,
    fontSize: 14,
    textAlign: 'center',
    alignSelf: 'center',
    backgroundColor: '#FFFFFF',
  },

};

export default SuggestionCard;
