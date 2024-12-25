import React from "react";

import { useNavigate } from 'react-router-dom';

import { Button, ButtonGroup, Container } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import './HomeTwoSpeedButton.css';

const HomeTwoSpeedButton = () => {
  
  const navigate = useNavigate();
  const handlePageSpChlick = (handlerSpItem) => {
        switch(handlerSpItem){
          case 'myData':
              navigate('/MyAssetsData'); break;
          case 'portfolio':
              navigate('/AssetsPortfolio'); break;
          case 'stock':
              navigate('/AssetsStock'); break;
          default:
              navigate('/NotFound'); break;
      }   
  }

    return (
      <Container className = "d-flex justify-content-center mt-3">
        <ButtonGroup className ="rounded-buttons" >
            <Button 
                    variant="primary"
                    onClick={ () => handlePageSpChlick('myData') }
                    className="left-rounded custom-button">나의자산현황</Button>
            <Button 
                    variant="info"
                    onClick={ () => handlePageSpChlick('portfolio') }
                    className="custom-button">포트폴리오</Button>
            <Button 
                    variant="info" 
                    onClick={ () => handlePageSpChlick('/')  }
                    className="custom-button">환율</Button>
            <Button 
                    variant="info" 
                    onClick={ () => handlePageSpChlick('stock') }
                    className="custom-button">주식</Button>
            <Button 
                    variant="light"
                    onClick={ () => handlePageSpChlick('*') }
                    className="right-rounded custom-button">빠른메뉴 &gt;</Button>
        </ButtonGroup>
      </Container>  
    );

}

export default HomeTwoSpeedButton;