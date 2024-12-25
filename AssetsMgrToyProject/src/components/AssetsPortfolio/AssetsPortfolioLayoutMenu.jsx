import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Navbar, Nav,NavDropdown, Container } from 'react-bootstrap';
import './AssetsPortfolioLayoutMenu.css'

const AssetsPortfolioLayoutMenu = () => {
    return (
        <Navbar expand="lg" className="main-head-tertiary">
            <Container fluid style={{ gap: "10px", display: "grid" ,height: '20vh'}}>
                <Nav className="flex-column">
                    <Navbar.Brand href="#home" className="main-head-tertiary-brand">
                        Portfolio
                    </Navbar.Brand>
                    <Nav.Link href="#home">펀드포트폴리오</Nav.Link>
                    <Nav.Link href="#features">퇴직연금포트폴리오</Nav.Link>
                    <Nav.Link href="#pricing">미래설계</Nav.Link>
                    <Nav.Link href="#pricing">자산운용현황</Nav.Link>
                    <Nav.Link href="#pricing">투자전략</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );

}

export default AssetsPortfolioLayoutMenu;