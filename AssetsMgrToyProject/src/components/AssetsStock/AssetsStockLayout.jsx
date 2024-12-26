import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import AssetsStockLayoutMenu from './AssetsStockLayoutMenu';
import AssetsStockLayoutRight from './AssetsStockLayoutRight';

const AssetsStockLayout = () => {
    return (
        <Container fluid style={{ height: '500vh' }}>
            <Row className="h-100">
            {/* Left Fixed Menu */}
            <Col xs={12} md={3} lg={2} style={{ backgroundColor : '#191818', height: '100%', padding: '20px' }}>
                <AssetsStockLayoutMenu />
            </Col>
            {/* Right Responsive Layout */}
            <Col xs={12} md={7} lg={10} style={{ backgroundColor : '#191818',height: '100%', padding: '20px' }}>
                <AssetsStockLayoutRight />
            </Col>
            </Row> 
      </Container>
    );
}

export default AssetsStockLayout;