import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Offcanvas from 'react-bootstrap/Offcanvas';
import './Navber.css';

function OffcanvasExample() {
  return (
    <>
    {/* false, 'sm', 'md', 'lg', 'xl', 'xxl' */}
      {['xxl'].map((expand) => (
        <Navbar key={expand} expand={expand} 
        // className="bg-body-tertiary mb-3" 
                className="bg-body-tertiary"
        >
          <Container fluid>
            <Navbar.Brand href="#" style={{ color : '#ffffff' }} >Assets Manager</Navbar.Brand>
            <Navbar.Toggle aria-controls={`offcanvasNavbar-expand-${expand}`} />
            <Navbar.Offcanvas
              id={`offcanvasNavbar-expand-${expand}`}
              aria-labelledby={`offcanvasNavbarLabel-expand-${expand}`}
              className="bg-body-tertiary"
              placement="end"
            >
              <Offcanvas.Header closeButton>
                <Offcanvas.Title id={`offcanvasNavbarLabel-expand-${expand}`}>
                  Offcanvas
                </Offcanvas.Title>
              </Offcanvas.Header>
              <Offcanvas.Body>
                <Nav className="justify-content-center flex-grow-1 pe-3">
                  <Nav.Link href="/" className="bg-body-menu">Home</Nav.Link>
                  <NavDropdown
                    title={<span className="navbar-text-white">My Data</span>} // 제목을 하얀색으로
                    href='/MyAssetsData'
                    id={`offcanvasNavbarDropdown-expand-${expand}`}
                    className="bg-body-menu"
                  >
                    <NavDropdown.Item href="#action2" className="bg-body-menu">
                      자산현황
                    </NavDropdown.Item>
                    <NavDropdown.Divider className="bg-body-menu"/>
                    <NavDropdown.Item href="#action3" className="bg-body-menu">
                      소비현황
                    </NavDropdown.Item>
                  </NavDropdown>
                  <Nav.Link href="/MyAssetsPlan" className="bg-body-menu">나의 계획</Nav.Link>
                  <Nav.Link href="/AssetsPortfolio" className="bg-body-menu">포트폴리오</Nav.Link>
                  <Nav.Link href="/AssetsFinance" className="bg-body-menu">금융</Nav.Link>
                  <Nav.Link href="/AssetsStock" className="bg-body-menu">주식</Nav.Link> 
                  <Nav.Link href="#action8" className="bg-body-menu">전체 메뉴</Nav.Link>
                </Nav>
                <Form className="d-flex">
                  <Form.Control
                    type="search"
                    placeholder="Search"
                    className="me-2"
                    aria-label="Search"
                  />
                  <Button variant="outline-success">Search</Button>
                </Form>
              </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
      ))}
    </>
  );
}

export default OffcanvasExample;