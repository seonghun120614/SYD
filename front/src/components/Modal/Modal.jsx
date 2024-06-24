import React from 'react';

import "./Modal.css";

const Modal = ({ isOpen, onClose, text }) => {
  if (!isOpen) return null;

  return (
    <div className="custom-modal-overlay" onClick={onClose}>
      <div className="custom-modal-content" onClick={(e) => e.stopPropagation()}>
        <h1>{text}</h1>
      </div>
    </div>
  );
};

export default Modal;