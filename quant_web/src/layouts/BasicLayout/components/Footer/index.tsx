import React from 'react';
import styles from './index.module.scss';

export default function Footer() {
  return (
    <p className={styles.footer}>
      <span className={styles.logo}>量化分析平台</span>
      <br />
      <span className={styles.copyright}>© 2021 - by 康凯</span>
    </p>
  );
}
