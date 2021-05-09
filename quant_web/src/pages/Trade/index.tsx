import React, { useEffect, useState } from 'react';
import { Link } from 'ice';
import { ResponsiveGrid , Tab , Table, Button} from '@alifd/next';
import PageHeader from '@/components/PageHeader';
import styles from '@/components/index.module.scss';

const { Cell } = ResponsiveGrid;

const DataManager = () => {

  const dataSource = [{name: "quant_stockbasic", desc:"股票基础信息表", gmt_modified: '2016-11-2',gmt_created:"2016-11-2",}];

   
  const [result,setResult] = useState([])
  useEffect(()=>{
    let url = `/quant/meta_tables`
    fetch(url).then(res=>res.json()).then(data=>{
      setResult(data)
    })

  },[])


  return (
    <>
   <Tab className={styles.TabContainer}> 
    <Tab.Item title="富途数据" key="1">

    富途数据
    </Tab.Item>
    <Tab.Item title="同花顺" key="2">


    </Tab.Item>
  </Tab>
</>
  );
};

export default DataManager;
