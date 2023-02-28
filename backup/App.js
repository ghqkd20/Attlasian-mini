import React from 'react';
import { useState, useEffect } from "react";
import { getManageApplication } from './api';
import './App.css';
import ManageTable from './ManageTable';
import Header from './header';
import Update_button from './Update_button';
import Period from './period';

function App() {

  return (
    <div style={{display: 'inline-block'}}>
      <div style={{display:'flex'}}>
        <Header/>
        <div>
          <Update_button/>
          <Period/>
        </div>
      </div>
      <ManageTable />
    </div>
  
  );
}

export default App;