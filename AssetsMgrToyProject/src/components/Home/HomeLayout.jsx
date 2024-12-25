import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import HomeCpBannerSlider from './HomeCpBannerSlider';
import HomeTwoSpeedButton from './HomeTwoSpeedButton';
import HomeLo3Icon from './HomeLo3Icon';
import HomeLo3CardGpList from './HomeLo3CardGpList';
import HomeLy5FooterList from './HomeLy5FooterList';

const HomeLayout = () => {
    return (
        <Container fluid style={{ gap: "30px", display: "grid" }}>
            <Row>  
                <Col style={{ background : "#FCFCFC", height : "480px" }}>
                    <HomeCpBannerSlider />
                </Col>
            </Row>
            <Row> 
                <Col style={{ background : "grey", height : "100px" }}>
                    <HomeTwoSpeedButton />
                </Col>
            </Row>
            <Row>
                <Col style={{ background : "grey", height : "200px" }}>
                    <HomeLo3Icon />
                </Col>
            </Row>
            <Row>
                <Col style={{ background : "grey", height : "500px" }}>
                    <HomeLo3CardGpList />
                </Col>
            </Row>
            <Row>
                <Col style={{ background : "grey", height : "300px" }}>
                    <HomeLy5FooterList />
                </Col>
           </Row>
        </Container>
    );

};

export default HomeLayout;

