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
    <ResponsiveGrid gap={0}>
    <Cell colSpan={12}>
      <PageHeader
        breadcrumbs={[{ name: '数据管理' }, { name: '表管理' }]}
      />
    </Cell>

    <Cell colSpan={12} style={{padding:"10px"}}>
    <Table dataSource={result}>
        <Table.Column title="表名称" dataIndex="Name"/>
        <Table.Column title="表描述" dataIndex="Comment"/>
        <Table.Column title="数据行数" dataIndex="Rows"/>
        <Table.Column title="创建时间" dataIndex="Create_time"/>
        <Table.Column title="更新时间" dataIndex="Update_time"/>
        <Table.Column title="查看详情"  cell={(value,rowIdx,record) =><a href={["http://localhost:3333/#/data/" + record.Name]}  target="_blank">详情</a>}/>
        <Table.Column title="操作"  cell={<Button type="secondary">更新</Button>}/>
    </Table>

    </Cell>
  </ResponsiveGrid>
    {/* <Tab className={styles.TopHeader}>
    <Tab.Item title="表管理" key="1"></Tab.Item>
    <Tab.Item title="任务管理" key="2"></Tab.Item>
</Tab> */}

</>
  );
};

export default DataManager;
