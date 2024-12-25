import './HomeLy5FooterList.css';

const HomeLy5FooterList = () => {
    return (
       <footer className='footer-container'>
            <div className='footer-column'>
                <h3>새소식</h3>
                <a href='#news' className='more-link'>바로가기 &gt;</a>
                <ul className ="footer-list">
                    <li>
                        <span>세 번째 소식입니다.</span>
                        <span className="footer-date">10.01</span>
                    </li>
                    <li>
                        <span>두 번째 소식입니다.</span>
                        <span className="footer-date">10.04</span>
                    </li>
                    <li>
                        <span>첫 번째 소식입니다.</span>
                        <span className="footer-date">10.10</span>
                    </li>

                </ul>
            </div>
            <div className='footer-column'>
                <h3>자산관리 관련 테스트</h3>
                <a href='#news' className='more-link'>바로가기2&gt;</a>
                <ul className ="footer-list">
                    <li>
                        <span>나의 데이터</span>
                        <span className="footer-date">10.01</span>
                    </li>
                    <li>
                        <span>나의 계획</span>
                        <span className="footer-date">10.04</span>
                    </li>  
                     <li>
                        <span>포트폴리오</span>
                        <span className="footer-date">10.10</span>
                    </li>

                </ul>
            </div>
       </footer>
    );
}

export default HomeLy5FooterList;