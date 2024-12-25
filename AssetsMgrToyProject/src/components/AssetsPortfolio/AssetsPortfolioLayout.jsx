import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import AssetsPortfolioLayoutMenu from './AssetsPortfolioLayoutMenu';
import AssetsPortfolioLayoutRight from './AssetsPortfolioLayoutRight';

const AssetsPortfolioLayout = () => {
    return (
        <Container fluid>
        <Row style={{ display: "flex", height: "100vh" }}>
          {/* 왼쪽 열: 비율 1.5 */}
          <Col style={{ background: "lightgrey", flex: 1.5, height: "100%" }}>
            <AssetsPortfolioLayoutMenu/>
          </Col>
  
          {/* 오른쪽 열: 비율 9 */}
          <Col style={{ background: "grey", flex: 9, height: "100%" }}>
            <AssetsPortfolioLayoutRight/>
          </Col>
        </Row>
      </Container>
      );   
};

export default AssetsPortfolioLayout;