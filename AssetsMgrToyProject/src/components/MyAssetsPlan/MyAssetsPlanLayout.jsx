import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";

const MyAssetsPlanLayout = () => {
    return (
        <Container fluid>
            <Row style={{ display: "flex", height: "100vh" }}>
                <Col style={{ background: "grey",  height: "100%" }}>
                    MyAssetsPlanLayout Reactive Web Layout 
                </Col>
            </Row>
        </Container>     
    );
}

export default MyAssetsPlanLayout;