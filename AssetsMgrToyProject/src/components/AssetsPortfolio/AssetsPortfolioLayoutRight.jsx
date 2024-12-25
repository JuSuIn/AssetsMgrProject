//import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import './AssetsPortfolioLayoutRight.css';

const AssetsPortfolioLayoutRight = () => {
    return (
        <Container fluid style={{ rowGap: "10px", display: "grid" ,height: '100vh'}}>
            <Row style={{ height: '20vh' }}>
                 <Col xs={6} md={6} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 1-1
                </Col>
                <Col xs={6} md={6} style={{ backgroundColor: 'grey',  height: '100%' }}>
                    Layout 1-2
                </Col>
            </Row>
            <Row tyle={{ height: '25vh'}}>
                 <Col xs={12} md={12} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 2
                </Col>
            </Row>
            <Row tyle={{ height: '25vh'}}>
                 <Col xs={12} md={12} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 3
                </Col>
            </Row>    
            <Row tyle={{ height: '25vh'}}>
                 <Col xs={12} md={12} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 4
                </Col>
            </Row>                      
        </Container>
    );
}

export default AssetsPortfolioLayoutRight;