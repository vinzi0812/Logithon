import React from 'react';

const RnD = () => {
  const container = styles.container; // Assign styles.container to a variable for easier usage
  return (
    <div style={container}>
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
    backgroundColor: '#000000',
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

export default RnD;
