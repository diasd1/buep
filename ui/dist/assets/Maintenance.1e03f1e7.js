import{_ as p}from"./index.1b01894e.js";import{l as i,o as a,c as r,a as t,t as n,p as l,d as c}from"./vendor.48d55495.js";const u=i({name:"Maintenance",methods:{quit(){fetch("/system/exit")},restart(){fetch("/system/reboot")},getRecommendedSpeeds(){fetch("/auto").then(e=>e.json()).then(e=>{this.speedL=e.speedL,this.speedR=e.speedR})},setSpeedLR(e,s){fetch("/rover/speed",{method:"POST",body:JSON.stringify({speedL:e,speedR:s})})},setSpeeds(){this.setSpeedLR(Number(this.speedL),Number(this.speedR)),setTimeout(()=>this.setSpeedLR(127,127),1e3)}},data(){return{speedL:127,speedR:127}}}),d=e=>(l("data-v-4d998712"),e=e(),c(),e),m={class:"maintenance"},_={class:"settingsWrapper"},S=d(()=>t("p",null,"Application",-1)),h={class:"content"},f={class:"settingsWrapper"},v=d(()=>t("p",null,"Propose Direction",-1)),R={class:"content"},L={class:"info"};function b(e,s,g,y,k,C){return a(),r("div",m,[t("div",_,[S,t("div",h,[t("button",{onClick:s[0]||(s[0]=(...o)=>e.restart&&e.restart(...o))},"Restart"),t("button",{onClick:s[1]||(s[1]=(...o)=>e.quit&&e.quit(...o))},"Quit")])]),t("div",f,[v,t("div",R,[t("button",{onClick:s[2]||(s[2]=(...o)=>e.getRecommendedSpeeds&&e.getRecommendedSpeeds(...o))},"GET"),t("div",L,[t("p",null,"Speed L: "+n(e.speedL),1),t("p",null,"Speed R: "+n(e.speedR),1)]),t("button",{onClick:s[3]||(s[3]=(...o)=>e.setSpeeds&&e.setSpeeds(...o))},"Set for 1s")])])])}var $=p(u,[["render",b],["__scopeId","data-v-4d998712"]]);export{$ as default};