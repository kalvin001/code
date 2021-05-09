import React, { useEffect, useState } from 'react';
import { ResponsiveGrid } from '@alifd/next';
import { Table ,Pagination, Box, Loading, Tab} from '@alifd/next';


import styles from '@/components/index.module.scss';
import KLine from '@/components/Charts/k_line'
import BasicLine from '@/components/Charts/basic_line'

const { Cell } = ResponsiveGrid;

const StockDetail = (props,context) => {
  const [result,setResult] = useState([])
  const [total,setTotal] = useState()
  const [code,setCode] = useState(props.searchParams.code?props.searchParams.code:"000001.SZ")

  const [loading,setLoading] = useState(true)
  const [page,setPage] = useState(1)
  
  useEffect(()=>{
    setLoading(true)
    let url = `quant/query_table?table_name=stock_trade_daily&where=ts_code=%27${code}%27&size=20&page=${page}`
    fetch(url).then(res=>res.json()).then(data=>{
      setResult(data.data)
      setTotal(data.total)
      setLoading(false)

    })

  },[page])

  const onPageChange = (currentPage) => {
    setPage(currentPage)
  }

  return (

    
<>
   <Tab className={styles.TabContainer}> 
    <Tab.Item title="图表展示" key="1">

    <ResponsiveGrid gap={20}>
      <Cell colSpan={12} style={{backgroundColor:"#fff",padding:"10px 10px 10px 10px"}}>
         <KLine></KLine>
        {/* <BasicLine></BasicLine> */}
      </Cell>
  </ResponsiveGrid>
    </Tab.Item>
    <Tab.Item title="明细数据" key="2">
    <ResponsiveGrid gap={20}>
      <Cell colSpan={12} style={{backgroundColor:"#fff",padding:"10px 10px 10px 10px"}}>
      <Loading tip="加载中..." visible={loading} fullScreen="true">
        <Table dataSource={result}>
          <Table.Column title="交易日期" dataIndex="trade_date"/>
          <Table.Column title="代码" dataIndex="ts_code"/>
          <Table.Column title="开盘价" dataIndex="open"/>
          <Table.Column title="收盘价" dataIndex="close"/>
          <Table.Column title="最高价" dataIndex="high"/>
          <Table.Column title="最低价" dataIndex="low"/>
          <Table.Column title="前交易日收盘价" dataIndex="pre_close"/>
          <Table.Column title="变动" dataIndex="pct_chg"/>
          <Table.Column title="交易量" dataIndex="vol"/>
          <Table.Column title="交易金额" dataIndex="amount"/>


      </Table>
      </Loading>
     <Box margin={[15, 0, 0, 0]} direction="row" align="center" justify="space-between">
              <div className={styles.total}>
                共<span>{total}</span>条
              </div>
              <Pagination onChange={onPageChange} total={total} />
      </Box>
      </Cell>
   
  </ResponsiveGrid>

    </Tab.Item>
  </Tab>
</>
  );
};

export default StockDetail;
