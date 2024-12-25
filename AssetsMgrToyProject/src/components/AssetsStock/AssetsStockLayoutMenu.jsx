import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Navbar, Nav,NavDropdown, Container } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMagnifyingGlassDollar,faClipboard,faFileInvoiceDollar,
         faMoneyCheckDollar,faMoneyBillTrendUp,
         faArrowTrendUp,faOilWell,faChartLine } from '@fortawesome/free-solid-svg-icons'
import './AssetsStockLayoutMenu.css'

const AssetsStockLayoutMenu = () => {

    return (
        <Navbar expand="lg" className="main-head-tertiary">
            <Container fluid style={{ gap: "10px", display: "grid" ,height: '20vh' }}>
                <Nav className="flex-column">
                    <Navbar.Brand href="/AssetsStock" className="main-head-tertiary-brand">
                        Stock
                    </Navbar.Brand>
                    <Nav.Link href="/AssetsStock/StockTop" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faMagnifyingGlassDollar} />
                        최근조회종목
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/PointNews" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faClipboard} />
                        주요뉴스
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/TodayStockPic" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faArrowTrendUp} />
                        오늘의증시
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/StockForeignPic" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faArrowTrendUp} />
                        해외증시
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/TopStockPic" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faFileInvoiceDollar} />
                        top종목
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/Exchange" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faMoneyCheckDollar} />
                        환율
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/InterestRate" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faMoneyBillTrendUp}  />
                        금리
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/OilPrice" className='main-head-tertiary-menu'>
                    <FontAwesomeIcon icon={faOilWell} />
                        유가
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/GoldQuotations" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faChartLine} />
                        금시세
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock/SilverQuotations" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faChartLine} />
                        은시세
                    </Nav.Link>
                    <Nav.Link href="/AssetsStock//RawMaterials" className='main-head-tertiary-menu'>
                        <FontAwesomeIcon icon={faChartLine} />
                        원자재
                    </Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );

}

export default AssetsStockLayoutMenu;