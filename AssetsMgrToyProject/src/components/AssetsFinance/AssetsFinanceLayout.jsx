import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import AssetsFinanceLayoutMenu from './AssetsFinanceLayoutMenu';
import AssetsFinanceLayoutRight from './AssetsFinanceLayoutRight';

//AssetsFinanceLayout Reactive Web Layout
const AssetsFinanceLayout = () => {
    return (
        <Container fluid style={{ height: '150vh' }}>
            <Row className="h-100">
            {/* Left Fixed Menu */}
            <Col xs={12} md={3} lg={2} style={{ backgroundColor: 'grey', height: '100%', padding: '20px' }}>
               <AssetsFinanceLayoutMenu/>
            </Col>
            {/* Right Responsive Layout */}
            <Col xs={12} md={7} lg={10} style={{ backgroundColor: 'lightgrey', padding: '20px' }}>
               <AssetsFinanceLayoutRight/>
            </Col>
            </Row>
      </Container>
    );
}

export default AssetsFinanceLayout;