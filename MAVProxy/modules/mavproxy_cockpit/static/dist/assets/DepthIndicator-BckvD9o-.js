import{c as r,u as p,K as m,M as f,Y as w,r as g,w as h,Z as u,k as v,l as k,m as x,n as t,t as i,q as c,$ as b}from"./index-BUkzlHeJ.js";const _="data:image/svg+xml,%3c?xml%20version='1.0'%20encoding='UTF-8'%20standalone='no'?%3e%3csvg%20height='512'%20viewBox='0%200%20448%20512'%20version='1.1'%20id='svg1013'%20sodipodi:docname='depth-icon.svg'%20width='448'%20inkscape:version='1.2.2%20(b0a84865,%202022-12-01)'%20xmlns:inkscape='http://www.inkscape.org/namespaces/inkscape'%20xmlns:sodipodi='http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:svg='http://www.w3.org/2000/svg'%20%3e%3cdefs%20id='defs1017'%20/%3e%3csodipodi:namedview%20id='namedview1015'%20pagecolor='%23ffffff'%20bordercolor='%23000000'%20borderopacity='0.25'%20inkscape:showpageshadow='2'%20inkscape:pageopacity='0.0'%20inkscape:pagecheckerboard='0'%20inkscape:deskcolor='%23d1d1d1'%20showgrid='false'%20inkscape:zoom='0.97458415'%20inkscape:cx='321.67566'%20inkscape:cy='282.68467'%20inkscape:window-width='1612'%20inkscape:window-height='851'%20inkscape:window-x='732'%20inkscape:window-y='159'%20inkscape:window-maximized='0'%20inkscape:current-layer='svg1013'%20/%3e%3c!--!%20Font%20Awesome%20Free%206.4.0%20by%20@fontawesome%20-%20https://fontawesome.com%20License%20-%20https://fontawesome.com/license%20(Commercial%20License)%20Copyright%202023%20Fonticons,%20Inc.%20--%3e%3cpath%20d='m%20222.46088,499.00158%20c%2017.7,0%2031.92636,-14.30015%2032,-32%20l%201.02608,-246.61275%2025.4,25.4%20c%2012.5,12.5%2032.8,12.5%2045.3,0%2012.5,-12.5%2012.5,-32.8%200,-45.3%20l%20-80,-80%20c%20-12.5,-12.5%20-32.8,-12.5%20-45.3,0%20l%20-80,80%20c%20-12.5,12.5%20-12.5,32.8%200,45.3%2012.5,12.5%2032.8,12.5%2045.3,0%20l%2025.3,-25.4%20-1.02608,246.61275%20c%20-0.0736,17.69985%2014.3,32%2032,32%20z%20M%20209.58779,18.923421%20c%20-17.52836,15.5%20-38.95191,26.1%20-60.37547,26.1%20-20.95613,0%20-60.297562,-26.1%20-60.297562,-26.1%20v%200%20c%200,0%20-21.890978,-7.8%20-30.538303,1.7%20-11.218152,11.9%20-25.318745,21%20-39.419338,25.2%20-13.3994595,4%20-16.9390419,22.226079%20-13.8228887,39.426079%203.1161527,17.2%2011.7194847,26.87392%2025.1189437,22.87392%2019.086439,-5.7%2034.97882,-16.499999%2045.34003,-24.999999%2022.592107,15.599998%2047.910858,25.899999%2073.619118,25.899999%2024.85133,0%2047.20973,-9.900001%2062.63468,-18.899999%204.51843,-2.7%208.64733,-5.3%2012.153,-7.7%203.50567,2.4%207.55667,5.1%2012.153,7.7%2015.42496,8.999998%2037.78336,18.899999%2062.63468,18.899999%2025.70826,0%2051.02701,-10.300001%2073.61912,-25.799999%2010.43911,8.4%2026.25359,19.299999%2045.34003,24.999999%2013.39946,4%2022.00279,-4.64784%2025.11894,-21.847842%203.11616,-17.2%20-0.42343,-36.452157%20-13.82289,-40.452157%20-14.10059,-4.2%20-28.20118,-13.3%20-39.41934,-25.2%20-8.64732,-9.4%20-30.5383,-1.7%20-30.5383,-1.7%20v%200%20c%200,0%20-39.34143,26%20-60.29756,26%20-21.42356,0%20-42.84711,-10.6%20-60.37547,-26.1%20-8.64733,-7.9%20-20.17709,-7.9%20-28.82442,0%20z'%20id='path1011'%20sodipodi:nodetypes='sscsssssssccsscsssccsccscccsccsccssscc'%20style='fill:%23fff'%20/%3e%3c/svg%3e",y={class:"w-[8.5rem] h-12 p-1 text-white relative"},D={class:"absolute left-[3rem] flex flex-col items-start justify-center select-none"},S={class:"font-mono text-xl font-semibold leading-6 w-fit"},C={class:"text-xl font-semibold leading-6 w-fit"},B=r({__name:"DepthIndicator",setup(F){const n=p(),{displayUnitPreferences:a}=m();f.registerUsage(w.depth);const o=g(0);h(n.altitude,()=>{const e=n.altitude.msl,s=u(-e.value,e.toJSON().unit);if(s.value<.01){o.value=0;return}const l=s.to(a.distance);o.value=l.toJSON().value});const d=v(()=>{const e=o.value;return e<10?2:e>=10&&e<1e3?1:0});return(e,s)=>(k(),x("div",y,[s[1]||(s[1]=t("img",{src:_,class:"h-[80%] left-[0.5rem] top-[13%] absolute",draggable:!1},null,-1)),t("div",D,[t("div",null,[t("span",S,i(o.value.toFixed(d.value)),1),t("span",C,i(" ")+i(c(b)[c(a).distance]),1)]),s[0]||(s[0]=t("span",{class:"w-full text-sm font-semibold leading-4 whitespace-nowrap"},"Depth",-1))])]))}});export{B as default};
