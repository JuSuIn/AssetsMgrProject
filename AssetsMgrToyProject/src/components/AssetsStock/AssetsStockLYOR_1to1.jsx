import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import "./AssetsStockLYOR_1to1.css";
import { Carousel } from 'react-bootstrap';




const AssetsStockLYOR_1to1 = () => {
    return (
        <Carousel data-bs-theme="dark">
        <Carousel.Item interval={1000}>
            Test1
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item interval={1000}>
             Test2
            <Carousel.Caption>
                <h3>Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </Carousel.Caption>
        </Carousel.Item>   
        <Carousel.Item interval={1000}>
            Test3
            <Carousel.Caption>
                <h3>Third slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
            </Carousel.Caption>
        </Carousel.Item>  
        <Carousel.Item interval={1000}>
            Test4
            <Carousel.Caption>
                <h3>Fourth slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
            </Carousel.Caption>
        </Carousel.Item>                
        </Carousel>
    );
}

export default AssetsStockLYOR_1to1;