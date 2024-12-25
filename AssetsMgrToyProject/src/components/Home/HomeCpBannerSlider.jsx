// import Slider from "react-slick";
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";
import AwesomeSlider from "react-awesome-slider";
import 'react-awesome-slider/dist/styles.css';

import { useNavigate } from 'react-router-dom';

import HomeLayoutoneMyDataimg from "./HomeImage/homeLayoutoneMyDataimg.jpg";
import HomeLayoutoneMyPlanimg from "./HomeImage/homeLayoutoneMyPlanimg.jpg";
import HomeLayoutonePortfolioimg from "./HomeImage/homeLayoutonePortfolioimg.jpg";
import HomeLayoutoneFinanceimg from "./HomeImage/homeLayoutoneFinanceimg.jpg";
import HomeLayoutoneStockimg from "./HomeImage/homeLayoutoneStockimg.jpg";

const HomeCpBannerSlider = () => {

    const navigate = useNavigate();
    const handlePageChangeClick = (handlerItem) => {
       
        //console.log(`Slide ${handlerItem} clicked!`);
        switch (handlerItem){
            case 'myData':
                 navigate('/MyAssetsData'); break;
            case 'myPlan':
                navigate('/MyAssetsPlan'); break;
            case 'portfolio':
                navigate('/AssetsPortfolio'); break;
            case 'finance':
                navigate('/AssetsFinance'); break;
            case 'stock':
                navigate('/AssetsStock'); break;
            default:
                 navigate('/NotFound'); break;
        }
    };

        return (
        <AwesomeSlider style={{ width : "100%", height : "420px" }} >
            <div data-src={ HomeLayoutoneMyDataimg }
                onClick={ () => handlePageChangeClick('myData') }
            />
            <div data-src={ HomeLayoutoneMyPlanimg }
               onClick={ () => handlePageChangeClick('myPlan') }
            />
            <div data-src={ HomeLayoutonePortfolioimg }
                onClick={ () => handlePageChangeClick('portfolio') }
            />
            <div data-src={ HomeLayoutoneFinanceimg }
                onClick={ () => handlePageChangeClick('finance') }
            />
            <div data-src={ HomeLayoutoneStockimg }
                onClick={ () => handlePageChangeClick('stock') }
            />
        </AwesomeSlider>
        );
};

export default HomeCpBannerSlider;