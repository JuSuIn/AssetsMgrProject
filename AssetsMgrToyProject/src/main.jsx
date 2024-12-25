import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter } from 'react-router-dom';

createRoot(document.getElementById('root')).render(
   <BrowserRouter>{/* 현재주소를 저장하고 감지 */}
        <App />
   </BrowserRouter>
   
);