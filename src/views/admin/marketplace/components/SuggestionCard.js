import React from 'react';
import '@fortawesome/fontawesome-free/css/all.css';
import avatarImage from "../../../../assets/img/avatars/stockman.jpg"
import { background } from '@chakra-ui/system';
import { ImFontSize } from 'react-icons/im';
import { Flex, Icon, Image, Text, useColorModeValue } from "@chakra-ui/react";
// import Timeline from '@mui/lab/Timeline';
// import TimelineItem from '@mui/lab/TimelineItem';
// import TimelineSeparator from '@mui/lab/TimelineSeparator';
// import TimelineConnector from '@mui/lab/TimelineConnector';
// import TimelineContent from '@mui/lab/TimelineContent';
// import TimelineOppositeContent from '@mui/lab/TimelineOppositeContent';
// import TimelineDot from '@mui/lab/TimelineDot';
// import FastfoodIcon from '@mui/icons-material/Fastfood';
// import LaptopMacIcon from '@mui/icons-material/LaptopMac';
// import HotelIcon from '@mui/icons-material/Hotel';
// import RepeatIcon from '@mui/icons-material/Repeat';
// import Typography from '@mui/material/Typography';


const SuggestionCard = () => {
  const textColor = useColorModeValue("secondaryGray.900", "white");
  const borderColor = useColorModeValue("gray.200", "whiteAlpha.100");
  const iconColor = useColorModeValue("brand.400", "white");
  const container = styles.container;
  return (
    <div style={styles.box}>
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
            {/* <Timeline className={classes.timeline} align="alternate">
              <TimelineItem>
                <TimelineSeparator>
                  <CheckCircleOutlineIcon
                    color="primary"
                    className={classes.timelineIcon}
                  />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className={classes.timelineContentContainer}>
                  <Paper className={classes.timelineContent}>
                    <Typography>Eat</Typography>
                  </Paper>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <PauseCircleFilledIcon
                    color="primary"
                    className={classes.timelineIcon}
                  />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className={classes.timelineContentContainer}>
                  <Paper className={classes.timelineContent}>
                    <Typography>Code</Typography>
                  </Paper>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <CachedIcon color="primary" className={classes.timelineIcon} />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className={classes.timelineContentContainer}>
                  <Paper className={classes.timelineContent}>
                    <Typography>Sleep</Typography>
                  </Paper>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <CachedIcon color="primary" className={classes.timelineIcon} />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className={classes.timelineContentContainer}>
                  <Paper className={classes.timelineContent}>
                    <Typography>Repeat</Typography>
                  </Paper>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <ErrorIcon color="primary" className={classes.timelineIcon} />
                </TimelineSeparator>
                <TimelineContent className={classes.timelineContentContainer}>
                  <Paper className={classes.timelineContent}>
                    <Typography>Sleep</Typography>
                  </Paper>
                </TimelineContent>
              </TimelineItem>
            </Timeline> */}
          </div>
        </div>
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
    background: 'borderColor',
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
  timeline: {
    listStyle: 'none',
    padding: '20px',
    position: 'relative',
  },
  button: {
    position: 'absolute',
    top: 'auto',
    bottom: '30px',
  },
  timelineBadge: {
    color: 'dodgerblue',
    width: '100px',
    height: '100px',
    lineHeight: '24px',
    fontSize: '18px',
    textAlign: 'center',
    position: 'absolute',
    top: '18px',
    left: '50%',
    marginLeft: '-25px',
    backgroundColor: 'white',
    border: '3px solid dodgerblue',
    zIndex: '100',
    borderRadius: '50%',
  },
  lowerText: {
    textTransform: 'uppercase',
    color: 'grey',
    fontSize: '14px',
    fontWeight: '600',
    position: 'absolute',
    left: '2em',
    bottom: '-2em',
  },
  box: {
    width: '100%',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#iconColor',
    padding: '0px',
  },
};

export default SuggestionCard;
