
// export default App
import './App.css'
import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css'; //bootstrap download
import Navbar from './components/Navber';
import { Container } from "react-bootstrap";
import { Routes,Route } from 'react-router-dom';

import Home from './components/Home/Home';
import MyAssetsDataMain from './components/MyAssetsData/MyAssetsDataMain';
import AssetsPortfolioMain from './components/AssetsPortfolio/AssetsPortfolioMain';
import MyAssetsPlanMain from './components/MyAssetsPlan/MyAssetsPlanMain';
import AssetsFinanceMain from './components/AssetsFinance/AssetsFinanceMain';
import AssetsStockMain from './components/AssetsStock/AssetsStockMain';
import NotFound from './NotFound';

function App() {
  return (
    <div style={{ height: "100vh", overflow: "hidden" }}>
      {/* 상단에 고정된 네비게이션 바 */}
      <Navbar sticky="top" className="m-0 p-0"/>
      {/* 고정된 Navbar 아래의 변동 가능한 콘텐츠 */}
      <div
        style={{
          marginTop: "0px", // Navbar 높이(기본적으로 56px) 만큼 여백 주기
          height: "calc(100vh - 0px)", // Navbar 아래에서 남은 영역을 차지하도록 설정
          overflowY: "auto", // 스크롤 가능하도록 설정
        }}
      >
        <Container fluid className="py-0 gx-0">
          <div style={{ height: "2000px" }}>
            {/* 더미 콘텐츠로 긴 페이지를 생성 */}
            {/* page설정 */}
             <Routes>
                <Route path="/" element={ <Home /> } />
                <Route path="/MyAssetsData" element={ <MyAssetsDataMain /> } />
                <Route path="/MyAssetsPlan" element={ <MyAssetsPlanMain /> } />
                <Route path="/AssetsPortfolio" element={ <AssetsPortfolioMain /> } />
                <Route path="/AssetsFinance" element={ <AssetsFinanceMain /> } />
                <Route path="/AssetsStock" element={ <AssetsStockMain /> } />
                <Route path="*" element={ <NotFound /> } />
             </Routes>
          </div>
        </Container>
      </div>
    </div>
  );
}

export default App;
