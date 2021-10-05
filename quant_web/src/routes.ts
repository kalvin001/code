import BasicLayout from '@/layouts/BasicLayout';
import DataManager from '@/pages/DataManager';
import StockBasic from '@/pages/DataAnalysis'
import StockDetail from '@/pages/DataAnalysis/stock_detail'

import Task from '@/pages/Task'
import Trade from '@/pages/Trade'
import FutuTrade from '@/pages/Trade/futu'





const routerConfig = [
  {
    path: '/',
    component: BasicLayout,
    children: [
      {
        path: '/analysis/stock_basic',
        component: StockBasic,
      },
      {
        path: '/analysis/stock_detail',
        component: StockDetail,
      },
      {
        path: '/trade/futu',
        component: FutuTrade,
      },
      {
        path: '/data',
        exact: true,
        component: DataManager,
      },  {
        path: '/task',
        exact: true,
        component: Task,
      }, {
        path: '/trade',
        exact: true,
        component: Trade,
      }
    ],
  },
];
export default routerConfig;
