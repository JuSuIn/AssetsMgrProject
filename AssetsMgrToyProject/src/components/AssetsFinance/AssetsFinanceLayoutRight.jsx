import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";

const AssetsFinanceLayoutRight = () => {
    return (
        <Container fluid style={{ gap: "10px", display: "grid" ,height: '100vh'}}>
            <Row style={{ height: '20vh' }}>
                 <Col xs={6} md={6} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 1-1
                </Col>
                <Col xs={6} md={6} style={{ backgroundColor: 'grey',  height: '100%' }}>
                    Layout 1-2
                </Col>
            </Row>
            <Row style={{ height: '40vh' }}>
                 <Col xs={6} md={6} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 2-1
                </Col>
                <Col xs={6} md={6} style={{ backgroundColor: 'grey',  height: '100%' }}>
                    Layout 2-2
                </Col>
            </Row>
            <Row style={{ height: '20vh' }}>
                 <Col xs={6} md={6} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 3-1
                </Col>
                <Col xs={6} md={6} style={{ backgroundColor: 'grey',  height: '100%' }}>
                    Layout 3-2
                </Col>
            </Row>
            <Row style={{ height: '20vh' }}>
                 <Col xs={6} md={6} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 4-1
                </Col>
                <Col xs={6} md={6} style={{ backgroundColor: 'grey',  height: '100%' }}>
                    Layout 4-2
                </Col>
            </Row>
            <Row style={{ height: '35vh' }}>
                <Col xs={12} md={12} style={{ backgroundColor: 'grey', height: '100%' }}>
                    Layout 5 
                </Col>
            </Row>
        </Container>
    );

}

export default AssetsFinanceLayoutRight;