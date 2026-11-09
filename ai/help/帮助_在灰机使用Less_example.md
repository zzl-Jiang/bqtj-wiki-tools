# 帮助:在灰机使用Less/example

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3A%E5%9C%A8%E7%81%B0%E6%9C%BA%E4%BD%BF%E7%94%A8Less/example
revid：41413 · 抓取时间：2026-11-09T14:27:10+08:00

---

本页以[[wandao:蛮力战士|部落与弯刀Wiki]]的技能树样式为例。

==Less==
<pre>
.unittree {
    a {
        color: inherit;
    }

    .unittree-grid {
        display: grid;
        gap: 12px 36px;
        padding: 72px 18px 18px;
        grid-template-columns: repeat(6, 200px);
        grid-template-rows: repeat(6, 84px);
        overflow-x: auto;
        border: 1px solid #947d52;
        background: #13110d;

        .unittree-item {
            position: relative;
            display: flex;
            justify-items: stretch;
            z-index: 50;
            margin: 0;
            transition: margin 0.2s linear;

            &:hover {
                margin: -6px;
            }


            .unit-icon {
                position: absolute;
                bottom: 0;
                right: 0;
                top: 0;
                left: 0;
                z-index: 0;

                &>p {
                    margin: 0 !important;
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    top: 0;
                    right: 0;
                    z-index: 0;
                    display: flex;
                    justify-items: flex-start;
                    align-items: flex-end;
                }
            }

            .unit-text {
                flex: 1;
                z-index: 50;
                position: relative;
                text-align: right;
                display: flex;
                gap: 6px;
                flex-direction: column;

                .unit-name {
                    flex: 1;
                    color: rgb(206, 199, 190);
                    padding: 4px 6px;
                }

                .unit-desc {
                    background: rgba(0, 0, 0, 0.4);

                    .unit-cost {
                        color: rgba(255, 255, 255, 0.6);
                        font-size: 12px;
                        display: flex;
                        align-items: center;
                        gap: 6px;

                        &>span {
                            display: flex;
                            align-items: center;

                            &>i {}

                            &>em {
                                font-style: normal;
                            }
                        }
                    }
                }

                .unit-types {
                    display: flex;
                    justify-content: flex-end;


                    .icon_unittype {
                        height: 24px;
                        width: 24px;
                    }
                }
            }
        }

        .unittree-arrow {
            display: grid;
            grid-template-columns: 200px 1fr 200px;
            grid-template-rows: 84px 1fr 84px;
            z-index: 20;

            .arrowparts-startcorner,
            .arrowparts-endcorner {
                display: grid;
                grid-template-columns: 1fr 6px 1fr;
                grid-template-rows: 1fr 6px 1fr;
            }

            /*上色*/
            .arrowcorner-start,
            .arrowcorner-end,
            .arrowcorner-center,
            .arrowcorner-repeat {
                background: rgb(197, 171, 81)
            }

            /*箭头组件定位*/
            .arrowparts-repeat {
                grid-column: 2;
                grid-row: 2;
                display: grid;
                grid-template-columns: 1fr 6px 1fr;
                grid-template-rows: 1fr 6px 1fr;

                .arrowcorner-repeat {
                    grid-row: 1/span 3;
                    grid-column: 2;
                }
            }

            &.unittree-arrow-down {
                .arrowparts-startcorner {
                    grid-column: 2;
                    grid-row: 1;

                    .arrowcorner-start {
                        grid-column: 1;
                        grid-row: 2;
                    }

                    .arrowcorner-end {
                        grid-column: 2;
                        grid-row: 3;
                    }

                    .arrowcorner-center {
                        grid-column: 2;
                        grid-row: 2;
                    }
                }

                .arrowparts-endcorner {
                    grid-column: 2;
                    grid-row: 3;

                    .arrowcorner-start {
                        grid-column: 2;
                        grid-row: 1;
                    }

                    .arrowcorner-end {
                        grid-column: 3;
                        grid-row: 2;
                    }

                    .arrowcorner-center {
                        grid-column: 2;
                        grid-row: 2;
                    }
                }
            }

            &.unittree-arrow-up {
                .arrowparts-endcorner {
                    grid-column: 2;
                    grid-row: 1;

                    .arrowcorner-start {
                        grid-column: 2;
                        grid-row: 3;
                    }

                    .arrowcorner-end {
                        grid-column: 3;
                        grid-row: 2;
                    }

                    .arrowcorner-center {
                        grid-column: 2;
                        grid-row: 2;
                    }
                }

                .arrowparts-startcorner {
                    grid-column: 2;
                    grid-row: 3;

                    .arrowcorner-start {
                        grid-column: 1;
                        grid-row: 2;
                    }

                    .arrowcorner-end {
                        grid-column: 2;
                        grid-row: 1;
                    }

                    .arrowcorner-center {
                        grid-column: 2;
                        grid-row: 2;
                    }
                }
            }

            &.unittree-arrow-horizontal {

                .arrowparts-startcorner,
                .arrowparts-endcorner {
                    display: none;
                }

                .arrowparts-repeat {
                    grid-row: 1;
                    grid-column: 1/span 3;

                    .arrowcorner-repeat {
                        grid-row: 2;
                        grid-column: 1/span 3;
                    }
                }
            }
        }

        .unittree-tierbg {
            grid-row: 1/span 7;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid #000;
            z-index: 10;
            margin: -60px -8px -6px;
            display: flex;
            padding: 6px;
            flex-direction: column;
            justify-items: stretch;

            .unittree-tierbg-title {
                text-align: center;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid #000;
                font-size: 16px;
                line-height: 32px;
                color: rgb(159, 144, 128);
            }

            &.unittree-tierbg-1 {
                grid-column: 1/span 1
            }

            &.unittree-tierbg-2 {
                grid-column: 2/span 1
            }

            &.unittree-tierbg-3 {
                grid-column: 3/span 1
            }

            &.unittree-tierbg-4 {
                grid-column: 4/span 1
            }

            &.unittree-tierbg-5 {
                grid-column: 5/span 1
            }

            &.unittree-tierbg-6 {
                grid-column: 6/span 1
            }
        }
    }
}
</pre>
==编译结果==
<pre>
.unittree a {
  color: inherit;
}
.unittree .unittree-grid {
  display: grid;
  gap: 12px 36px;
  padding: 72px 18px 18px;
  grid-template-columns: repeat(6, 200px);
  grid-template-rows: repeat(6, 84px);
  overflow-x: auto;
  border: 1px solid #947d52;
  background: #13110d;
}
.unittree .unittree-grid .unittree-item {
  position: relative;
  display: flex;
  justify-items: stretch;
  z-index: 50;
  margin: 0;
  transition: margin 0.2s linear;
}
.unittree .unittree-grid .unittree-item:hover {
  margin: -6px;
}
.unittree .unittree-grid .unittree-item .unit-icon {
  position: absolute;
  bottom: 0;
  right: 0;
  top: 0;
  left: 0;
  z-index: 0;
}
.unittree .unittree-grid .unittree-item .unit-icon > p {
  margin: 0 !important;
  position: absolute;
  bottom: 0;
  left: 0;
  top: 0;
  right: 0;
  z-index: 0;
  display: flex;
  justify-items: flex-start;
  align-items: flex-end;
}
.unittree .unittree-grid .unittree-item .unit-text {
  flex: 1;
  z-index: 50;
  position: relative;
  text-align: right;
  display: flex;
  gap: 6px;
  flex-direction: column;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-name {
  flex: 1;
  color: #cec7be;
  padding: 4px 6px;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-desc {
  background: rgba(0, 0, 0, 0.4);
}
.unittree .unittree-grid .unittree-item .unit-text .unit-desc .unit-cost {
  color: rgba(255, 255, 255, 0.6);
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-desc .unit-cost > span {
  display: flex;
  align-items: center;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-desc .unit-cost > span > em {
  font-style: normal;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-types {
  display: flex;
  justify-content: flex-end;
}
.unittree .unittree-grid .unittree-item .unit-text .unit-types .icon_unittype {
  height: 24px;
  width: 24px;
}
.unittree .unittree-grid .unittree-arrow {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: 84px 1fr 84px;
  z-index: 20;
  /*上色*/
  /*箭头组件定位*/
}
.unittree .unittree-grid .unittree-arrow .arrowparts-startcorner,
.unittree .unittree-grid .unittree-arrow .arrowparts-endcorner {
  display: grid;
  grid-template-columns: 1fr 6px 1fr;
  grid-template-rows: 1fr 6px 1fr;
}
.unittree .unittree-grid .unittree-arrow .arrowcorner-start,
.unittree .unittree-grid .unittree-arrow .arrowcorner-end,
.unittree .unittree-grid .unittree-arrow .arrowcorner-center,
.unittree .unittree-grid .unittree-arrow .arrowcorner-repeat {
  background: #c5ab51;
}
.unittree .unittree-grid .unittree-arrow .arrowparts-repeat {
  grid-column: 2;
  grid-row: 2;
  display: grid;
  grid-template-columns: 1fr 6px 1fr;
  grid-template-rows: 1fr 6px 1fr;
}
.unittree .unittree-grid .unittree-arrow .arrowparts-repeat .arrowcorner-repeat {
  grid-row: 1 / span 3;
  grid-column: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-startcorner {
  grid-column: 2;
  grid-row: 1;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-startcorner .arrowcorner-start {
  grid-column: 1;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-startcorner .arrowcorner-end {
  grid-column: 2;
  grid-row: 3;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-startcorner .arrowcorner-center {
  grid-column: 2;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-endcorner {
  grid-column: 2;
  grid-row: 3;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-endcorner .arrowcorner-start {
  grid-column: 2;
  grid-row: 1;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-endcorner .arrowcorner-end {
  grid-column: 3;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-down .arrowparts-endcorner .arrowcorner-center {
  grid-column: 2;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-endcorner {
  grid-column: 2;
  grid-row: 1;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-endcorner .arrowcorner-start {
  grid-column: 2;
  grid-row: 3;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-endcorner .arrowcorner-end {
  grid-column: 3;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-endcorner .arrowcorner-center {
  grid-column: 2;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-startcorner {
  grid-column: 2;
  grid-row: 3;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-startcorner .arrowcorner-start {
  grid-column: 1;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-startcorner .arrowcorner-end {
  grid-column: 2;
  grid-row: 1;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-up .arrowparts-startcorner .arrowcorner-center {
  grid-column: 2;
  grid-row: 2;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-horizontal .arrowparts-startcorner,
.unittree .unittree-grid .unittree-arrow.unittree-arrow-horizontal .arrowparts-endcorner {
  display: none;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-horizontal .arrowparts-repeat {
  grid-row: 1;
  grid-column: 1 / span 3;
}
.unittree .unittree-grid .unittree-arrow.unittree-arrow-horizontal .arrowparts-repeat .arrowcorner-repeat {
  grid-row: 2;
  grid-column: 1 / span 3;
}
.unittree .unittree-grid .unittree-tierbg {
  grid-row: 1 / span 7;
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid #000;
  z-index: 10;
  margin: -60px -8px -6px;
  display: flex;
  padding: 6px;
  flex-direction: column;
  justify-items: stretch;
}
.unittree .unittree-grid .unittree-tierbg .unittree-tierbg-title {
  text-align: center;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid #000;
  font-size: 16px;
  line-height: 32px;
  color: #9f9080;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-1 {
  grid-column: 1 / span 1;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-2 {
  grid-column: 2 / span 1;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-3 {
  grid-column: 3 / span 1;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-4 {
  grid-column: 4 / span 1;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-5 {
  grid-column: 5 / span 1;
}
.unittree .unittree-grid .unittree-tierbg.unittree-tierbg-6 {
  grid-column: 6 / span 1;
}
</pre>
