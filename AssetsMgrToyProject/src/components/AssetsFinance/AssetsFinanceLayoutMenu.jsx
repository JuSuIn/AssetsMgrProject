import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Navbar, Nav,NavDropdown, Container } from 'react-bootstrap';
import './AssetsFinanceLayoutMenu.css'

const AssetsFinanceLayoutMenu = () => {
    return (
        <Navbar expand="lg" className="main-head-tertiary">
            <Container fluid style={{ gap: "10px", display: "grid" ,height: '20vh'}}>
                <Nav className="flex-column">
                    <Navbar.Brand href="#home" className="main-head-tertiary-brand">
                        Finance
                    </Navbar.Brand>
                    <Nav.Link href="#home">골드</Nav.Link>
                    <Nav.Link href="#features">대출</Nav.Link>
                    <Nav.Link href="#pricing">예금</Nav.Link>
                    <Nav.Link href="#pricing">ISA</Nav.Link>
                    <Nav.Link href="#pricing">보험</Nav.Link>
                    <Nav.Link href="#pricing">외환</Nav.Link>
                    <Nav.Link href="#pricing">펀드</Nav.Link>
                    <Nav.Link href="#pricing">퇴직연금</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );
}

export default AssetsFinanceLayoutMenu;