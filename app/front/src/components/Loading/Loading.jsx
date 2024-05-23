import React from 'react';


const Loading = () => {
  /**
   * Component representing a loading indicator.
   * It overlays the screen with a semi-transparent black background and displays the message "Loading...".
   */
  return (
    <div className="loading-overlay">
      <div className="loading-content">
        <p>Loading...</p>
      </div>
    </div>
  );
}

export default Loading;