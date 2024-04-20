import React from 'react';

const ProfileCard = ({ name, age, occupation, bio, imageUrl }) => {
  return (
    <div className="profile-card">
      <img src={imageUrl} alt={name} className="profile-img" />
      <div className="profile-info">
        <h2>{name}</h2>
        <p>Age: {age}</p>
        <p>Occupation: {occupation}</p>
        <p>Bio: {bio}</p>
      </div>
    </div>
  );
};

const routeCard = () => {
  return (
    <div>
      <ProfileCard
        name="John Doe"
        age={30}
        occupation="Software Engineer"
        bio="Passionate about coding and technology."
        imageUrl="https://example.com/john-doe.jpg"
      />
    </div>
  );
};

// CSS styles
// const styles = {
//   .profile-card {
//     width: 300px;
//     border: 1px solid #ccc;
//     border-radius: 5px;
//     padding: 20px;
//     margin: 20px;
//     box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
//   }

//   .profile-img {
//     width: 100%;
//     border-radius: 5px;
//     margin-bottom: 10px;
//   }

//   .profile-info h2 {
//     margin-top: 0;
//   }

//   .profile-info p {
//     margin: 5px 0;
//   }
// };

// const styleElement = document.createElement('style');
// styleElement.innerHTML = styles;
// document.head.appendChild(styleElement);

// export default App;
