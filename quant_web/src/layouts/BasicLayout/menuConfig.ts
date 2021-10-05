const headerMenuConfig = [];

const asideMenuConfig = [
  {
    name: '数据管理',
    path: '/data',
    icon: 'smile',
  },  
  {
    name: '任务管理',
    path: '/task',
    icon: 'smile',
  },  
  {
    name: '数据分析',
    path: '/data1',
    icon: 'smile',
    children: [
      {
        name: '股票列表',
        path: '/analysis/stock_basic',
      },   {
        name: '股票详情',
        path: '/analysis/stock_detail',
      },
    ]
  },
  {
    name: '量化策略',
    path: '/data2',
    icon: 'smile',
  },  
  {
    name: '实盘对接',
    path: '/trade',
    icon: 'smile',   
    children: [
      {
        name: '富途',
        path: '/trade/futu',
      },  {
        name: '同花顺',
        path: '/trade',
      },
    ]
  },
  {
    name: '对外开放',
    path: '/data4',
    icon: 'smile',
  },
];

export { headerMenuConfig, asideMenuConfig };
