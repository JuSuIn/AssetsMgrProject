import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import { Container,Row,Col } from "react-bootstrap";
import AssetsStockLYOR_1to1 from './AssetsStockLYOR_1to1';

const AssetsStockLayoutRight = () => {
    return (
        <Container fluid style={{ gap: "10px", display: "grid" ,height: '100vh'}}>
            <Row className='layout-row'> 
                <Col xs={12} md={12} style={{ backgroundColor: 'grey', height: '8vh', padding: '8px' }}>
                    <AssetsStockLYOR_1to1 />
                </Col>
            </Row>
            <Row>
                <Col xs={4} md={4} style={{ backgroundColor: 'grey', height: '40vh' }}>
                    top 종목 Layout 2-1
                </Col>
                <Col xs={4} md={8} style={{ backgroundColor: 'grey', height: '40vh' }}>
                    오늘의 증시 Layout 2-2
                </Col>
            </Row>
            <Row style={{ height: '40vh' }}>
                <Col xs={4} md={4} style={{ backgroundColor: 'grey', height: '100%' }}>
                    주요 뉴스 Layout 3-1
                </Col>
                <Col xs={8} md={8} style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>{/* 오른쪽 열을 Flexbox로 설정 */}
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                       해외증시 Layout 3-2
                    </div>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                       해외 증시 현황(차트) Layout 3-3
                    </div>
                </Col>
            </Row>    
            <Row style={{ height: '40vh' }}>
                <Col xs={3} md={3} style={{ display: 'flex', flexDirection: 'column', backgroundColor: 'grey', height: '100%' }}>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                        환율(금액표기) Layout 4-1
                    </div>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                        환율(국제시장금액표기)Layout 4-4
                    </div>
                </Col>
                <Col xs={3} md={3} style={{ display: 'flex', flexDirection: 'column', backgroundColor: 'grey', height: '100%' }}>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                        금리 Layout 4-2
                    </div>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                        금시세 Layout 4-5
                    </div>
                </Col>
                <Col xs={3} md={3} style={{ display: 'flex', flexDirection: 'column', backgroundColor: 'grey', height: '100%' }}>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                       유가 Layout 4-3
                    </div>
                    <div style ={{ backgroundColor : 'grey' , flex : 1}}>
                       은시세 Layout 4-6
                    </div>   
                </Col>
                <Col xs={3} md={3} style={{ backgroundColor: 'grey', height: '100%' }}>
                    원자재 Layout 4-7
                </Col>
            </Row>               
        </Container>
    );
}

export default AssetsStockLayoutRight;