import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download

import { useNavigate } from 'react-router-dom';

import { Container,Row,Col } from "react-bootstrap";
import HomeIconMyDataImg from "./HomeImage/homeiconMyDataimg.png";
import HomeIconMyPlanImg from "./HomeImage/homeiconMyPlanimg.png";
import HomeIconFinanceImg from "./HomeImage/homeiconFinanceimg.png";
import HomeIconPortfolioImg from "./HomeImage/homeiconPortfolioimg.png";
import HomeIconStockImg from "./HomeImage/homeiconStockimg.png";
import './HomeLo3Icon.css';


const HomeLo3Icon = () => {

    const navigate = useNavigate();
    const handlePageIconChlick = (handlerIconItem) => {
        //console.log(`Slide ${handlerIconItem} clicked!`);
        switch(handlerIconItem){
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
        <Container fluid style={{ display: "grid" ,gap : "10px", marginTop: "8px", padding: "5px" }} >
            <p>주요 메뉴</p>
            <Row style={{ height: "130px" }} >  
                <Col style={{ background : "#4a4a4a" , cursor : 'pointer' }} 
                     onClick={ () => handlePageIconChlick('myData') } >
                    <img src={ HomeIconMyDataImg } className='img-small'/>
                </Col>
                <Col style={{ background : "#4a4a4a", cursor : 'pointer' }}
                     onClick={ () => handlePageIconChlick('myPlan') } >
                    <img src={ HomeIconMyPlanImg } className='img-small'/>
                </Col>
                <Col style={{ background : "#4a4a4a", cursor : 'pointer' }}
                     onClick={ () => handlePageIconChlick('portfolio') } >
                    <img src={ HomeIconFinanceImg } className='img-small'/>
                </Col>
                <Col style={{ background : "#4a4a4a", cursor : 'pointer' }}
                     onClick={ () => handlePageIconChlick('finance') } >
                    <img src={ HomeIconPortfolioImg } className='img-small'/>
                </Col>
                <Col style={{ background : "#4a4a4a", cursor : 'pointer' }}
                     onClick={ () => handlePageIconChlick('stock') } >
                    <img src={ HomeIconStockImg } className='img-small'/>
                </Col>                                                               
            </Row>
        </Container>

    );
}

export default HomeLo3Icon;