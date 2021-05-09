import React, { useEffect, useState } from 'react';
import { Link, logger } from 'ice';
import { ResponsiveGrid , Tab , Table, Button,Dialog,Progress} from '@alifd/next';
import PageHeader from '@/components/PageHeader';
import styles from '@/components/index.module.scss';

const { Cell } = ResponsiveGrid;

const Task = () => {


   
  const [result,setResult] = useState([])
  const [dialogShow,setDialogShow] = useState(false)
  const [dialogMsg,setDialogMsg] = useState("")
  const [curTaskId,setCurTaskId] = useState()
  const [curTask,setCurTask] = useState({})


 
  useEffect(()=>{
    let url = `/quant/meta_tables`
    fetch(url).then(res=>res.json()).then(data=>{
      setResult(data)
    })

  },[])

  const dataSource = [
  {id:1,name: "更新基础股票信息", desc:"更新基础表:quant_stockbasic", run_cycle: '手动',task_type:"数据获取",},
  {id:2,name: "股票日K线", desc:"更新基础表:quant_stock_trade_daily", run_cycle: '手动',task_type:"数据获取",}
];

  const closeDialog =(type,task) =>{
    console.log("type=",type)
    if(type == 'okClick'){
      if(task.id == 1){
        let url = `/quant/data_update?name=stock_basic`
        fetch(url).then(res=>res.json()).then(data=>{
          setResult(data)
        })
      }else if(task.id==2){
        let url = `/quant/data_update?name=stock_trade_daily`
        fetch(url).then(res=>res.json()).then(data=>{
          setResult(data)
        })
      }

    } 
    setDialogShow(false)
  }

  const openDialog=(record)=>{
    console.log("msg--," + record.name)
    setDialogShow(true)
    setDialogMsg(record.name)
    setCurTaskId(record.id)
    setCurTask(record)
    
  }

  const renderTaskRun = (value, index, record)=>{
    return <Button type="secondary" onClick={()=>openDialog(record)}>运行</Button>
  }

  const renderTaskProgress = (value, index, record)=>{
    return  <Progress percent={100} /> 
    // shape={'circle'}
  }

  return (
    <>
    <ResponsiveGrid gap={0}>
    <Cell colSpan={12}>
      <PageHeader
        breadcrumbs={[{ name: '任务管理' }]}
      />
    </Cell>

    <Cell colSpan={12} style={{padding:"10px"}}>
    <Table dataSource={dataSource}>
        <Table.Column title="任务ID" dataIndex="id"/>
        <Table.Column title="任务名称" dataIndex="name"/>
        <Table.Column title="任务描述" dataIndex="desc"/>
        <Table.Column title="运行周期" dataIndex="run_cycle"/>
        <Table.Column title="任务类型" dataIndex="task_type"/>
        <Table.Column title="进度" cell={renderTaskProgress}/>

        <Table.Column title="运行日志"  cell={(value,rowIdx,record) =><a href={["http://localhost:3333/#/data/" + record.name]}  target="_blank">日志</a>}/>
        <Table.Column title="操作"  cell={renderTaskRun}/>
    </Table>
    </Cell>
  </ResponsiveGrid>
  <Dialog
        title="运行任务"
        visible={dialogShow}
        onOk={closeDialog.bind(this,'okClick',curTask)}
        onCancel={closeDialog.bind(this,'cancelClick',curTask)}
        onClose={closeDialog.bind(this,'onClose',curTask)}>
        确定是否运行任务-{curTask.name}?
    </Dialog>

    {/* <Tab className={styles.TopHeader}>
    <Tab.Item title="表管理" key="1"></Tab.Item>
    <Tab.Item title="任务管理" key="2"></Tab.Item>
</Tab> */}

</>
  );
};

export default Task;
