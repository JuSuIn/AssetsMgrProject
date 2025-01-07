from django.db import models

#Kospi 
#코스피 시리즈 지수의 시세정보를 제공(일별)에 대한 모델
# api : http://openapi.krx.co.kr/
class KospiDDInFor(models.Model):
    bas_dd = models.CharField(max_length=8) #기준일자
    inx_clss = models.CharField(max_length=100) #계열구분
    idx_nm = models.CharField(max_length=100)#지수명
    clsprc_idx = models.BigIntegerField()#종가
    cmpprevdd_idx = models.BigIntegerField()#대비
    fluc_rt = models.FloatField()#등락률
    opnprc_idx = models.BigIntegerField()#시가
    hgprc_idx = models.BigIntegerField()#고가
    lwprc_idx = models.BigIntegerField()#저가
    acc_trdvol = models.BigIntegerField()#거래량
    acc_trdval = models.BigIntegerField()#거래대금
    mktcap = models.BigIntegerField()#상장시가총액
    
    class Meta:
        db_table = 'kospi_dd_info'
    
    

#Koddaq 
#코스닥시장에 상장되어 있는 주권의 매매정보
# api : http://openapi.krx.co.kr/
class KosDaQDDInFor(models.Model):
        bas_dd = models.CharField(max_length=8) #기준일자
        isu_cd = models.CharField(max_length=100) #종목코드 
        isu_nm = models.CharField(max_length=100)#종목명
        mkt_nm = models.CharField(max_length=100)#시장구분
        sect_tp_nm = models.CharField(max_length=100)#소속부
        tdd_clsprc = models.BigIntegerField()#종가
        cmpprevdd_prc = models.BigIntegerField()#대비
        fluc_rt = models.FloatField()#등락률
        tdd_opnprc = models.BigIntegerField()#시가
        tdd_hgprc = models.BigIntegerField()#고가
        tdd_lwprc = models.BigIntegerField()#저가
        acc_trdvol = models.BigIntegerField()#거래량
        acc_trdval = models.BigIntegerField()#거래대금
        mktcap = models.BigIntegerField()#시가총액
        list_shrs = models.BigIntegerField()#상장주식수
        
        class Meta:
            db_table = 'kosdaq_dd_info'

# 석유시장 일별매매정보 ,
# KRX 석유시장의 매매정보 제공
# api : http://openapi.krx.co.kr/
class  OilByDDInfor(models.Model):
    bas_dd = models.CharField(max_length=8) #기준일자
    oil_nm = models.CharField(max_length=100) #유종구분
    wt_avg_prc = models.CharField(max_length=256)#가중평균가격_경쟁
    wt_dis_avg_prc = models.CharField(max_length=256)#가중평균가격_협의
    acc_trdvol= models.BigIntegerField()#거래량
    acc_trdval= models.BigIntegerField()#거래대금
    
    class Meta:
        db_table = 'oil_by_dd_info'

# 금시장 일별매매정보
# KRX 금시장 매매정보 제공
# api : http://openapi.krx.co.kr/
class GoldByDDInfor(models.Model):
    bas_dd = models.CharField(max_length=8) #기준일자
    lsu_cd = models.CharField(max_length=100) #종목코드
    lsu_nm = models.CharField(max_length=100) #종목명
    tdd_clsprc = models.BigIntegerField()#종가
    cmpprevdd_prc = models.BigIntegerField()#대비
    fluc_rt= models.CharField(max_length=100)#등락률
    tdd_opnprc = models.BigIntegerField()#시가
    tdd_hgprc = models.BigIntegerField()#고가
    tdd_lwprc = models.BigIntegerField()#저가
    acc_trdvol = models.BigIntegerField()#거래량
    acc_trdval= models.BigIntegerField()#거래대금
    
    class Meta:
        db_table = 'gold_by_dd_info'

# 환율 정보 
# api : https://fixer.io/
class ExChangeBsInfor(models.Model):
    bas_dd = models.CharField(max_length=8) #기준일자
    bas_ymdhms = models.CharField(max_length=14) #기준일시
    ex_Base = models.CharField(max_lengh=10) #환율명
    ex_Rates = models.FloatField()# 환율
    
    class Meta:
        db_table = 'exchangeBsInfo'
        
# 금리 정보 
# api : https://ecos.bok.or.kr/#/SearchStat 
class InterestRateInfor(models.Model):
    bas_dd = models.CharField(max_length=8) #기준일자
    bas_ymdhms = models.CharField(max_length=14) #기준일시
    ir_Base = models.CharField(max_lengh=10) #금리명
    ir_Rates = models.FloatField()# 금리
    
    class Meta:
        db_table = 'interestRateInfo'
    
   
        