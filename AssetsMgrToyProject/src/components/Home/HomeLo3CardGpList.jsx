import React from 'react';
import { Card, CardGroup } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

import './HomeLo3CardGpList.css';


const HomeLo3CardGpList = () => {

    const navigate = useNavigate();
    const handlePageCardClick = (handlerItem) => {
       
        //console.log(`Slide ${handlerItem} clicked!`);
        switch (handlerItem){
            case 'myData':
                 navigate('/MyAssetsData'); break;
            case 'myPlan':
                navigate('/MyAssetsPlan'); break;
            case 'portfolio':
                navigate('/AssetsPortfolio'); break;
            case 'finance':
                navigate('/AssetsFinance'); break;
            case 'stock':
                navigate('/AssetsStock'); break;
            default:
                 navigate('/NotFound'); break;
        }
    };
    return (
    <div>
      <h4>Test</h4>
      <CardGroup>
        <Card className='custom-card'> 
            <Card.Img variant='top' 
                    src="holder.js/100px160" 
                    onClick={ () => handlePageCardClick('myData') }
                    className='custom-card-img' />
            <Card.Body>
                <Card.Title>My Data</Card.Title>
                <Card.Text>
                    자산관리 프로젝트중 나의 데이터 입니다.
                </Card.Text>
            </Card.Body>
            <Card.Footer>
                <small className="text-muted">test1</small>
            </Card.Footer>
        </Card>
        <Card className='custom-card'>
            <Card.Img variant='top' 
                        src="holder.js/100px160" 
                        onClick={ () => handlePageCardClick('portfolio') } 
                        className='custom-card-img' />
            <Card.Body>
                <Card.Title>Portfolio</Card.Title>
                <Card.Text>
                    자산관리 프로젝트에서 구성된 포트폴리오를 확인할 수 있습니다.{' '}
                </Card.Text>
            </Card.Body>
            <Card.Footer>
                <small className="text-muted">test2</small>
            </Card.Footer>
        </Card>   
        <Card className='custom-card'>
            <Card.Img variant='top' 
                        src="holder.js/100px160" 
                        onClick={ () => handlePageCardClick('finance') } 
                        className='custom-card-img' />
            <Card.Body>
                <Card.Title>Finance</Card.Title>
                <Card.Text>
                    자산관리 프로젝트에서 구성된 금융관련 자료를 확인 하실 수 있습니다.{' '}
                </Card.Text>
            </Card.Body>
            <Card.Footer>
                <small className="text-muted">test3</small>
            </Card.Footer>
        </Card>                
      </CardGroup>
      </div>
    );
}

export default HomeLo3CardGpList;
