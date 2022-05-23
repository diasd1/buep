import{s as p,o,c as i,C as n,p as c,f as u,a as s,r as b,b as r,k as f,w as y}from"./vendor.dd02f02e.js";import{_ as h}from"./index.f44c382b.js";const S=p({props:{initialState:Boolean},data(){return{active:this.initialState}},watch:{active(){this.$emit("onChange",this.active)},initialState(){this.active=this.initialState}}}),k=e=>(c("data-v-704b8e31"),e=e(),u(),e),$=k(()=>s("div",{class:"bubble"},null,-1)),C=[$];function M(e,t,_,v,m,g){return o(),i("div",{onClick:t[0]||(t[0]=l=>e.active=!e.active),class:n(["toggle",{active:e.active}])},C,2)}var T=h(S,[["render",M],["__scopeId","data-v-704b8e31"]]);const w=p({name:"Maintenance",watch:{lightMode(){window.setTheme(this.lightMode?"default":"dark")}},methods:{quit(){fetch("/system/exit")},restart(){fetch("/system/reboot")},enableAuto(){fetch("/auto/enable")},disableAuto(){fetch("/auto/disable")},getRecommendedSpeeds(){fetch("/auto").then(e=>e.json()).then(e=>{this.speedL=e.speedL,this.speedR=e.speedR})},setSpeedLR(e,t){fetch("/rover/speed",{method:"POST",body:JSON.stringify({speedL:e,speedR:t})})},setSpeeds(){this.setSpeedLR(Number(this.speedL),Number(this.speedR)),setTimeout(()=>this.setSpeedLR(127,127),1e3)}},data(){return this.$nextTick(()=>{this.lightMode=window.getCurrentTheme()=="default"}),{speedL:127,speedR:127,lightMode:!1}},components:{Toggler:T}}),d=e=>(c("data-v-615af6a6"),e=e(),u(),e),A={class:"maintenance"},L={class:"settingsWrapper",key:1},R=d(()=>s("h4",null,"Application",-1)),I={class:"content"},B={class:"settingsWrapper",style:{"transition-delay":"0.25s"},key:4},N=d(()=>s("h4",null,"Self Drive",-1)),E={class:"content"},q={class:"settingsWrapper",style:{"transition-delay":"0.5s"},key:3},O=d(()=>s("h4",null,"Theme",-1)),W={class:"content"};function D(e,t,_,v,m,g){const l=b("Toggler");return o(),i("div",A,[r(f,{name:"list",appear:""},{default:y(()=>[(o(),i("div",L,[R,s("div",I,[s("button",{class:"accent",onClick:t[0]||(t[0]=(...a)=>e.restart&&e.restart(...a))},"Restart"),s("button",{onClick:t[1]||(t[1]=(...a)=>e.quit&&e.quit(...a))},"Quit")])])),(o(),i("div",B,[N,s("div",E,[s("button",{onClick:t[2]||(t[2]=(...a)=>e.enableAuto&&e.enableAuto(...a))},"ENABLE"),s("button",{onClick:t[3]||(t[3]=(...a)=>e.disableAuto&&e.disableAuto(...a))},"DISABLE")])])),(o(),i("div",q,[O,s("div",W,[s("span",{class:n(["clickable material-symbols-rounded",{selected:!e.lightMode}])},"dark_mode",2),r(l,{class:"toggler",initialState:e.lightMode,onOnChange:t[4]||(t[4]=a=>e.lightMode=a)},null,8,["initialState"]),s("span",{class:n(["clickable material-symbols-rounded",{selected:e.lightMode}])},"light_mode",2)])]))]),_:1})])}var G=h(w,[["render",D],["__scopeId","data-v-615af6a6"]]);export{G as default};
