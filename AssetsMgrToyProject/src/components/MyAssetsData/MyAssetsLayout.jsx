import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";

const MyAssetsLayout = () => {
    return (
        <Container fluid>
        <Row style={{ display: "flex", height: "100vh" }}>
          {/* 왼쪽 열: 비율 1.5 */}
          <Col style={{ background: "lightgrey", flex: 1.5, height: "100%" }}>
            MyAssetsDataMain Layout 1
          </Col>
  
          {/* 오른쪽 열: 비율 9 */}
          <Col style={{ background: "grey", flex: 9, height: "100%" }}>
            MyAssetsDataMain Layout 2
          </Col>
        </Row>
      </Container>
      );
};

export default MyAssetsLayout;