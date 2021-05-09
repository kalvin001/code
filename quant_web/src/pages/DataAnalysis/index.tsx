import React, { useEffect, useState } from 'react';
import { ResponsiveGrid } from '@alifd/next';
import { Table ,Pagination, Box, Loading,Tab} from '@alifd/next';

import styles from '@/components/index.module.scss';

const { Cell } = ResponsiveGrid;

const StockBasic = (props,context) => {
  
  const [result,setResult] = useState([])
  const [total,setTotal] = useState()

  const [loading,setLoading] = useState(true)
  const [page,setPage] = useState(1)
  
  useEffect(()=>{
    setLoading(true)
    let url = `/quant/query_table?table_name=quant_stockbasic&size=10&page=${page}`
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
    <Tab className={styles.TabContainer}> 
    <Tab.Item title="选股" key="1">

    <ResponsiveGrid gap={20}>
      <Cell colSpan={12} style={{backgroundColor:"#fff",padding:"10px 10px 10px 10px"}}>
      <Loading tip="加载中..." visible={loading} fullScreen="true">
        <Table dataSource={result}>
          <Table.Column title="代码" cell={(value,rowIdx,record) =><a href={["http://localhost:3333/#/analysis/stock_detail?code=" + record.code]}  target="_blank">{record.code}</a>}/>
          <Table.Column title="名称" dataIndex="name"/>
          <Table.Column title="市场" dataIndex="market"/>
          <Table.Column title="所属行业" dataIndex="industry"/>
          <Table.Column title="上市时间" dataIndex="list_date"/>
          <Table.Column title="深沪通" dataIndex="is_hs"/>


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

    <Tab.Item title="热力图" key="2">
      热力图
    </Tab.Item>
    </Tab>
  );
};

export default StockBasic;
