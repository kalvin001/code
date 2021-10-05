import React, { useEffect, useState } from 'react';
import { Link } from 'ice';
import { ResponsiveGrid , Tab , Table, Button} from '@alifd/next';
import PageHeader from '@/components/PageHeader';
import styles from '@/components/index.module.scss';

const { Cell } = ResponsiveGrid;

const FutuTrade = () => {

  const dataSource = [{name: "quant_stockbasic", desc:"股票基础信息表", gmt_modified: '2016-11-2',gmt_created:"2016-11-2",}];

   
  const [result,setResult] = useState({})
  useEffect(()=>{
    let url = `/quant/futu_info`
    fetch(url).then(res=>res.json()).then(data=>{
      setResult(data.power)
    })

  },[])


  return (
    <>
   <Tab className={styles.TabContainer}> 
    <Tab.Item title="资金数据" key="1">

    资金数据 :{result[0]}
    </Tab.Item>
    <Tab.Item title="同花顺" key="2">


    </Tab.Item>
  </Tab>
</>
  );
};

export default FutuTrade;
